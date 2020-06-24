# Python: 3.8.2
# Author: Alex Moffat
# Purpose: Assignments in Tech Academy Boot Camp: Inheritance
# Tags: class, parent, child
#=============================================================
'''
Requirements:
Create two classes that inherit from another class.
Each child should have at least two of their own attributes.
'''

#===== PARENT CLASS - pet
class pet:
    def __init__ (self, iName, iAnimal, iBreed, iAge, iFeed):
        self.name = iName
        self.animal = iAnimal
        self.breed = iBreed
        self.age = iAge
        self.feed = iFeed

#===== CHILD CLASS - chicken <-- pet
class chicken(pet):
    production = False
    daily = 0
    roostPosition = 0

#===== CHILD CLASS - dog <-- pet
class dog(pet):
    tricks = []
    treat = "Greenies"
    bed = "Pillow"

#===== CHILD CLASS - cat <-- pet
class cat(pet):
    def __init__ (self, iName, iAnimal, iBreed, iAge, iFeed, iPlayTime, iNapTime):
        super().__init__(iName, iAnimal, iBreed, iAge, iFeed)
        self.playTime = iPlayTime
        self.napTime = iNapTime


#===== INSTANTIATE - pet objects
def createObjects():
    global petList
    ch1 = chicken('Plurp','Chicken', 'SIlver Wyndotte', 1.2, 'grain with oyster shell')
    ch2 = chicken('Nug','Chicken', 'Rhode Island Red', 1.2, 'grain with oyster shell')
    d1 = dog('Albert','Dog', 'Norwich Terrier', 12.6, 'ground lamb & grain free kibble')
    d2 = dog('Gretchen','Dog', 'Norwich Terrier', 2.5, 'ground lamb & grain free kibble')
    c1 = cat('Zuli','Cat', 'Balinese', 0.8, 'tuna & grain free kibble','11:00', '14:00')
    ch1.roostPosition = 3
    ch2.production, ch2.daily, ch2.roostPosition = True, 1.2, 1
    d1.tricks, d1.treat, d1.bed = ['rollover', 'dance', 'spin', 'stay', 'sit', 'come', 'shake'], 'Cheese', 'Sidecar'
    petList = [ch1, ch2, d1, d2, c1]

#===== PRINT - pet objects
def printObjects():
    pString = ""
    for p in petList:
        pString += '{name} is a {age} year old {breed} {animal} that eats {feed}.\n\t'.format(name = p.name, animal = p.animal, breed = p.breed, age = p.age, feed = p.feed) 
        if p.animal == 'Chicken':
            pString += '- {name} sleeps in roosting position {roost} and '.format(name = p.name, roost = p.roostPosition)
            if p.production:
                pString += 'currently lays {prod} eggs per day.\n'.format(prod = p.daily)
            else:
                pString += 'is currently not laying eggs.\n'
        elif p.animal =='Dog':
            pString += '- {name} will perform {trickCount} tricks for {treatName} and sleeps on a {bedName}.\n'.format(name = p.name, trickCount = len(p.tricks), treatName = p.treat, bedName = p.bed) 
        elif p.animal =='Cat':
            pString += '- {name} wants to play at {playTime} and nap at {napTime} each day.\n'.format(name = p.name, playTime = p.playTime, napTime = p.napTime)
    print(pString)

    
if __name__ == '__main__':
    createObjects()
    printObjects()
