from tkinter import *
import os
import IconsManager as iconsmanager
import CasesManager as casesmanager
import ComputerPlaying as computerplaying
import Utils as utils
import MultiPlayer as multiplayer
import sys

# Initialisation de la frame
Frame = Tk()

# Définition d'attributs
Frame.title('Tik Tac Toe - Tanguy J | Supinfo.com')
Frame.resizable(width=False, height=False)

# Création d'un canvas
canvas = Canvas(Frame,width=1000,height=650,bg="white")
canvas.pack()

# Définition des ressources
base_folder = os.path.dirname(__file__)
image_path_bg = os.path.join(base_folder, 'imgs/background.png')
image_path_sheep = os.path.join(base_folder, 'imgs/sheep.png')
image_path_bird = os.path.join(base_folder, 'imgs/bird.png')
image_path_msg_win = os.path.join(base_folder, 'imgs/msg_win.png')
image_path_msg_lose = os.path.join(base_folder, 'imgs/msg_lose.png')
image_path_msg_draw = os.path.join(base_folder, 'imgs/msg_draw.png')
image_path_switch = os.path.join(base_folder, 'imgs/switch.png')
image_path_multi = os.path.join(base_folder, 'imgs/multi_btn.png')
image_path_frame_multi = os.path.join(base_folder, 'imgs/mp_stats.png')

# Création des images
photo = PhotoImage(file=image_path_bg)
icon_sheep = PhotoImage(file = image_path_sheep)
icon_bird = PhotoImage(file = image_path_bird)
msg_win = PhotoImage(file = image_path_msg_win)
msg_lose = PhotoImage(file = image_path_msg_lose)
msg_draw = PhotoImage(file = image_path_msg_draw)
image_switch = PhotoImage(file = image_path_switch)
image_multi = PhotoImage(file = image_path_multi)
image_frame_multi = PhotoImage(file = image_path_frame_multi)

# Placement des composants sur le canvas

canvas.create_image(0, 0, image=photo, anchor=NW)
label_player = canvas.create_text(850,260,fill="black",font="null 20",text="Votre Pion")
label_computer = canvas.create_text(850,380,fill="black",font="null 20",text="Ordinateur")

info_txt = canvas.create_text(180,619,fill="#0A7E70",font="null 15",text="C'est à vous de jouer !")
game_mode = canvas.create_text(840,619,fill="#0A7E70",font="null 15",text="Mode de jeu : Joueur VS Bot")

switchBtn = Button(Frame, anchor = W, image=image_switch, bg="#15BDAC", command=lambda: switchingIcon())
switchBtn.configure(width=30, height=15, activebackground = "#15BDAC", relief = FLAT, cursor='hand2')

multiBtn = Button(Frame, anchor = W, image=image_multi, bg="#15BDAC", command=lambda: utils.createMultiFrame(canvas, NW, image_frame_multi, multiBtn, 1))
multiBtn.configure(width=199, height=50, activebackground = "#15BDAC", relief = FLAT, cursor='hand2')

utils.createSwitchButton(canvas, NW, switchBtn)
utils.createMultiButton(canvas, NW, multiBtn)

# Création et placement des boutons de placement des pions sur le plateau
case1 = Button(Frame, anchor = W, bg="#15BDAC", command=lambda: setCaseIcon(1))
case2 = Button(Frame, anchor = W, bg="#15BDAC", command=lambda: setCaseIcon(2))
case3 = Button(Frame, anchor = W, bg="#15BDAC", command=lambda: setCaseIcon(3))
case4 = Button(Frame, anchor = W, bg="#15BDAC", command=lambda: setCaseIcon(4))
case5 = Button(Frame, anchor = W, bg="#15BDAC", command=lambda: setCaseIcon(5))
case6 = Button(Frame, anchor = W, bg="#15BDAC", command=lambda: setCaseIcon(6))
case7 = Button(Frame, anchor = W, bg="#15BDAC", command=lambda: setCaseIcon(7))
case8 = Button(Frame, anchor = W, bg="#15BDAC", command=lambda: setCaseIcon(8))
case9 = Button(Frame, anchor = W, bg="#15BDAC", command=lambda: setCaseIcon(9))

case1.configure(width=21, height=10, activebackground = "#15BDAC", relief = FLAT, cursor='hand2')
case2.configure(width=21, height=10, activebackground = "#15BDAC", relief = FLAT, cursor='hand2')
case3.configure(width=21, height=10, activebackground = "#15BDAC", relief = FLAT, cursor='hand2')
case4.configure(width=21, height=10, activebackground = "#15BDAC", relief = FLAT, cursor='hand2')
case5.configure(width=21, height=10, activebackground = "#15BDAC", relief = FLAT, cursor='hand2')
case6.configure(width=21, height=10, activebackground = "#15BDAC", relief = FLAT, cursor='hand2')
case7.configure(width=21, height=10, activebackground = "#15BDAC", relief = FLAT, cursor='hand2')
case8.configure(width=21, height=10, activebackground = "#15BDAC", relief = FLAT, cursor='hand2')
case9.configure(width=21, height=10, activebackground = "#15BDAC", relief = FLAT, cursor='hand2')

# Initialisation de certaines variables pour le module Utils
utils.init(icon_bird, icon_sheep, switchBtn, label_player, label_computer, case1, case2, case3, case4, case5, case6, case7, case8, case9, game_mode, info_txt)

# Fonction de création des boutons du plateau
def createCasesButton():
    casesmanager.createCasesButton(canvas, NW, case1, case2, case3, case4, case5, case6, case7, case8, case9)

# Appel de la fonction de création des boutons du plateau ci-dessus
createCasesButton()

# Fonction d'inversement des pions
def switchingIcon():
    utils.switchingIcon(canvas, label_player, label_computer)

# Fonction d'ajout du pion du joueur sur le plateau
def setCaseIcon(caseId):
    computerplaying.setCaseIcon(canvas, caseId, icon_bird, icon_sheep, NW, msg_draw, msg_win, msg_lose, info_txt)

# Évenement clique bouton de souris gauche
def mouseClickLeftButton(event):
    if utils.finish_game == True:
        utils.reloadGame(canvas, NW, switchBtn)
        utils.finish_game = False

# Évenement pression touche de clavier Échape
def keyEscapePressed(event):
    # Vérifié si le mode multijoueur est en cours
    if multiplayer.multiplayer == True:
        data = "quit"
        multiplayer.sendPacket(data)
        multiplayer.quitMP = True
        sys.exit(0)

    # Vérifié si le mode multijoueur vient juste d'être quitté
    if multiplayer.quitMP == True:
        canvas.delete(utils.mpFrame)
        canvas.delete(utils.mp_txt)
        utils.reloadGame(canvas, NW, switchBtn)
        multiplayer.quitMP = False
        utils.switchGameMode()
        multiBtn.config(state="active")
        canvas.itemconfigure(info_txt, text="C'est à vous de jouer !")
        canvas.coords(info_txt, 180, 619)

# Instruction d'écoute des évenements ci-dessus
Frame.bind("<Button-1>", mouseClickLeftButton)
Frame.bind('<Escape>', keyEscapePressed)

# Ordre de création de la Frame
Frame.mainloop()