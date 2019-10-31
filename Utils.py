import IconsManager as iconsmanager
import CasesManager as casesmanager
import ComputerPlaying as computerplaying
import PossibleCombinations as possiblecombinations
import MultiPlayer as multiplayer
import threading

entity_win = 0

finish_game = False

render_switchBtn = 0
render_multiBtn = 0

mp_txt = 0

f_canvas = 0
f_NW = 0

def verifyWin(cases_player, cases_computer, canvas, NW, msg_draw, msg_win, msg_lose) :
    global entity_win

    if(1 in cases_player and 2 in cases_player and 3 in cases_player):
        entity_win = 1
    if(4 in cases_player and 5 in cases_player and 6 in cases_player):
        entity_win = 1
    if(7 in cases_player and 8 in cases_player and 9 in cases_player):
        entity_win = 1
    if(1 in cases_player and 4 in cases_player and 7 in cases_player):
        entity_win = 1
    if(2 in cases_player and 5 in cases_player and 8 in cases_player):
        entity_win = 1
    if(3 in cases_player and 6 in cases_player and 9 in cases_player):
        entity_win = 1
    if(1 in cases_player and 5 in cases_player and 9 in cases_player):
        entity_win = 1
    if(3 in cases_player and 5 in cases_player and 7 in cases_player):
        entity_win = 1

    if(1 in cases_computer and 2 in cases_computer and 3 in cases_computer):
        entity_win = 2
    if(4 in cases_computer and 5 in cases_computer and 6 in cases_computer):
        entity_win = 2
    if(7 in cases_computer and 8 in cases_computer and 9 in cases_computer):
        entity_win = 2
    if(1 in cases_computer and 4 in cases_computer and 7 in cases_computer):
        entity_win = 2
    if(2 in cases_computer and 5 in cases_computer and 8 in cases_computer):
        entity_win = 2
    if(3 in cases_computer and 6 in cases_computer and 9 in cases_computer):
        entity_win = 2
    if(1 in cases_computer and 5 in cases_computer and 9 in cases_computer):
        entity_win = 2
    if(3 in cases_computer and 5 in cases_computer and 7 in cases_computer):
        entity_win = 2

    if entity_win == 1:
        print("Joueur gagne !")
        computerplaying.stop_computer_playing = 1
        printGameMsg(canvas, NW, 1, msg_draw, msg_win, msg_lose)
    if entity_win == 2:  
        print("Ordinateur gagne !")  
        computerplaying.stop_computer_playing = 1
        printGameMsg(canvas, NW, 2, msg_draw, msg_win, msg_lose)

    cases_total = len(cases_player) + len(cases_computer)
    if(cases_total == 9 and entity_win == 0):
        print("Match nul !")
        computerplaying.stop_computer_playing = 1
        printGameMsg(canvas, NW, 0, msg_draw, msg_win, msg_lose)


image_msg_delete = 0

# 0 = match nul | 1 = joueur gagne | 2 = ordinateur gagne
def printGameMsg(canvas, NW, gameStat, msg_draw, msg_win, msg_lose):
    global finish_game
    global image_msg_delete
    global render_switchBtn

    for i in range(9):
        casesmanager.deleteCase(canvas, i+1)

    canvas.delete(render_switchBtn)

    if gameStat == 0:
        image_draw = canvas.create_image(180, 130, image=msg_draw, anchor=NW)
        image_msg_delete = image_draw
    elif gameStat == 1:
        image_win = canvas.create_image(180, 130, image=msg_win, anchor=NW)
        image_msg_delete = image_win
    elif gameStat == 2:
        image_lose = canvas.create_image(180, 130, image=msg_lose, anchor=NW)
        image_msg_delete = image_lose

    finish_game = True


def reloadGame(canvas, NW, switchBtn, case1, case2, case3, case4, case5, case6, case7, case8, case9):
    global image_msg_delete
    global entity_win
    global image_msg_delete
    global render_switchBtn

    canvas.delete(image_msg_delete)
    iconsmanager.deleteIcons(canvas)
    casesmanager.createCasesButton(canvas, NW, case1, case2, case3, case4, case5, case6, case7, case8, case9)

    computerplaying.start_game = False
    createSwitchButton(canvas, NW, switchBtn)

    del computerplaying.cases_player[:]
    del computerplaying.cases_computer[:]
    del possiblecombinations.combinationsTreated[:]
    del possiblecombinations.computerAttackTreated[:]

    possiblecombinations.defend = 0
    possiblecombinations.attack = 0

    computerplaying.player_play = 1
    entity_win = 0
    image_msg_delete = 0
    computerplaying.stop_computer_playing = 0


def switchingIcon(canvas, label_player, label_computer):
    if computerplaying.switchIcon == False and computerplaying.start_game == False:
        canvas.itemconfigure(label_player, text="Ordinateur")
        canvas.itemconfigure(label_computer, text="Votre Pion")
        computerplaying.switchIcon = True
    elif computerplaying.switchIcon == True and computerplaying.start_game == False:
        canvas.itemconfigure(label_player, text="Votre Pion")
        canvas.itemconfigure(label_computer, text="Ordinateur")
        computerplaying.switchIcon = False


def createSwitchButton(canvas, NW, switchBtn):
    global render_switchBtn
    render_switchBtn = canvas.create_window(800, 310, anchor=NW, window=switchBtn)

def createMultiButton(canvas, NW, multiBtn):
    global render_multiBtn
    render_multiBtn = canvas.create_window(715, 480, anchor=NW, window=multiBtn)

f_multiImage = 0
f_multiBtn = 0

def createMultiFrame(canvas, NW, multiImage, multiBtn):
    global render_switchBtn
    global mp_txt
    global f_canvas
    global f_NW
    global f_multiImage
    global f_multiBtn

    f_canvas = canvas
    f_NW = NW
    f_multiImage = multiImage
    f_multiBtn = multiBtn

    if computerplaying.start_game == False:

        for i in range(9):
            casesmanager.deleteCase(canvas, i+1)

        canvas.delete(render_switchBtn)

        multiBtn.config(state="disabled")

        canvas.create_image(180, 130, image=multiImage, anchor=NW)
        mp_txt = canvas.create_text(500,300,fill="white",font="null 20")

        updateMultiplayerLabel(1)

        multiplayer.multiplayer = True

        t = threading.Timer(1, multiplayer.initConnection)
        t.start()

def updateMultiplayerLabel(status):
    global f_canvas
    global mp_txt

    if status == 0:
        f_canvas.itemconfigure(mp_txt, text="Erreur réseau : Veuillez vérifiez votre \n             connexion internet !")
    elif status == 1:
        f_canvas.itemconfigure(mp_txt, text="Connexion au serveur de jeu en cours,\n       merci de bien vouloir patienter")
    elif status == 2:
        f_canvas.itemconfigure(mp_txt, text="Connexion au serveur réussi ! \n       En attente de joueur ...")
    elif status == 3:
        f_canvas.itemconfigure(mp_txt, text="La partie va pouvoir commencer !")
    elif status == 4:
        f_canvas.itemconfigure(mp_txt, text="Le joueur adverse c'est déconnecté !")
