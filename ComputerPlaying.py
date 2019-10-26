from random import randint
import IconsManager as iconsmanager
import CasesManager as casesmanager
import Utils as utils

start_game = False

cases_player = []
cases_computer = []

player_play = 1

stop_computer_playing = 0

switchIcon = False

def playComputer(canvas, switchIcon, info_txt, icon_bird, icon_sheep, NW, stop_computer_playing,msg_draw, msg_win, msg_lose):
    global player_play
    global cases_computer
    
    random_case = randint(1,9)

    if(random_case in cases_computer):
        playComputer(canvas, switchIcon, info_txt, icon_bird, icon_sheep, NW, stop_computer_playing,msg_draw, msg_win, msg_lose)
    elif(random_case in cases_player):
        playComputer(canvas, switchIcon, info_txt, icon_bird, icon_sheep, NW, stop_computer_playing,msg_draw, msg_win, msg_lose)
    else:
        casesmanager.deleteCase(canvas, random_case)
        if switchIcon == False:
            iconsmanager.setIcon(canvas, 0, random_case, icon_bird, icon_sheep, NW)
        else:
            iconsmanager.setIcon(canvas, 1, random_case, icon_bird, icon_sheep, NW)
        player_play = 1
        cases_computer.insert(0, random_case)
        utils.verifyWin(cases_player, cases_computer, canvas, NW, msg_draw, msg_win, msg_lose)
        canvas.itemconfigure(info_txt, text="C'est à vous de jouer !")
        canvas.coords(info_txt, 180, 619)


def setCaseIcon(canvas, caseId, icon_bird, icon_sheep, NW, msg_draw, msg_win, msg_lose, info_txt):
    global player_play
    global cases_player
    global start_game

    if start_game == False:
        start_game = True

    if player_play == 1:
        casesmanager.deleteCase(canvas, caseId)
        if switchIcon == False:
            iconsmanager.setIcon(canvas, 1, caseId, icon_bird, icon_sheep, NW)
        else:
            iconsmanager.setIcon(canvas, 0, caseId, icon_bird, icon_sheep, NW)
        player_play = 0
        cases_player.insert(0, caseId)
        utils.verifyWin(cases_player, cases_computer, canvas, NW, msg_draw, msg_win, msg_lose)
        if stop_computer_playing == 0:
            playComputer(canvas, switchIcon, info_txt, icon_bird, icon_sheep, NW, stop_computer_playing,msg_draw, msg_win, msg_lose)
