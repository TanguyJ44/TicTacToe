# Ce module regroupe un ensemble d'instructions permettant d'effectuer tout type d'actions. 
# Il s'agit en quelque sorte d'une classe "fourre-tout" qui reste néanmoins bien pratique 
# pour y stocker toutes les fonctions utiles au bon fonctionnement du jeu.

import IconsManager as iconsmanager
import CasesManager as casesmanager
import ComputerPlaying as computerplaying
import PossibleCombinations as possiblecombinations
import MultiPlayer as multiplayer
import threading

# Défini qui remporte la partie
# 0 = match nul, 1 = joueur gagne, 2 = ordinateur gagne (ou joueur adverse dans le cas d'une partie multijoueur)
entity_win = 0

# Défini la partie comme terminée
finish_game = False

# Initialisation des variables de rendu des composants
render_switchBtn = 0
render_multiBtn = 0

# Initialisation de l'état du bouton de changement de pion
switchBtn = 0

# Initialisation du menu multijoueur
mpFrame = 0
mp_txt = 0

# Création d'une instance canvas et NW
f_canvas = 0
f_NW = 0

# Initialisation des icons et composants de textes
icon_bird = 0
icon_sheep = 0
info_txt = 0
label_player = 0
label_computer = 0

# Initialisation du mode de jeu (joueur vs bot ou multijoueur)
game_mode = 0
mode = 0

# Initialisation des 9 cases du plateau
case1 = 0
case2 = 0
case3 = 0
case4 = 0
case5 = 0
case6 = 0
case7 = 0
case8 = 0
case9 = 0

# Fonction d'initialisation de toutes les variables ci-dessus afin de leur affecter une donnée
def init(ic_bird, ic_sheep, swBtn, lb_player, lb_computer, c1, c2, c3, c4, c5, c6, c7, c8, c9, g_mode, label_txt):
    global icon_bird
    global icon_sheep
    global switchBtn
    global info_txt
    global label_player
    global label_computer
    global case1, case2, case3, case4, case5, case6, case7, case8, case9
    global game_mode

    icon_bird = ic_bird
    icon_sheep = ic_sheep
    label_player = lb_player
    label_computer = lb_computer

    switchBtn = swBtn
    info_txt = label_txt
    game_mode = g_mode

    case1 = c1
    case2 = c2
    case3 = c3
    case4 = c4
    case5 = c5
    case6 = c6
    case7 = c7
    case8 = c8
    case9 = c9

# Fonction permetant de détecter un gagnant, un perdant ou un match nul
def verifyWin(cases_player, cases_computer, canvas, NW, msg_draw, msg_win, msg_lose) :
    global entity_win

    # Vérification du jeu du joueur
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

    # Vérification du jeu de l'ordinateur
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

    # Si le joueur gagne, la condition est vérifiée
    if entity_win == 1:
        print("Joueur gagne !")
        computerplaying.stop_computer_playing = 1
        printGameMsg(canvas, NW, 1, msg_draw, msg_win, msg_lose)

    # Si l'ordinateur gagne, la condition est vérifiée
    if entity_win == 2:  
        print("Ordinateur gagne !")  
        computerplaying.stop_computer_playing = 1
        printGameMsg(canvas, NW, 2, msg_draw, msg_win, msg_lose)

    cases_total = len(cases_player) + len(cases_computer)
    # Si match nul, la condition est vérifiée
    if(cases_total == 9 and entity_win == 0):
        print("Match nul !")
        computerplaying.stop_computer_playing = 1
        printGameMsg(canvas, NW, 0, msg_draw, msg_win, msg_lose)


image_msg_delete = 0

# Fonction d'affichage du message de fin de partie
# 0 = match nul | 1 = joueur gagne | 2 = ordinateur gagne
def printGameMsg(canvas, NW, gameStat, msg_draw, msg_win, msg_lose):
    global finish_game
    global image_msg_delete
    global render_switchBtn

    # Suppression des 9 cases du plateau pour laisser la place au message de fin de partie
    for i in range(9):
        casesmanager.deleteCase(canvas, i+1)

    # Suppression du bouton d'échange de pion
    canvas.delete(render_switchBtn)

    # Affichage du message approprié
    if gameStat == 0:
        image_draw = canvas.create_image(180, 130, image=msg_draw, anchor=NW)
        image_msg_delete = image_draw
    elif gameStat == 1:
        image_win = canvas.create_image(180, 130, image=msg_win, anchor=NW)
        image_msg_delete = image_win
    elif gameStat == 2:
        image_lose = canvas.create_image(180, 130, image=msg_lose, anchor=NW)
        image_msg_delete = image_lose

    # Définir la fin de la partie
    finish_game = True

