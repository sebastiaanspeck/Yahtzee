from random import randint
import os

global score
score = [[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],['Drie dezelfde',0],
         ['Vier dezelfde',0],['Full House',0],['Kleine straat',0],
         ['Grote straat',0],['Yahtzee',0],['Kans',0],['Totale punten',0],['Totaal Deel 1',0],['Totaal Deel 2',0],['Totaal',0]]

def menu():
    keuze = ''
    global spelers
    spelers = 0
    correct = False
    while correct == False:
        if keuze.upper() != 'M':
            cls()
        print('Welkom bij Yahtzee \n- Menu Yatzee - \nSingleplayer  (S)\nMultiplayer   (M)\nQuit          (Q)')
        try:
            keuze = input('\nKies een optie (S, M, of Q): ')
            if keuze.upper() == 'S':
                cls()
                correct = True
                speelYatzee()
            elif keuze.upper() == 'M':
                cls()
                print('Multiplayer is under construction')
                correct = False
    ##            keuze == False
    ##            while keuze == False:
    ##                spelers = int(input('Met hoeveel spelers wil je spelen?: '))
    ##                if spelers > 1:
    ##                    keuze == True
    ##            speelYatzee()
            elif keuze.upper() == 'Q':
                quit()
        except(KeyboardInterrupt, ValueError):
            #cls()
            print('Je hebt een foute keuze gemaakt')

def speelYatzee():
    global dobbelstenen
    global beurten
    beurten = 1
    while beurten < 14:
        beurt = 1
        dobbelstenen = []
        bewaardeDobbelstenen = []
        while beurt < 4:
            cls()
            teller = 0
            for b in range(5-len(dobbelstenen)):
                dobbelsteen = randint(1,6)
                dobbelstenen.append(dobbelsteen)
            if beurt < 3:
                print('Beurt:', beurt)
                print('Gedobbelde dobbelstenen:')
                for c in range(len(dobbelstenen)):
                    if c == (len(dobbelstenen)-1):
                        print(dobbelstenen[c], end='')
                    else:
                        print(dobbelstenen[c], end=', ')
                for d in range(len(dobbelstenen)):
                    print('\n','Dobbelsteen met waarde: ',dobbelstenen[d], sep='')
                    keuze = False
                    while keuze == False:
                        try:
                            bewaren = input('Wilt u deze dobbelsteen bewaren? (J/N): ')
                            if bewaren.upper() == 'J':
                                teller += 1
                                keuze = True
                                print(dobbelstenen[d], 'wordt bewaard')
                                bewaardeDobbelstenen.append(dobbelstenen[d])
                                if teller == 5:
                                    beurt = 4
                            elif bewaren.upper() == 'N':
                                print(dobbelstenen[d],'wordt verwijderd')
                                keuze = True
                            else:
                                print('Je hebt een foute keuze gemaakt')
                        except(KeyboardInterrupt, ValueError):
                            print('Je hebt een foute keuze gemaakt')
                if len(bewaardeDobbelstenen) != 5:
                    dobbelstenen.clear()
                    for e in range(len(bewaardeDobbelstenen)):
                        dobbelstenen.append(bewaardeDobbelstenen[e])
                    bewaardeDobbelstenen.clear()
            beurt += 1
        cls()
        scoreInvullen()
        beurten += 1
    printScore()

