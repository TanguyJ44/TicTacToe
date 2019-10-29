from tkinter import *
import os
import IconsManager as iconsmanager
import CasesManager as casesmanager
import ComputerPlaying as computerplaying
import Utils as utils

Frame = Tk()

Frame.title('Tik Tac Toe - Tanguy J | Supinfo.com')
Frame.resizable(width=False, height=False)

canvas = Canvas(Frame,width=1000,height=650,bg="white")
canvas.pack()

base_folder = os.path.dirname(__file__)
image_path_bg = os.path.join(base_folder, 'imgs/background.png')
image_path_sheep = os.path.join(base_folder, 'imgs/sheep.png')
image_path_bird = os.path.join(base_folder, 'imgs/bird.png')
image_path_msg_win = os.path.join(base_folder, 'imgs/msg_win.png')
image_path_msg_lose = os.path.join(base_folder, 'imgs/msg_lose.png')
image_path_msg_draw = os.path.join(base_folder, 'imgs/msg_draw.png')
image_path_switch = os.path.join(base_folder, 'imgs/switch.png')
image_path_multi = os.path.join(base_folder, 'imgs/multi_btn.png')

photo = PhotoImage(file=image_path_bg)
icon_sheep = PhotoImage(file = image_path_sheep)
icon_bird = PhotoImage(file = image_path_bird)
msg_win = PhotoImage(file = image_path_msg_win)
msg_lose = PhotoImage(file = image_path_msg_lose)
msg_draw = PhotoImage(file = image_path_msg_draw)
image_switch = PhotoImage(file = image_path_switch)
image_multi = PhotoImage(file = image_path_multi)

canvas.create_image(0, 0, image=photo, anchor=NW)
label_player = canvas.create_text(850,260,fill="black",font="null 20",text="Votre Pion")
label_computer = canvas.create_text(850,380,fill="black",font="null 20",text="Ordinateur")

info_txt = canvas.create_text(180,619,fill="#0A7E70",font="null 15",text="C'est à vous de jouer !")
game_mode = canvas.create_text(840,619,fill="#0A7E70",font="null 15",text="Mode de jeu : Joueur VS Bot")

switchBtn = Button(Frame, anchor = W, image=image_switch, bg="#15BDAC", command=lambda: switchingIcon())
switchBtn.configure(width=30, height=15, activebackground = "#15BDAC", relief = FLAT, cursor='hand2')

multiBtn = Button(Frame, anchor = W, image=image_multi, bg="#15BDAC", command=lambda: switchingIcon())
multiBtn.configure(width=199, height=50, activebackground = "#15BDAC", relief = FLAT, cursor='hand2')

utils.createSwitchButton(canvas, NW, switchBtn)
utils.createMultiButton(canvas, NW, multiBtn)

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


def createCasesButton():
    casesmanager.createCasesButton(canvas, NW, case1, case2, case3, case4, case5, case6, case7, case8, case9)

createCasesButton()


def switchingIcon():
    utils.switchingIcon(canvas, label_player, label_computer)


def setCaseIcon(caseId):
    computerplaying.setCaseIcon(canvas, caseId, icon_bird, icon_sheep, NW, msg_draw, msg_win, msg_lose, info_txt)


def mouseClickLeftButton(event):
    if utils.finish_game == True:
        utils.reloadGame(canvas, NW, switchBtn, case1, case2, case3, case4, case5, case6, case7, case8, case9)
        utils.finish_game = False


Frame.bind("<Button-1>", mouseClickLeftButton)

Frame.mainloop()