# Fonction permettant de remettre le jeu à zero pour une nouvelle partie
def reloadGame(canvas, NW, switchBtn):
    global image_msg_delete
    global entity_win
    global image_msg_delete
    global render_switchBtn

    # Suppression des composants de fin de partie
    canvas.delete(image_msg_delete)
    iconsmanager.deleteIcons(canvas)
    casesmanager.createCasesButton(canvas, NW, case1, case2, case3, case4, case5, case6, case7, case8, case9)

    # Restauration du bouton d'échange d'icon
    computerplaying.start_game = False
    createSwitchButton(canvas, NW, switchBtn)

    # Suppression des tableaux de stockage de donnée
    del computerplaying.cases_player[:]
    del computerplaying.cases_computer[:]
    del possiblecombinations.combinationsTreated[:]
    del possiblecombinations.computerAttackTreated[:]

    # Réinitialisation des variables de jeu de l'ordinateur
    possiblecombinations.defend = 0
    possiblecombinations.attack = 0

    # Réinitialisation des variables de jeu
    computerplaying.player_play = 1
    entity_win = 0
    image_msg_delete = 0
    computerplaying.stop_computer_playing = 0

# Fonction permettant l'échange d'icon
def switchingIcon(canvas, label_player, label_computer):
    if computerplaying.switchIcon == False and computerplaying.start_game == False:
        canvas.itemconfigure(label_player, text="Ordinateur")
        canvas.itemconfigure(label_computer, text="Votre Pion")
        computerplaying.switchIcon = True
    elif computerplaying.switchIcon == True and computerplaying.start_game == False:
        canvas.itemconfigure(label_player, text="Votre Pion")
        canvas.itemconfigure(label_computer, text="Ordinateur")
        computerplaying.switchIcon = False

# Fonction permettant de créer le bouton d'échange d'icon sur le canvas
def createSwitchButton(canvas, NW, switchBtn):
    global render_switchBtn
    render_switchBtn = canvas.create_window(800, 310, anchor=NW, window=switchBtn)

# Fonction permettant de créer le bouton multijoueur sur le canvas
def createMultiButton(canvas, NW, multiBtn):
    global render_multiBtn
    render_multiBtn = canvas.create_window(715, 480, anchor=NW, window=multiBtn)

f_multiImage = 0
f_multiBtn = 0

# Fonction permettant de créer le menu de connexion multijoueur
def createMultiFrame(canvas, NW, multiImage, multiBtn, init):
    global render_switchBtn
    global mp_txt
    global f_canvas
    global f_NW
    global f_multiImage
    global f_multiBtn
    global mpFrame

    f_canvas = canvas
    f_NW = NW
    f_multiImage = multiImage
    f_multiBtn = multiBtn

    if computerplaying.start_game == False:

        for i in range(9):
            casesmanager.deleteCase(canvas, i+1)

        canvas.delete(render_switchBtn)

        multiBtn.config(state="disabled")

        mpFrame = canvas.create_image(180, 130, image=multiImage, anchor=NW)
        mp_txt = canvas.create_text(500,300,fill="white",font="null 20")

        updateMultiplayerLabel(1)

        if init == 1:
            multiplayer.multiplayer = True

            t = threading.Timer(1, multiplayer.initConnection)
            t.start()

# Fonction permettant d'informer le joueur sur le jeu en temps réel (lors d'une partie multijoueur)
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
    elif status == 5:
        f_canvas.itemconfigure(mp_txt, text="Vous remportez la partie !")
    elif status == 6:
        f_canvas.itemconfigure(mp_txt, text="Vous perdez la partie !")
    elif status == 7:
        f_canvas.itemconfigure(mp_txt, text="Match Nul !")

# Informer le joueur sur le mode de jeu
def switchGameMode():
    global mode
    global game_mode
    global f_canvas

    if mode == 0:
        f_canvas.itemconfigure(game_mode, text="Mode de jeu : Multijoueur")
        mode = 1
    elif mode == 1:
        f_canvas.itemconfigure(game_mode, text="Mode de jeu : Joueur VS Bot")