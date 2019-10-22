from tkinter import *
import os

Frame = Tk()

Frame.title('Tik Tac Toe - Supinfo')
Frame.resizable(width=False, height=False)

canvas = Canvas(Frame,width=1000,height=650,bg="white")
canvas.pack()

def myfonc(nameBtn):
    print("pressed : " + nameBtn)

base_folder = os.path.dirname(__file__)
image_path = os.path.join(base_folder, 'imgs/background.png')

photo = PhotoImage(file=image_path)

canvas.create_image(0, 0, image=photo, anchor=NW)

canvas.create_text(850,260,fill="black",font="null 20",text="Votre Pion")

canvas.create_text(850,380,fill="black",font="null 20",text="Ordinateur")

button1 = Button(Frame, text = "5", anchor = W, bg="#15BDAC", command=lambda: myfonc("5"))
button1.configure(width=21, height=10, activebackground = "#33B5E5", relief = FLAT)
button1_window = canvas.create_window(212, 235, anchor=NW, window=button1)

Frame.mainloop()

#15BDAC

# canvas.create_rectangle(50,50,600,600,width=2)

# canvas.create_line(50,230,600,230,fill="red",width=2)
# canvas.create_line(50,420,600,420,fill="red",width=2)

# canvas.create_line(230,50,230,600,fill="red",width=2)
# canvas.create_line(420,50,420,600,fill="red",width=2)