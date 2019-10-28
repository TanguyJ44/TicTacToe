from random import randint

combinationsTreated = []
computerAttackTreated = []

cases_player = []
cases_computer = []

defend = 0
attack = 0

def calcCombinations(c_player, c_computer):
    global combinationsTreated
    global computerAttackTreated
    global defend
    global cases_player
    global cases_computer

    cases_player = c_player
    cases_computer = c_computer

    lower = 1
    upper = 2
    result = 3
    index = 1

    position = 0
    update = False
    cycle = 1

    for i in range(23):

        if(lower in cases_player and upper in cases_player and index not in combinationsTreated and checkCaseEmpty(result) == True):
            combinationsTreated.insert(0, index)
            defend = result
            update = True

        if cycle == 1:
            if position == 0:
                lower+=1
                upper+=1
                result-=2
                position+=1
            elif position == 1:
                lower-=1
                result+=1
                position+=1
            elif position == 2:
                lower+=3
                upper+=2
                result+=4
                position = 0
        if cycle == 2:
            if position == 0:
                lower+=3
                upper+=3
                result-=6
                position+=1
            elif position == 1:
                lower-=3
                result+=3
                position+=1
            elif position == 2:
                lower+=1
                upper-=2
                result+=4
                position = 0
        if cycle == 3:
            if position == 0:
                lower+=4
                upper+=4
                result-=8
                position+=1
            elif position == 1:
                lower-=4
                result+=4
                position+=1
            elif position == 2:
                lower+=2
                upper-=4
                result+=2
                position = 0
        if cycle == 4:
            if position == 0:
                lower+=2
                upper+=2
                result-=4
                position+=1
            elif position == 1:
                lower-=2
                result+=2
                position+=1

        if i == 8:
            lower=1
            upper=4
            result=7
            position = 0
            cycle+=1
        elif i == 17:
            lower=1
            upper=5
            result=9
            position = 0
            cycle+=1
        elif i == 20:
            cycle+=1

        index+=1

    if update == False:
        defend = 0


    computerAttack(cases_computer)

    print(defend)
    print(attack)

    if(defend > 0 and attack == 0):
        return defend
    elif(attack > 0 and defend == 0):
        return attack
    elif(defend > 0 and attack > 0):
        return attack
    elif(defend == 0 and attack == 0):
        for i in range(1, 9):
            if(i not in cases_player and i not in cases_computer):
                return i


def computerAttack(cases_computer):
    global computerAttackTreated
    global attack

    if(1 in cases_computer and 2 in cases_computer and 1 not in computerAttackTreated and checkCaseEmpty(3) == True):
        computerAttackTreated.insert(0, 1)
        attack = 3
    elif(2 in cases_computer and 3 in cases_computer and 2 not in computerAttackTreated and checkCaseEmpty(1) == True):
        computerAttackTreated.insert(0, 2)
        attack = 1   
    elif(1 in cases_computer and 3 in cases_computer and 3 not in computerAttackTreated and checkCaseEmpty(2) == True):
        computerAttackTreated.insert(0, 3)
        attack = 2    

    elif(4 in cases_computer and 5 in cases_computer and 4 not in computerAttackTreated and checkCaseEmpty(6) == True):
        computerAttackTreated.insert(0, 4)
        attack = 6
    elif(5 in cases_computer and 6 in cases_computer and 5 not in computerAttackTreated and checkCaseEmpty(4) == True):
        computerAttackTreated.insert(0, 5)
        attack = 4   
    elif(4 in cases_computer and 6 in cases_computer and 6 not in computerAttackTreated and checkCaseEmpty(5) == True):
        computerAttackTreated.insert(0, 6)
        attack = 5

    elif(7 in cases_computer and 8 in cases_computer and 7 not in computerAttackTreated and checkCaseEmpty(9) == True):
        computerAttackTreated.insert(0, 7)
        attack = 9
    elif(8 in cases_computer and 9 in cases_computer and 8 not in computerAttackTreated and checkCaseEmpty(7) == True):
        computerAttackTreated.insert(0, 8)
        attack = 7   
    elif(7 in cases_computer and 9 in cases_computer and 9 not in computerAttackTreated and checkCaseEmpty(8) == True):
        computerAttackTreated.insert(0, 9)
        attack = 8

    elif(1 in cases_computer and 4 in cases_computer and 10 not in computerAttackTreated and checkCaseEmpty(7) == True):
        computerAttackTreated.insert(0, 10)
        attack = 7
    elif(4 in cases_computer and 7 in cases_computer and 11 not in computerAttackTreated and checkCaseEmpty(1) == True):
        computerAttackTreated.insert(0, 11)
        attack = 1  
    elif(1 in cases_computer and 7 in cases_computer and 12 not in computerAttackTreated and checkCaseEmpty(4) == True):
        computerAttackTreated.insert(0, 12)
        attack = 4

    elif(2 in cases_computer and 5 in cases_computer and 13 not in computerAttackTreated and checkCaseEmpty(8) == True):
        computerAttackTreated.insert(0, 13)
        attack = 8
    elif(5 in cases_computer and 8 in cases_computer and 14 not in computerAttackTreated and checkCaseEmpty(2) == True):
        computerAttackTreated.insert(0, 14)
        attack = 2
    elif(2 in cases_computer and 8 in cases_computer and 15 not in computerAttackTreated and checkCaseEmpty(5) == True):
        computerAttackTreated.insert(0, 15)
        attack = 5

    elif(3 in cases_computer and 6 in cases_computer and 16 not in computerAttackTreated and checkCaseEmpty(9) == True):
        computerAttackTreated.insert(0, 16)
        attack = 9
    elif(6 in cases_computer and 9 in cases_computer and 17 not in computerAttackTreated and checkCaseEmpty(3) == True):
        computerAttackTreated.insert(0, 17)
        attack = 3
    elif(3 in cases_computer and 9 in cases_computer and 18 not in computerAttackTreated and checkCaseEmpty(6) == True):
        computerAttackTreated.insert(0, 18)
        attack = 6

    elif(1 in cases_computer and 5 in cases_computer and 19 not in computerAttackTreated and checkCaseEmpty(9) == True):
        computerAttackTreated.insert(0, 19)
        attack = 9
    elif(5 in cases_computer and 9 in cases_computer and 20 not in computerAttackTreated and checkCaseEmpty(1) == True):
        computerAttackTreated.insert(0, 20)
        attack = 1
    elif(1 in cases_computer and 9 in cases_computer and 21 not in computerAttackTreated and checkCaseEmpty(5) == True):
        computerAttackTreated.insert(0, 21)
        attack = 5

    elif(3 in cases_computer and 5 in cases_computer and 22 not in computerAttackTreated and checkCaseEmpty(7) == True):
        computerAttackTreated.insert(0, 22)
        attack = 7
    elif(5 in cases_computer and 7 in cases_computer and 23 not in computerAttackTreated and checkCaseEmpty(3) == True):
        computerAttackTreated.insert(0, 23)
        attack = 3
    elif(3 in cases_computer and 7 in cases_computer and 24 not in computerAttackTreated and checkCaseEmpty(5) == True):
        computerAttackTreated.insert(0, 24)
        attack = 5
        
    else:
        attack = 0


def checkCaseEmpty(caseNumber):
    if(caseNumber not in cases_player and caseNumber not in cases_computer):
        return True
    else:
        return False