def scoreInvullen():
    dobbelstenen.sort()
    correct = False
    while correct == False:
        print('Je uiteindelijke gegooide dobbelstenen:')
        for i in range(len(dobbelstenen)):
            if i == (len(dobbelstenen)-1):
                print(dobbelstenen[i], end='')
            else:
                print(dobbelstenen[i], end=', ')
        print('''\nKies waar je je score wilt invullen \n- Menu Score -
1.  Alle enen\n2.  Alle tweeën\n3.  Alle drieën\n4.  Alle vieren\n5.  Alle vijven
6.  Alle zessen\n\n7.  Drie dezelfde\n8.  Vier dezelfde\n9.  Full House\n10. Kleine straat
11. Grote straat\n12. Yahtzee\n13. Kans''')
        try:
            keuze = int(input('\nKies een optie (1 t/m 13): '))
            i = keuze-1
            if keuze < 7:
                if score[i][1] != 0:
                    cls()
                    correct = False
                    print('Je hebt deze al in gevuld, probeer een andere')
                elif score[i][0] not in dobbelstenen:
                    cls()
                    print('Je hebt geen',score[i][0],'gegooid')
                    keuzeJN = input('Wil je deze score leeglaten? (J/N): ')
                    if keuzeJN.upper() == 'J':
                        score[i][1] = 'x'
                    elif keuzeJN.upper() == 'N':
                        correct = False 
                else:
                    correct = True
                    aantal = dobbelstenen.count(keuze)
                    totaal = aantal * score[i][0]
                    score[i][1] = totaal
            if keuze >= 7:
                if score[i][1] != 0:
                    cls()
                    correct = False
                    print('Je hebt deze score al ingevuld, probeer een andere')
                else:
                    correct = True
                    if keuze == 7:
                        a = 1
                        while a < 7:
                            aantalA = dobbelstenen.count(a)
                            if aantalA == 3:
                                print(aantalA)
                                som = 0
                                for b in range(len(dobbelstenen)):
                                    som += dobbelstenen[b]
                                score[i][1] = som
                            a += 1
                        if score[i][1] == 0:
                            cls()
                            keuzeJN = input('Je hebt geen drie dezelfde, wil je deze score leeglaten? (J/N): ')
                            if keuzeJN.upper() == 'J':
                                score[i][1] = 'x'
                            elif keuzeJN.upper() == 'N':
                               correct = False 
                    elif keuze == 8:
                        a = 1
                        while a < 7:
                            aantalA = dobbelstenen.count(a)
                            if aantalA == 4:
                                som = 0
                                for b in range(len(dobbelstenen)):
                                    som += dobbelstenen[b]
                                score[i][1] = som
                            a += 1
                        if score[i][1] == 0:
                            cls()
                            keuzeJN = input('Je hebt geen vier dezelfde, wil je deze score leeglaten? (J/N): ')
                            if keuzeJN.upper() == 'J':
                                score[i][1] = 'x'
                            elif keuzeJN.upper() == 'N':
                                correct = False
                    elif keuze == 9:
                        a = 1
                        while a < 7:
                            aantalA = dobbelstenen.count(a)
                            if aantalA == 3:
                                b = 1
                                while b < 7:
                                    if b == a:
                                        b += 1
                                    aantalB = dobbelstenen.count(b)
                                    if aantalB == 2:
                                        score[i][1] = 25
                                        b = 6
                                    else:
                                        b += 1
                            a += 1
                        if score[i][1] == 0:
                            cls()
                            keuzeJN = input('Je hebt geen Full House, wil je deze score leeglaten? (J/N): ')
                            if keuzeJN.upper() == 'J':
                                score[i][1] = 'x'
                            elif keuzeJN.upper() == 'N':
                                correct = False
                    elif keuze == 10:
                        for b in range(3):
                            for c in range(6):
                                KleineStraat = [[1,2,3,4],[2,3,4,5],[3,4,5,6]]
                                KleineStraat[b].append(c+1)
                                KleineStraat[b].sort()
                                if KleineStraat[b] == dobbelstenen:
                                    score[i][1] = 30
                        if score[i][1] == 0:
                            cls()
                            keuzeJN = input('Je hebt geen kleine straat, wil je deze score leeglaten? (J/N): ')
                            if keuzeJN.upper() == 'J':
                                score[i][1] = 'x'
                            elif keuzeJN.upper() == 'N':
                                correct = False
                    elif keuze == 11:
                        if dobbelstenen == [1,2,3,4,5] or dobbelstenen == [2,3,4,5,6]:
                            score[i][1] = 40
                        if score[i][1] == 0:
                            cls()
                            keuzeJN = input('Je hebt geen grote straat, wil je deze score leeglaten? (J/N): ')
                            if keuzeJN.upper() == 'J':
                                score[i][1] = 'x'
                            elif keuzeJN.upper() == 'N':
                                correct = False
                    elif keuze == 12:
                        a = 1
                        while a < 6:
                            aantalA = dobbelstenen.count(a)
                            if aantalA == 5:
                                score[i][1] = 50
                            a += 1
                        if score[i][1] == 0:
                            cls()
                            keuzeJN = input('Je hebt geen Yathzee, wil je deze score leeglaten? (J/N): ')
                            if keuzeJN.upper() == 'J':
                                score[i][1] = 'x'
                            elif keuzeJN.upper() == 'N':
                                correct = False
                    elif keuze == 13:
                        som = 0
                        for a in range(len(dobbelstenen)):
                            som += dobbelstenen[a]
                        score[i][1] = som
        except(KeyboardInterrupt, ValueError):
            cls()
            print('Je hebt een foute keuze gemaakt')
    printScore()

def printScore():
    if beurten == 14:
        som = 0
        for b in range(6):
            som += score[b][1]
        score[13][1] = som
        if som >= 63:
            score[14][1] = som + 35
        else:
            score[14][1] = score[13][1]
        som = 0
        for c in range(6):
            if score[c+6][1] == 'x':
                c += 1
            som += score[c+6][1]
        score[15][1] = som
        score[16][1] = score[14][1] + score[15][1]
    print('\nJe score:\nDeel 1')
    for a in range(len(score)):
        if a < 6:
            print('Alle',score[a][0], '        |', score[a][1])
        elif a == 6:
            if beurten == 14:
                print(score[13][0], ' |', score[13][1])
            print('\nDeel 2')
            print(score[a][0], ' |', score[a][1])
        elif a == 7:
            print(score[a][0], ' |', score[a][1])
        elif a == 8:
            print(score[a][0], '    |', score[a][1])
        elif a == 9:
            print(score[a][0], ' |', score[a][1])
        elif a == 10:
            print(score[a][0], '  |', score[a][1])
        elif a == 11:
            print(score[a][0], '       |', score[a][1])
        elif a == 12:
            print(score[a][0], '          |', score[a][1])
    if beurten == 14:
            print('\n',score[14][0], '  | ', score[14][1],'\n',score[15][0],'  | ', score[15][1],'\n',score[16][0],'         | ', score[16][1], sep='')    
    input('Druk op Enter voor de volgende beurt')

        
def cls():
    os.system('cls')

global spelen
spelen = True    
while spelen == True:
    menu()
    

