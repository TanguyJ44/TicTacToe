import socket
import Utils as utils
import threading

multiplayer = False

#hote = "217.182.67.57"
hote = "192.168.1.23"
port = 1212

def initConnection():

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((hote, port))
        
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


def disconnect(soc):
    soc.close()


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
    soc.send(packet)


def packetAnalyzer(packet):

    test = "test"

    if test in packet:
        print("!!")