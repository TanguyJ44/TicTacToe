import socket
import Utils as utils
import threading

multiplayer = False

#hote = "217.182.67.57"
hote = "192.168.1.23"
port = 1212

global_soc = 0

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


def sendPacket(soc, packet):
    soc.send(packet.encode())


def packetAnalyzer(packet):
    packet = packet.decode()
    
    if "case" in packet:
        print("Case packet !")
    elif "wait" in packet:
        if "1" in packet:
            pass
        else:
            pass

    elif "start" in packet:
        print("Start")
    elif "quit" in packet:
        disconnect()
        utils.createMultiFrame(utils.f_canvas, utils.f_NW, utils.f_multiImage, utils.f_multiBtn)
        utils.updateMultiplayerLabel(2)
