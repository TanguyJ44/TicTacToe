from tkinter import *

Fenetre = Tk()

zone_dessin = Canvas(Fenetre,width=1000,height=650,bg="white",bd=8)
zone_dessin.pack()

zone_dessin.create_rectangle(50,50,600,600,width=2)

zone_dessin.create_line(50,230,600,230,fill="red",width=2)
zone_dessin.create_line(50,420,600,420,fill="red",width=2)

zone_dessin.create_line(230,50,230,600,fill="red",width=2)
zone_dessin.create_line(420,50,420,600,fill="red",width=2)

Fenetre.mainloop()