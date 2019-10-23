from tkinter import *
import os

Frame = Tk()

Frame.title('Tik Tac Toe - Supinfo')
Frame.resizable(width=False, height=False)

canvas = Canvas(Frame,width=1000,height=650,bg="white")
canvas.pack()

base_folder = os.path.dirname(__file__)
image_path_bg = os.path.join(base_folder, 'imgs/background.png')
image_path_sheep = os.path.join(base_folder, 'imgs/sheep.png')
image_path_bird = os.path.join(base_folder, 'imgs/bird.png')

photo = PhotoImage(file=image_path_bg)

icon_sheep = PhotoImage(file = image_path_sheep)
icon_bird = PhotoImage(file = image_path_bird)

canvas.create_image(0, 0, image=photo, anchor=NW)

canvas.create_text(850,260,fill="black",font="null 20",text="Votre Pion")

canvas.create_text(850,380,fill="black",font="null 20",text="Ordinateur")

case1 = Button(Frame, anchor = W, bg="#15BDAC", command=lambda: setCaseIcon(1, 1))
case2 = Button(Frame, anchor = W, bg="#15BDAC", command=lambda: setCaseIcon(2, 1))
case3 = Button(Frame, anchor = W, bg="#15BDAC", command=lambda: setCaseIcon(3, 1))
case4 = Button(Frame, anchor = W, bg="#15BDAC", command=lambda: setCaseIcon(4, 1))
case5 = Button(Frame, anchor = W, bg="#15BDAC", command=lambda: setCaseIcon(5, 1))
case6 = Button(Frame, anchor = W, bg="#15BDAC", command=lambda: setCaseIcon(6, 1))
case7 = Button(Frame, anchor = W, bg="#15BDAC", command=lambda: setCaseIcon(7, 1))
case8 = Button(Frame, anchor = W, bg="#15BDAC", command=lambda: setCaseIcon(8, 1))
case9 = Button(Frame, anchor = W, bg="#15BDAC", command=lambda: setCaseIcon(9, 1))

case1.configure(width=21, height=10, activebackground = "#33B5E5", relief = FLAT)
case2.configure(width=21, height=10, activebackground = "#33B5E5", relief = FLAT)
case3.configure(width=21, height=10, activebackground = "#33B5E5", relief = FLAT)
case4.configure(width=21, height=10, activebackground = "#33B5E5", relief = FLAT)
case5.configure(width=21, height=10, activebackground = "#33B5E5", relief = FLAT)
case6.configure(width=21, height=10, activebackground = "#33B5E5", relief = FLAT)
case7.configure(width=21, height=10, activebackground = "#33B5E5", relief = FLAT)
case8.configure(width=21, height=10, activebackground = "#33B5E5", relief = FLAT)
case9.configure(width=21, height=10, activebackground = "#33B5E5", relief = FLAT)

case1_render = canvas.create_window(39, 60, anchor=NW, window=case1)
case2_render = canvas.create_window(213, 60, anchor=NW, window=case2)
case3_render = canvas.create_window(389, 60, anchor=NW, window=case3)
case4_render = canvas.create_window(39, 237, anchor=NW, window=case4)
case5_render = canvas.create_window(213, 235, anchor=NW, window=case5)
case6_render = canvas.create_window(389, 235, anchor=NW, window=case6)
case7_render = canvas.create_window(39, 413, anchor=NW, window=case7)
case8_render = canvas.create_window(213, 413, anchor=NW, window=case8)
case9_render = canvas.create_window(389, 413, anchor=NW, window=case9)

def setCaseIcon(caseId, iconType):
    deleteCase(caseId)
    setIcon(iconType, caseId)

def deleteCase(caseId):
    if caseId == 1:
        canvas.delete(case1_render)
    if caseId == 2:
        canvas.delete(case2_render)
    if caseId == 3:
        canvas.delete(case3_render)
    if caseId == 4:
        canvas.delete(case4_render)
    if caseId == 5:
        canvas.delete(case5_render)
    if caseId == 6:
        canvas.delete(case6_render)
    if caseId == 7:
        canvas.delete(case7_render)
    if caseId == 8:
        canvas.delete(case8_render)
    if caseId == 9:
        canvas.delete(case9_render)


def setIcon(iconType, caseId):
    if iconType == 0:
        if caseId == 1:
            canvas.create_image(60,80,image=icon_bird,anchor=NW)
        if caseId == 2:
            canvas.create_image(240,80,image=icon_bird,anchor=NW) 
        if caseId == 3:
            canvas.create_image(420,80,image=icon_bird,anchor=NW) 
        if caseId == 4:
            canvas.create_image(60,260,image=icon_bird,anchor=NW)
        if caseId == 5:
            canvas.create_image(240,260,image=icon_bird,anchor=NW) 
        if caseId == 6:
            canvas.create_image(420,260,image=icon_bird,anchor=NW)
        if caseId == 7:
            canvas.create_image(60,440,image=icon_bird,anchor=NW)
        if caseId == 8:
            canvas.create_image(240,440,image=icon_bird,anchor=NW) 
        if caseId == 9:
            canvas.create_image(420,440,image=icon_bird,anchor=NW) 
            
    else:
        if caseId == 1:
            canvas.create_image(60,80,image=icon_sheep,anchor=NW)
        if caseId == 2:
            canvas.create_image(240,80,image=icon_sheep,anchor=NW) 
        if caseId == 3:
            canvas.create_image(420,80,image=icon_sheep,anchor=NW) 
        if caseId == 4:
            canvas.create_image(60,260,image=icon_sheep,anchor=NW)
        if caseId == 5:
            canvas.create_image(240,260,image=icon_sheep,anchor=NW) 
        if caseId == 6:
            canvas.create_image(420,260,image=icon_sheep,anchor=NW)
        if caseId == 7:
            canvas.create_image(60,440,image=icon_sheep,anchor=NW)
        if caseId == 8:
            canvas.create_image(240,440,image=icon_sheep,anchor=NW) 
        if caseId == 9:
            canvas.create_image(420,440,image=icon_sheep,anchor=NW)       



# canvas.delete(case1_render)
# canvas.create_image(10,10,image=icon_sheep,anchor=NW)



Frame.mainloop()




#15BDAC

# canvas.create_rectangle(50,50,600,600,width=2)

# canvas.create_line(50,230,600,230,fill="red",width=2)
# canvas.create_line(50,420,600,420,fill="red",width=2)

# canvas.create_line(230,50,230,600,fill="red",width=2)
# canvas.create_line(420,50,420,600,fill="red",width=2)