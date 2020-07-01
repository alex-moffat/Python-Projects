# Python: 3.8.2
# Author: Alex Moffat
# Purpose: Tech Academy Boot Camp - Encapsulation assignment
#===================================================================
Requirements = """
Create a class that uses encapsulation.
1. This class should make use of a private attribute or function.
2. This class should make use of a protected attribute or function.
3. Create an object that makes use of protected and private.
"""
contact = """
Alex Moffat\n
wamoffat4@gmail.com\n
(917) 674-4820"""
#=============================================================

#========== IMPORTED MODULES
import cards


#========== DEMO - Create class with protected and private attributes
def demo():
    #===== Create class objects
    deck1 = cards.Card_Deck()
    deck2 = cards.Card_Deck()
    print("Deck1 created with {} cards.".format(deck1._count))
    print("Deck2 created with {} cards.".format(deck2._count))
    #===== Call methods - showDeck() & suffleDeck() 
    print("Card Names:")
    for c in deck1.showDeck():
        print(c['cName'])
    print("========== Shuffle decks ==========")
    deck1.suffleDeck()
    deck2.suffleDeck()
    print("Deck 1 First Card:")
    print(deck1.showDeck()[0])
    print("Deck 2 First Card:")
    print(deck2.showDeck()[0])
    #===== Call method - dealCards()
    print("========== Deal 2 hands of 5 cards ==========")
    print("Using Deck 1 to alternate deal cards from top of deck.")
    player1 = []
    player2 = []
    for i in range(5):
        player1.append(deck1.dealCards('pop',1))
        player2.append(deck1.dealCards('pop',1))
    print("Deck 1 has {} cards remaining.".format(deck1._count))
    print("\nPlayer 1 hand:")
    for c in player1:
        print(c['cName'])
    print("\nPlayer 2 hand:")
    for c in player2:
        print(c['cName'])
    print("========== Deal 1 hand of 5 cards ==========")
    print("Using Deck 2 to pull 5 random cards anywhere in the deck.")
    player3 = deck2.dealCards('random',5)
    print("Deck 2 has {} cards remaining.".format(deck2._count))
    print("\nPlayer 3 hand:")
    for c in player3:
        print(c['cName'])
    print("========== Deal 1 more hand of 5 cards ==========")
    print("Using Deck 2 to pull 5 cards from top of the deck.")
    player4 = deck2.dealCards(5)
    print("Deck 2 has {} cards remaining.".format(deck2._count))
    print("\nPlayer 4 hand:")
    for c in player4:
        print(c['cName'])
    
       
#========================================================    
#========== MAIN
#========================================================
if __name__ == '__main__':
    demo()
