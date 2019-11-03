# Ce module regroupe un enssemble d'instruction utile a la connexion au serveur 3tS (TicTacToe Server) 
# L'authentification des clients est réalisé par un token unique, merci de ne pas connecter un client autre que celui-ci

import socket
import Utils as utils
import threading
import ComputerPlaying as computerplaying
import CasesManager as casesmanager
import IconsManager as iconsmanager

multiplayer = False
quitMP = True

# Les données suivantes corresponde au serveur d'authentification des clients
# Ne pas changer les données ci-dessous
# Si le serveur est inaccessible, les requêtes peuvent être redirigé vers un serveur local
hote = "217.182.67.57"
port = 1212

global_soc = 0

main_player = False

loop = 0
run = 1

# Initialisation de la connexion avec le serveur et demande d'autorisation de connexion sur le réseau
def initConnection():
    global global_soc
    global quitMP
    global loop

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((hote, port))

        global_soc = s
        
        print("Initialized connection with the server !")
        utils.updateMultiplayerLabel(2)

        quitMP = False

        loop = threading.Thread(target=listeningLoop, args=(s,))
        loop.start()
        loop.join()

    except:
        print("Connection error with the server !")
        utils.updateMultiplayerLabel(0)

    finally:
        pass

# Fonction permettant de ce déconnecter du serveur de jeu
def disconnect():
    global global_soc
    global quitMP
    global multiplayer

    quitMP = True
    multiplayer = False
    global_soc.close()

# Écoute des instruction du serveur
def listeningLoop(soc):
    global run

    print("func")

    datas = ""

    while run:
        datas = soc.recv(4096)

        if(datas != ""):
            print("Paquet : ", datas)
            packetAnalyzer(datas)
            datas = ""

# Envoie de paquet au serveur
def sendPacket(packet):
    global global_soc
    global_soc.send(packet.encode())

# Analyse les paquets afin de les utiliser
def packetAnalyzer(packet):
    global main_player 
    global quitMP
    global loop
    global run

    packet = packet.decode()
    
    if "case" in packet:
        case = packet[4:]
        case = case[:1]

        print(case)

        casesmanager.deleteCase(utils.f_canvas, int(case))
        if main_player == True:
            iconsmanager.setIcon(utils.f_canvas, 0, int(case), utils.icon_bird, utils.icon_sheep, utils.f_NW)
        else:
            iconsmanager.setIcon(utils.f_canvas, 1, int(case), utils.icon_bird, utils.icon_sheep, utils.f_NW)

        utils.f_canvas.itemconfigure(utils.info_txt, text="C'est à vous de jouer !")
        utils.f_canvas.coords(utils.info_txt, 180, 619)

        computerplaying.player_play = 1

    elif "wait" in packet:
        if "1" in packet:
            main_player = True
            computerplaying.player_play = 1
            print("wait 1")
        else:
            main_player = False
            computerplaying.player_play = 0
            utils.updateMultiplayerLabel(3)
            utils.f_canvas.itemconfigure(utils.info_txt, text="C'est à l'Adversaire de jouer !")
            utils.f_canvas.coords(utils.info_txt, 215, 619)
            print("wait 2")

    elif "newplayer" in packet:
        utils.updateMultiplayerLabel(3)

    elif "start" in packet:
        
        utils.f_canvas.delete(utils.mpFrame)
        utils.f_canvas.delete(utils.mp_txt)

        utils.reloadGame(utils.f_canvas, utils.f_NW, utils.switchBtn)

        if main_player == True and computerplaying.switchIcon == True:
            utils.switchingIcon(utils.f_canvas, utils.label_player, utils.label_computer)
        elif main_player == False and computerplaying.switchIcon == False:
            utils.switchingIcon(utils.f_canvas, utils.label_player, utils.label_computer)

        utils.switchGameMode()

        if main_player == False:
            computerplaying.player_play = 0

        computerplaying.start_game = True
        computerplaying.stop_computer_playing = 1

    elif "gamestat" in packet:
        loop = threading.currentThread()
        run = 0

        disconnect()
        quitMP = True

        computerplaying.start_game = False

        utils.createMultiFrame(utils.f_canvas, utils.f_NW, utils.f_multiImage, utils.f_multiBtn, 0)

        if "0" in packet:
            utils.updateMultiplayerLabel(6)
        elif "1" in packet:
            utils.updateMultiplayerLabel(5)
        elif "2" in packet:
            utils.updateMultiplayerLabel(7)

    elif "quit" in packet:
        disconnect()
        utils.createMultiFrame(utils.f_canvas, utils.f_NW, utils.f_multiImage, utils.f_multiBtn, 0)
        utils.updateMultiplayerLabel(4)
