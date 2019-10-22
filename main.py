from tkinter import *
import os

Fenetre = Tk()

Fenetre.title('Tik Tac Toe')
Fenetre.resizable(width=False, height=False)

zone_dessin = Canvas(Fenetre,width=1000,height=650,bg="white",bd=8)
zone_dessin.pack()

base_folder = os.path.dirname(__file__)
image_path = os.path.join(base_folder, 'imgs/background.png')

photo = PhotoImage(file=image_path)

zone_dessin.create_image(0, 0, image=photo, anchor=NW)

zone_dessin.create_text(850,260,fill="black",font="null 20",text="Votre Pion")

zone_dessin.create_text(850,380,fill="black",font="null 20",text="Ordinateur")

# zone_dessin.create_rectangle(50,50,600,600,width=2)

# zone_dessin.create_line(50,230,600,230,fill="red",width=2)
# zone_dessin.create_line(50,420,600,420,fill="red",width=2)

# zone_dessin.create_line(230,50,230,600,fill="red",width=2)
# zone_dessin.create_line(420,50,420,600,fill="red",width=2)

Fenetre.mainloop()