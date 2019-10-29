import socket

multiplayer = False

#hote = "217.182.67.57"
hote = "192.168.1.23"
port = 1212

def initConnection():

    if multiplayer == False:

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((hote, port))

        print("Initialized connection with the server !")

    else:

        print("Client already initialized with the server !")