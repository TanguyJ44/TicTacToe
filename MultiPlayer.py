import socket
import Utils as utils
import threading
import ComputerPlaying as computerplaying
import CasesManager as casesmanager
import IconsManager as iconsmanager

multiplayer = False

#hote = "217.182.67.57"
hote = "192.168.1.23"
port = 1212

global_soc = 0

main_player = False

def initConnection():
    global global_soc

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((hote, port))

        global_soc = s
        
        print("Initialized connection with the server !")
        utils.updateMultiplayerLabel(2)

        loop = threading.Thread(target=listeningLoop, args=(s,))
        loop.start()
        loop.join()

    except:
        print("Connection error with the server !")
        utils.updateMultiplayerLabel(0)

    finally:
        pass


def disconnect():
    global global_soc
    global_soc.close()


def listeningLoop(soc):

    print("func")

    datas = ""

    while 1:
        datas = soc.recv(4096)

        if(datas != ""):
            print("Paquet : ", datas)
            packetAnalyzer(datas)
            datas = ""


def sendPacket(packet):
    global global_soc
    global_soc.send(packet.encode())


def packetAnalyzer(packet):
    global main_player 

    packet = packet.decode()
    
    if "case" in packet:
        case = packet[4:]

        casesmanager.deleteCase(utils.f_canvas, case)
        if main_player == True:
            iconsmanager.setIcon(utils.f_canvas, 1, case, utils.icon_bird, utils.icon_sheep, utils.f_NW)
        else:
            iconsmanager.setIcon(utils.f_canvas, 0, case, utils.icon_bird, utils.icon_sheep, utils.f_NW)

        utils.f_canvas.itemconfigure(utils.info_txt, text="C'est à vous de jouer !")
        utils.f_canvas.coords(utils.info_txt, 180, 619)

        computerplaying.player_play = 1

    elif "wait" in packet:
        if "1" in packet:
            main_player = True
            computerplaying.player_play = 1
        else:
            main_player = False
            computerplaying.player_play = 0
            utils.updateMultiplayerLabel(3)

    elif "newplayer" in packet:
        utils.updateMultiplayerLabel(3)

    elif "start" in packet:
        
        utils.f_canvas.delete(utils.mpFrame)
        utils.f_canvas.delete(utils.info_txt)

        utils.reloadGame(utils.f_canvas, utils.f_NW, 0)

        if main_player == True and computerplaying.switchIcon == True:
            utils.switchingIcon(utils.f_canvas, utils.label_player, utils.label_computer)
        elif main_player == False and computerplaying.switchIcon == False:
            utils.switchingIcon(utils.f_canvas, utils.label_player, utils.label_computer)

        computerplaying.start_game = True
        computerplaying.stop_computer_playing = 1

    elif "quit" in packet:
        disconnect()
        utils.createMultiFrame(utils.f_canvas, utils.f_NW, utils.f_multiImage, utils.f_multiBtn)
        utils.updateMultiplayerLabel(2)
