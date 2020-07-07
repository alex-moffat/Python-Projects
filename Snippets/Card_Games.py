# Python: 3.8.2
# Author: Alex Moffat
# Purpose: Some card games that show off basic programming skills
#======== War (2 Player),  5 card stud poker (2 - 10 players)

import random

#========== DECK/HAND ================
#=====================================
def hand(handSize):
   #== Create & shuffle deck 
   deck = []
   cards = 'Ace Two Three Four Five Six Seven Eight Nine Ten Jack Queen King'.split()
   suits = '-D -H -S -C'.split()
   for c in cards:
       for s in suits:
           deck.append(c+s)
   random.shuffle(deck)
   return(random.sample(deck,handSize))

#========== WARDECK =================
#=====================================
def warDeck():
    wDeck = []
    #== Create & shuffle deck
    cards = [2,3,4,5,6,7,8,9,10,11,12,13,14]
    for x in range(4):
        wDeck = wDeck + cards
    random.shuffle(wDeck)
    return wDeck


#========== POKER ====================
#=====================================
def poker():
   print("\n========== POKER ==========")
   hands = players()
   handList = []
   #== Create & shuffle deck 
   deck = hand(52)    
   #== Deal hands
   print('Deal ' + str(hands) + ' hands')
   deltHands = random.sample(deck,(5 * hands))
   for x in range(hands):
       h = random.sample(deltHands,5)
       deltSet = set(deltHands)
       s = set(h)
       handList.append(s)
       remainingSet = deltSet.difference(s)
       deltHands = list(remainingSet)
       print('Player ' + str(x+1) + ' has: ' + str(s))
    #== handsList contains all the player hands for additional processing
    #print(handList) 

#========== WAR ====================
#===================================
def war():
    print("\n========== WAR ==========")
    p1 = []
    p2 = []
    p1Score = 0
    p2Score = 0
    #== Create & shuffle deck
    wDeck = warDeck()
    #== Deal hands
    for d in range(52):
        if d % 2 != 0:
            p1.append(wDeck[d])
        else:
            p2.append(wDeck[d])
    #== Play hands
    stake = 0
    for w in range(26):
        stake += 2
        draw = [p1[w], p2[w]]
        cDraw = []
        for c in range(2):
            if draw[c] <=10:
                cDraw.append(str(draw[c]))
            else:
                if draw[c] == 11:
                    cDraw.append( 'Jack')
                elif draw[c] == 12:
                    cDraw.append( 'Queen')
                elif draw[c] == 13:
                    cDraw.append( 'King')
                else:
                    cDraw.append( 'Ace')
        if p1[w] == p2[w]:
            result = 'Tie - each player had ' + cDraw[0]
        elif p1[w] > p2[w]:
            result = 'Player One ' + cDraw[0] + ' beats Player Two ' + cDraw[1]
            p1Score += stake
            stake = 0
        else:
            result = 'Player Two ' + cDraw[1] + ' beats Player One ' + cDraw[0]
            p2Score += stake
            stake = 0
        print('Round ' + str(w+1) + ': ' + result)
    print('FINAL SCORE: \n Player 1 = ' + str(p1Score) + '\n Player 2 = ' + str(p2Score))
    if p1Score == p2Score:
        print('TIE GAME!')
    elif p1Score > p2Score:
        print('PLAYER 1 WINS!')
    else:
        print('PLAYER 2 WINS!')

#========== PLAYERS =================
#===================================
def players():
    go = True
    i = 0   
    while go:
        pNum = input('How many players? ')
        if pNum == '':
            print('You need to provide the number of players')
        else:
            try:
               if int(pNum) <= 10 and int(pNum) > 1:
                  go = False
                  return int(pNum)
               else:
                  print('There can only be 2 - 10 players')                  
            except ValueError as e:
               print('Please enter an integer between 2 and 10')
               print("Error: {}".format(e))                
            finally:
               i += 1
               if i == 1:
                  print('You have tried 1 times to input a valid integer')
               else:
                  print('You have tried {} times to input a valid integer'.format(i))
 
def playerNames():
    go = True
    while go:
        iName = input('What is your name? ')
        if iName == '':
            print('You need to provide a name!')
        else:
            go = False
       



if __name__ == "__main__":
    pass
