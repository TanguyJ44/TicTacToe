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

    computerDefend(c_player)
    computerAttack(c_computer)

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
            if(i not in c_player and i not in c_computer):
                return i


def computerDefend(cases_player):
    global combinationsTreated
    global defend

    lower = 1
    upper = 2
    result = 3
    index = 1

    position = 0
    update = False
    cycle = 1

    for i in range(24):

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


def computerAttack(cases_computer):
    global computerAttackTreated
    global attack

    lower = 1
    upper = 2
    result = 3
    index = 1

    position = 0
    update = False
    cycle = 1

    for i in range(24):

        if(lower in cases_computer and upper in cases_computer and index not in computerAttackTreated and checkCaseEmpty(result) == True):
            computerAttackTreated.insert(0, index)
            attack = result
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
        attack = 0


def checkCaseEmpty(caseNumber):
    if(caseNumber not in cases_player and caseNumber not in cases_computer):
        return True
    else:
        return False