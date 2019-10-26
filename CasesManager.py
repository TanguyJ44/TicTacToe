case1_render = 0
case2_render = 0
case3_render = 0
case4_render = 0
case5_render = 0
case6_render = 0
case7_render = 0
case8_render = 0
case9_render = 0

def createCasesButton(canvas, NW, case1, case2, case3, case4, case5, case6, case7, case8, case9):
    global case1_render
    global case2_render
    global case3_render
    global case4_render
    global case5_render
    global case6_render
    global case7_render
    global case8_render
    global case9_render

    case1_render = canvas.create_window(39, 60, anchor=NW, window=case1)
    case2_render = canvas.create_window(213, 60, anchor=NW, window=case2)
    case3_render = canvas.create_window(389, 60, anchor=NW, window=case3)
    case4_render = canvas.create_window(39, 237, anchor=NW, window=case4)
    case5_render = canvas.create_window(213, 235, anchor=NW, window=case5)
    case6_render = canvas.create_window(389, 235, anchor=NW, window=case6)
    case7_render = canvas.create_window(39, 413, anchor=NW, window=case7)
    case8_render = canvas.create_window(213, 413, anchor=NW, window=case8)
    case9_render = canvas.create_window(389, 413, anchor=NW, window=case9)

def deleteCase(canvas, caseId):
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