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

    if(1 in cases_player and 2 in cases_player and 1 not in combinationsTreated and checkCaseEmpty(3) == True):
        combinationsTreated.insert(0, 1)
        defend = 3
    elif(2 in cases_player and 3 in cases_player and 2 not in combinationsTreated and checkCaseEmpty(1) == True):
        combinationsTreated.insert(0, 2)
        defend = 1   
    elif(1 in cases_player and 3 in cases_player and 3 not in combinationsTreated and checkCaseEmpty(2) == True):
        combinationsTreated.insert(0, 3)
        defend = 2    

    elif(4 in cases_player and 5 in cases_player and 4 not in combinationsTreated and checkCaseEmpty(6) == True):
        combinationsTreated.insert(0, 4)
        defend = 6
    elif(5 in cases_player and 6 in cases_player and 5 not in combinationsTreated and checkCaseEmpty(4) == True):
        combinationsTreated.insert(0, 5)
        defend = 4   
    elif(4 in cases_player and 6 in cases_player and 6 not in combinationsTreated and checkCaseEmpty(5) == True):
        combinationsTreated.insert(0, 6)
        defend = 5

    elif(7 in cases_player and 8 in cases_player and 7 not in combinationsTreated and checkCaseEmpty(9) == True):
        combinationsTreated.insert(0, 7)
        defend = 9
    elif(8 in cases_player and 9 in cases_player and 8 not in combinationsTreated and checkCaseEmpty(7) == True):
        combinationsTreated.insert(0, 8)
        defend = 7   
    elif(7 in cases_player and 9 in cases_player and 9 not in combinationsTreated and checkCaseEmpty(8) == True):
        combinationsTreated.insert(0, 9)
        defend = 8

    elif(1 in cases_player and 4 in cases_player and 10 not in combinationsTreated and checkCaseEmpty(7) == True):
        combinationsTreated.insert(0, 10)
        defend = 7
    elif(4 in cases_player and 7 in cases_player and 11 not in combinationsTreated and checkCaseEmpty(1) == True):
        combinationsTreated.insert(0, 11)
        defend = 1  
    elif(1 in cases_player and 7 in cases_player and 12 not in combinationsTreated and checkCaseEmpty(4) == True):
        combinationsTreated.insert(0, 12)
        defend = 4

    elif(2 in cases_player and 5 in cases_player and 13 not in combinationsTreated and checkCaseEmpty(8) == True):
        combinationsTreated.insert(0, 13)
        defend = 8
    elif(5 in cases_player and 8 in cases_player and 14 not in combinationsTreated and checkCaseEmpty(2) == True):
        combinationsTreated.insert(0, 14)
        defend = 2
    elif(2 in cases_player and 8 in cases_player and 15 not in combinationsTreated and checkCaseEmpty(5) == True):
        combinationsTreated.insert(0, 15)
        defend = 5

    elif(3 in cases_player and 6 in cases_player and 16 not in combinationsTreated and checkCaseEmpty(9) == True):
        combinationsTreated.insert(0, 16)
        defend = 9
    elif(6 in cases_player and 9 in cases_player and 17 not in combinationsTreated and checkCaseEmpty(3) == True):
        combinationsTreated.insert(0, 17)
        defend = 3
    elif(3 in cases_player and 9 in cases_player and 18 not in combinationsTreated and checkCaseEmpty(6) == True):
        combinationsTreated.insert(0, 18)
        defend = 6

    elif(1 in cases_player and 5 in cases_player and 19 not in combinationsTreated and checkCaseEmpty(9) == True):
        combinationsTreated.insert(0, 19)
        defend = 9
    elif(5 in cases_player and 9 in cases_player and 20 not in combinationsTreated and checkCaseEmpty(1) == True):
        combinationsTreated.insert(0, 20)
        defend = 1
    elif(1 in cases_player and 9 in cases_player and 21 not in combinationsTreated and checkCaseEmpty(5) == True):
        combinationsTreated.insert(0, 21)
        defend = 5

    elif(3 in cases_player and 5 in cases_player and 22 not in combinationsTreated and checkCaseEmpty(7) == True):
        combinationsTreated.insert(0, 22)
        defend = 7
    elif(5 in cases_player and 7 in cases_player and 23 not in combinationsTreated and checkCaseEmpty(3) == True):
        combinationsTreated.insert(0, 23)
        defend = 3
    elif(3 in cases_player and 7 in cases_player and 24 not in combinationsTreated and checkCaseEmpty(5) == True):
        combinationsTreated.insert(0, 24)
        defend = 5
        
    else:
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