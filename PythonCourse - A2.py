myDog = 'Albert'
myCat = 'Zuli'
print(myDog)
myPoem = ('To keep your marriage brimming '
    'With love in the loving cup, '
    'Whenever you’re wrong, admit it; '
    ' Whenever you’re right, shut up.')
print(myPoem)
print(len(myPoem))
subPoem = myPoem[slice(3,30)]
print(subPoem)
crazyString = ",,,,,rrttgg.....banana....rrr"
stripString = crazyString.strip(',.rtg')
print(stripString)
print(myDog.upper())
print(myCat.lower())
print('love' in myPoem)
print('love' not in myPoem)
print('hate' not in myPoem)
myPets = myDog + ' ' + myCat + ' are my pets.'
print(myPets)
sQuote = "\"To be or not to be, that is the question...\" - William Shakespeare"
print(sQuote)

print("\n===== ARITHMETIC OPERATORS =====")
num1 = 34
num2 = 11
print(num1 / num2)
print(num1 // num2)
print(num1 % num2)

print("\n===== ASSIGNMENT OPERATORS =====")
num3 = 6
num3 += num1
print(num3)
num3 **=2
print(num3)

print("\n===== LOGICAL OPERATORS =====")
print("should be true, false, true")
print(num1 < num2 | num1 < num3)
print(num1 < num2 & num1 < num3)
print(num1 < num2 ^ num1 < num3)
print("\n===== IDENTITY OPERATORS =====")
print("should be true, false, true")
print(num1 is not num2)
print(num1 is num2)
print(num1 is (num2 + 23))

print("\n===== MEMBERSHIP OPERATORS =====")
myList = ["apple", "banana", "pear", "strawberry"]
print("should be true, false")
print('cherry' not in myList)
print('cherry' in myList)

print("===== TUPLES =====")
myTuple = ("dog", "cat", "chicken", "frog", "snake")
animals = ('zebra', 'alligator', 'giraffe', 'goat', 'ox')
animalList = list(animals)
print('My Tuple has ' + str(len(myTuple)) + ' items and the value \"cat\" appears ' + str(myTuple.count('cat')) + ' time(s)')
print(animals)
print(animalList)
animalList.append('honey badger')
print(animalList)

print("\n===== LIST & SPLIT =====")
sList = list(sQuote)
print(sList)
qList = sQuote.split(" ")
print(qList)
print("\n===== ITERATE =====")
for i in myList:
    print(i)
for i in myTuple:
    print(i)
petList = []
for i in myTuple:
    petList.append(i)
petList.append("squirrels")
print(petList)
print(petList[5].capitalize() + ' are unintensional members of the Moffat Family Farm.')

print("\n===== COPY & CONCATENATE =====")
pets = petList.copy()
wildAnimals = animalList.copy()
animals = pets + wildAnimals
print(animals)

print("\n===== REVERSE =====")
animals.reverse()
print(animals)
for i in animals:
    print(i)

print("\n===== SETS & ADD & REMOVE & DIFFERENCE=====")
mySet = {'Albert', 'Zuli', 'Plurp', 'Peep', 'Nug', 'Supreme', 'Guchi', 'Barbus'}
mySet1 = mySet.copy()
print(mySet1)
mySet.remove('Barbus')
mySet.add('Batman')
print(mySet)
newItems = mySet1.difference(mySet)
print('Items in the first list that are not in the second:')
print(newItems)
print('Items in the second list that are not in the first:')
print(mySet.difference(mySet1))

print("\n========== DICTIONARIES ==========")
petDic = {'dog':'Albert', 'cat':'Zuli', 'snake':'Barbus', 'chicken':'Plurp','frog':'Cogswerth'}
print(petDic)
print(petDic.get('chicken'))
petDic['chicken']='Peep'
print(petDic['chicken'])
petDic['squirrel']='Merl'
print(petDic)

print("\n===== NESTED DICTIONARY =====")
farm = {
    'a1':{
        'type':'dog',
        'name':'Albert',
        'breed':'norwich terrier',
        'age': 144
        },
    'a2':{
        'type':'cat',
        'name':'Zuli',
        'breed':'balinese',
        'age': 9
        },
    'a3':{
        'type':'chicken',
        'name':'Plurp',
        'breed':'silver wyandotte',
        'age': 15
        },
    'a4':{
        'type':'chicken',
        'name':'Nug',
        'breed':'rhode island red',
        'age': 15
        },
    'a5':{
        'type':'snake',
        'name':'Barbus',
        'breed':'ball python',
        'age': 30
        }
    }
print(farm.keys())
print(farm.values())
for i in farm:
    print(farm[i]['name'])
aList = []
aNames = []
for x,y in farm.items():
    aList.append(x)
    aNames.append(y['name'])
print(aList)
print(aNames)
farmNames = dict.fromkeys(aNames)
print(farmNames)

print("\n===== LIST/ARRAY =====")
petNames = ['Albert', 'Zuli', 'Barbus', 'Cogswerth', 'Plurp', 'Peep', 'Nug', 'Pilar', 'Supreme', 'Guchi', 'Papiya', 'Batman']
print(petNames)

print("\n===== TYPE() =====")
print('The datatype from petNames :' + str(type(petNames)))
print('The datatype from farmNames :' + str(type(farmNames)))
print('The datatype from myTuple :' + str(type(myTuple)))
print('The datatype from stripString :' + str(type(stripString)))
print('The datatype from myDog :' + str(type(myDog)))
print('The datatype from num1 :' + str(type(num1)))

print("\n===== BOOLEAN CHALLENGE =====")
if  num1 > num2:
    print('num1 is greater than num2')
elif num2 > num1:
    print('num2 is greater than num1')
else:
    print('num1 is equal to num2')

if petNames[0] == farm['a1']['name']:
    print('Albert is the 1st pet on the farm')
else:
    print('Albert is not the 1st pet on the farm')

print("\n===== DATETIME =====")
import datetime
print(datetime.date.today())
print(datetime.datetime.now())

print("\n===== SYS MODULE =====")
import sys
#print(sys.copyright)
print(sys.executable)

#============================= I can comment code like this ========
# I can write anything after the hash and the rest of the line is ignored
#==============================================================
print("\n===== RANDOM MODULE =====")
import random
#===== Assignment  - random number from 1 to 100 
randomNum = random.randint(1,100)
randomDice = random.randint(1,6) + random.randint(1,6)
print('Random number from 1 to 100: ' + str(randomNum))
print('Random number from two 6-sided die: ' + str(randomDice))

#===== Extra Credit - five card stud
import Card_Games
players = 3
Card_Games.poker()
hands = 3

print("\n===== IF / ELIF / ELSE =====")
import Card_Games
Card_Games.war()

print("\n===== BOOL() function =====")
trueString = 'anything'
falseString = ''
trueInteger = 49
falseInteger = 0
trueArray = [1,2,3]
falseArray = []

print(bool(trueString))
print(bool(falseString))
print(bool(trueInteger))
print(bool(falseInteger))
print(bool(trueArray))
print(bool(falseArray))      

print("\n===== ISINSTANCE() function =====")

print(isinstance(5, int))
print(isinstance(5, str))
print(isinstance('Hello world!', (int,float,list,dict,tuple)))
print(isinstance('Hello world!', (int,float,list,dict,tuple,str)))

print("\n===== WHILE LOOP =====")
i = 0
hand = Card_Games.hand(52)
print(hand)
print(len(hand))
while i < len(hand):
    if hand[i] == 'Ace-S':
        print('It took you ' + str(i+1) + ' draws to pull an Ace of Spades. GAME OVER.')
        break
    elif hand[i][slice(0,4)] == 'King':
        print('On Draw ' + str(i+1) + ' you pulled a ' + hand[i])
        i += 1
        continue
    print('Draw ' + str(i+1))
    i +=1

print("\n===== FOR LOOP =====")
for num in range(10,-100,-1):
    if num == 0:
        print('BLAST OFF!')
        continue
    elif num < 4 and num > 0:
        print(num)
        continue    
    elif num < 0:
        if num == -60:
            print('Boosters detach at 1 minute')
            break
        else:
            continue
    print('T- ' + str(num))

print("\n===== ENUMERATE =====")
name = 'Python'
print(len(name))
eName = enumerate(name)
print(eName)
lName = list(eName)
print(lName)
print(len(lName))
for i in eName: #this will NOT work
    print(i)
for i in lName: #this will iterate through the list created
    print(i)
for i in enumerate(name): #this will iterate through enumerated object
    print(i)

print("\n===== ARRAY - COUNT() & SORT() =====")
petNames = ['Albert', 'Zuli', 'Barbus', 'Cogswerth', 'Plurp', 'Peep', 'Nug', 'Pilar', 'Supreme', 'Guchi', 'Papiya', 'Batman']
print('My Pets:')
#Loop through all the elements of an array using the for loop.
for p in petNames:
    print(p)
#Use the COUNT() method
import Card_Games
warDeck = Card_Games.warDeck()
print('There should be 4 of each card (1 in each suit) in a deck of cards:')
print('Number 2s = ' + str(warDeck.count(2)))
print('Number Jacks = ' + str(warDeck.count(11)))
#Use the SORT() method
deck = Card_Games.hand(52)
print(deck)
deck.sort()
print(deck)
#sort desending
deck.sort(reverse=True)
print(deck)
#sort a list of dictionaries based on value
lFarm = list(farm.values())
print(lFarm)
def sortOrder(k):
  return k['age']
lFarm.sort(key=sortOrder)
print(lFarm)

print("\n===== LAMBDA FUNCTION =====")     
import math
rTriHypo  = lambda a, b: round(math.sqrt(a**2 + b**2),3)
print(rTriHypo(3,5))

print("\n===== FORMAT() =====") 
txt1 = "My name is {fname}, I'am {age} and I have {pets} pets. My favorite pet is {fav}".format(pets=9, age = 49, fname = "Alex", fav='Albert')
txt2 = "I can count {} {} {} and I know my {} {} {}s."
print(txt1)
print(txt2.format(1,2,3,'A','B','C'))

yAge = 49
dAge = 49 * 365
mAge = 49 * 12
hAge = dAge * 24
print('I am {0} years old, which is {1} months, or {2:,} days. In binary, that is {2:b} days. In hexidecimal, that is {3:x} hours.'.format(yAge, mAge, dAge, hAge))

def getSum(num1, num2):
    answer = num1 + num2
    answer = 'The answer is {}.'.format(answer)
    return answer

mySum = getSum(2,4)
print(mySum)
