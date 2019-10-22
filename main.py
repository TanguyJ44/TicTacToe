from tkinter import *
import os

Frame = Tk()

Frame.title('Tik Tac Toe - Supinfo')
Frame.resizable(width=False, height=False)

canvas = Canvas(Frame,width=1000,height=650,bg="white")
canvas.pack()

base_folder = os.path.dirname(__file__)
image_path = os.path.join(base_folder, 'imgs/background.png')

photo = PhotoImage(file=image_path)

canvas.create_image(0, 0, image=photo, anchor=NW)

canvas.create_text(850,260,fill="black",font="null 20",text="Votre Pion")

canvas.create_text(850,380,fill="black",font="null 20",text="Ordinateur")

def myfonc(nameBtn):
    print("Case : ", nameBtn)

case1 = Button(Frame, text = "1", anchor = W, bg="#15BDAC", command=lambda: myfonc(1))
case2 = Button(Frame, text = "2", anchor = W, bg="#15BDAC", command=lambda: myfonc(2))
case3 = Button(Frame, text = "3", anchor = W, bg="#15BDAC", command=lambda: myfonc(3))
case4 = Button(Frame, text = "4", anchor = W, bg="#15BDAC", command=lambda: myfonc(4))
case5 = Button(Frame, text = "5", anchor = W, bg="#15BDAC", command=lambda: myfonc(5))
case6 = Button(Frame, text = "6", anchor = W, bg="#15BDAC", command=lambda: myfonc(6))
case7 = Button(Frame, text = "7", anchor = W, bg="#15BDAC", command=lambda: myfonc(7))
case8 = Button(Frame, text = "8", anchor = W, bg="#15BDAC", command=lambda: myfonc(8))
case9 = Button(Frame, text = "9", anchor = W, bg="#15BDAC", command=lambda: myfonc(9))

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

Frame.mainloop()




#15BDAC

# canvas.create_rectangle(50,50,600,600,width=2)

# canvas.create_line(50,230,600,230,fill="red",width=2)
# canvas.create_line(50,420,600,420,fill="red",width=2)

# canvas.create_line(230,50,230,600,fill="red",width=2)
# canvas.create_line(420,50,420,600,fill="red",width=2)