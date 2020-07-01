# Python: 3.8.2
# Author: Alex Moffat
# Purpose: Playing card management. Used to create a deck of cards for playing card games.
#============================================================================
description = """
MODULE cards.py: \r
Create a standard deck of playing cards when initializing a class object. Standard deck can be
altered by altering the protected attributes and calling the makeDeck() method. The private
.__deck attribute is a list and each card in the deck is a dictionary containing face, suit, cName
fValue, sValue, and tValue properties. \n
Methods: \r
makeDeck() creates a deck using available cards defined by protected attributes \r
shuffleDeck() shuffles the deck \r
showDeck() returns the .__deck list of card dictionaries \r
dealCards(self, *args) takes options of 'pop'/'random' and number of cards - returns single card
dictionary or list of cards. 
"""
requirements = """
Create a class that uses encapsulation.
1. This class should make use of a private attribute or function.
2. This class should make use of a protected attribute or function.
3. Create an object that makes use of protected and private.
"""
tags = """
random, shuffle, sample, init, class, private, protected, self, args handling, dictionaries, lists
pop, split, append, isinstance, lower, continue, range
"""
contact = """
Alex Moffat \r
wamoffat4@gmail.com \r
(917) 674-4820
"""
#============================================================================

#========== IMPORTED MODULES
import random

#========================================================
#========== CLASS - Card_Deck - private and protected attributes
#========================================================
class Card_Deck:
    #========== INITIALIZE
    def __init__(self):
        self._cards = 'Two Three Four Five Six Seven Eight Nine Ten Jack Queen King Ace'.split()
        self._suits = 'Clubs Diamonds Hearts Spades'.split()
        self._faceValues = [2,3,4,5,6,7,8,9,10,11,12,13,14]
        self._suitValues = [0.1,0.2,0.3,0.4]
        self._count = 0
        self.__deck = []
        self.makeDeck()        
    #========== MAKE DECK - use cards from protected variables above
    def makeDeck(self):
        i = 0
        for c in self._cards:
            j = 0
            for s in self._suits:
                newCard = {}
                newCard['face'] = c
                newCard['suit'] = s
                newCard['cName'] = '{}-of-{}'.format(c, s)
                newCard['fValue'] = self._faceValues[i]
                newCard['sValue'] = self._suitValues[j]
                newCard['tValue'] = self._faceValues[i] + self._suitValues[j]
                j += 1
                self.__deck.append(newCard)
            i += 1            
        self._count = len(self.__deck)
    #========== SUFFLE DECK - random order the cards in private variable '__deck' 
    def suffleDeck(self):
        random.shuffle(self.__deck)
    #========== SHOW DECK - returns list of dictionaries 
    def showDeck(self):
        return self.__deck
    #========== DEAL CARDS - deals one card - option 'pop'(default) or 'random' - option number of cards (default 1)
    def dealCards(self, *args):
        if len(self.__deck) == 0: return False # empty deal return
        num = 1
        draw = 'pop'
        #===== Options: 'pop' or 'random' / number of cards 
        for i in args:
            if isinstance(i, int):
                if len(self.__deck) < i: return False # not enough cards for draw return
                num = i
            if isinstance(i, str):
                if i.lower() == 'pop' or i.lower() == 'random': draw = i.lower()
        #===== Deal Card(s) - returns a single card dictionary or list of card dictionaries
        if draw == 'random': #=== 'random' card from deck
            theReturn = random.sample(self.__deck,num)
            for r in range(len(theReturn)):
                for c in range(len(self.__deck)):
                    if self.__deck[c]['tValue'] == theReturn[r]['tValue']:
                        self.__deck.pop(c)
                        break            
        else: #=== 'pop' top card(s) from deck
            theReturn = []
            for i in range(num):
                theReturn.append(self.__deck.pop(0))
        #===== Return - 1 returns single dictionary, anything greater than 1 returns list of dictionaries
        self._count = len(self.__deck)
        if num == 1: return theReturn[0]
        return theReturn
            
#========================================================    
#========== MAIN
#========================================================
if __name__ == '__main__':
    print(description)
    print(contact)
