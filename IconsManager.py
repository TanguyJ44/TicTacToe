icon_bird1_render = 0
icon_bird2_render = 0
icon_bird3_render = 0
icon_bird4_render = 0
icon_bird5_render = 0
icon_bird6_render = 0
icon_bird7_render = 0
icon_bird8_render = 0
icon_bird9_render = 0

icon_sheep1_render = 0
icon_sheep2_render = 0
icon_sheep3_render = 0
icon_sheep4_render = 0
icon_sheep5_render = 0
icon_sheep6_render = 0
icon_sheep7_render = 0
icon_sheep8_render = 0
icon_sheep9_render = 0


def setIcon(canvas, iconType, caseId, icon_bird, icon_sheep, NW):
    global icon_bird1_render
    global icon_bird2_render
    global icon_bird3_render
    global icon_bird4_render
    global icon_bird5_render
    global icon_bird6_render
    global icon_bird7_render
    global icon_bird8_render
    global icon_bird9_render

    global icon_sheep1_render
    global icon_sheep2_render
    global icon_sheep3_render
    global icon_sheep4_render
    global icon_sheep5_render
    global icon_sheep6_render
    global icon_sheep7_render
    global icon_sheep8_render
    global icon_sheep9_render

    if iconType == 0:
        if caseId == 1:
            icon_bird1_render = canvas.create_image(60,80,image=icon_bird,anchor=NW)
        if caseId == 2:
            icon_bird2_render = canvas.create_image(240,80,image=icon_bird,anchor=NW) 
        if caseId == 3:
            icon_bird3_render = canvas.create_image(420,80,image=icon_bird,anchor=NW) 
        if caseId == 4:
            icon_bird4_render = canvas.create_image(60,260,image=icon_bird,anchor=NW)
        if caseId == 5:
            icon_bird5_render = canvas.create_image(240,260,image=icon_bird,anchor=NW) 
        if caseId == 6:
            icon_bird6_render = canvas.create_image(420,260,image=icon_bird,anchor=NW)
        if caseId == 7:
            icon_bird7_render = canvas.create_image(60,440,image=icon_bird,anchor=NW)
        if caseId == 8:
            icon_bird8_render = canvas.create_image(240,440,image=icon_bird,anchor=NW) 
        if caseId == 9:
            icon_bird9_render = canvas.create_image(420,440,image=icon_bird,anchor=NW) 

    else:
        if caseId == 1:
            icon_sheep1_render = canvas.create_image(60,80,image=icon_sheep,anchor=NW)
        if caseId == 2:
            icon_sheep2_render = canvas.create_image(240,80,image=icon_sheep,anchor=NW) 
        if caseId == 3:
            icon_sheep3_render = canvas.create_image(420,80,image=icon_sheep,anchor=NW) 
        if caseId == 4:
            icon_sheep4_render = canvas.create_image(60,260,image=icon_sheep,anchor=NW)
        if caseId == 5:
            icon_sheep5_render = canvas.create_image(240,260,image=icon_sheep,anchor=NW) 
        if caseId == 6:
            icon_sheep6_render = canvas.create_image(420,260,image=icon_sheep,anchor=NW)
        if caseId == 7:
            icon_sheep7_render = canvas.create_image(60,440,image=icon_sheep,anchor=NW)
        if caseId == 8:
            icon_sheep8_render = canvas.create_image(240,440,image=icon_sheep,anchor=NW) 
        if caseId == 9:
            icon_sheep9_render = canvas.create_image(420,440,image=icon_sheep,anchor=NW)


def deleteIcons(canvas):
    global icon_bird1_render
    global icon_bird2_render
    global icon_bird3_render
    global icon_bird4_render
    global icon_bird5_render
    global icon_bird6_render
    global icon_bird7_render
    global icon_bird8_render
    global icon_bird9_render

    global icon_sheep1_render
    global icon_sheep2_render
    global icon_sheep3_render
    global icon_sheep4_render
    global icon_sheep5_render
    global icon_sheep6_render
    global icon_sheep7_render
    global icon_sheep8_render
    global icon_sheep9_render

    canvas.delete(icon_bird1_render)
    canvas.delete(icon_bird2_render)
    canvas.delete(icon_bird3_render)
    canvas.delete(icon_bird4_render)
    canvas.delete(icon_bird5_render)
    canvas.delete(icon_bird6_render)
    canvas.delete(icon_bird7_render)
    canvas.delete(icon_bird8_render)
    canvas.delete(icon_bird9_render)

    canvas.delete(icon_sheep1_render)
    canvas.delete(icon_sheep2_render)
    canvas.delete(icon_sheep3_render)
    canvas.delete(icon_sheep4_render)
    canvas.delete(icon_sheep5_render)
    canvas.delete(icon_sheep6_render)
    canvas.delete(icon_sheep7_render)
    canvas.delete(icon_sheep8_render)
    canvas.delete(icon_sheep9_render)