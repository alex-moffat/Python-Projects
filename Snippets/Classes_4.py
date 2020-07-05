# Python: 3.8.2
# Author: Alex Moffat
# Purpose: Assignments in Tech Academy Boot Camp: POLYMORPHISM
# Tags: class, parent, child, class method, polymorphism 
#=============================================================
'''
Requirements:
    Create two classes that inherit from another class.
        1. Each child should have at least two of their own attributes.
        2. The parent class should have at least one method (function).
        3. Both child classes should utilize polymorphism on the parent class method.
'''

#===== PARENT CLASS - Car
class Car:
    def __init__ (self, iModel, iMake, iBody, iYear, iDoors):
        self.model = iModel
        self.make = iMake
        self.body = iBody
        self.year = iYear
        self.doors = iDoors
    engine = 'unknown'
    slogan = 'Buy this car because you like the way it looks and feels when you drive it!'
    #===== METHODS
    def info(self):
        msg = "The {} {} {} is a {} with {} doors.".format(self.year, self.make, self.model, self.body, self.doors)
        msg += "\n" + self.slogan 
        return msg

#===== CHILD CLASS - EV <-- Car
class EV(Car):
    def __init__ (self, iModel, iMake, iBody, iYear, iDoors, iCapacity, iRange, iSpeed):
        super().__init__(iModel, iMake, iBody, iYear, iDoors)
        self.capacity = iCapacity
        self.range = iRange
        self.speed = iSpeed
    engine = 'electric'
    slogan = 'Buy this car because you want to save the planet for you and your children!'
    #===== METHODS
    def info(self):
        msg = "The {} {} {} is a {} with {} doors.".format(self.year, self.make, self.model, self.body, self.doors)
        msg += "\nThe {0} has a {1} kWh capacity battery that provides {2} miles of range and goes 0 to 60 in {3} seconds".format(self.model, self.capacity, self.range, self.speed)
        msg += "\n" + self.slogan 
        return msg

#===== CHILD CLASS - IC <-- Car
class IC(Car):
    def __init__ (self, iModel, iMake, iBody, iYear, iDoors, iMPG):
        super().__init__(iModel, iMake, iBody, iYear, iDoors)
        self.mpg = iMPG
    engine = 'internal combustion'
    slogan = "Buy this car because you don't care about the health of you, the planet or your children!"
    #===== METHODS
    def info(self):
        carbon100 = int(100 * (19.64 / self.mpg)) #CO2 per 100 miles travelled
        carbonYear = int(carbon100 * 120) #CO2 per 12,000 miles travelled
        msg = "The {} {} {} is a {} with {} doors.".format(self.year, self.make, self.model, self.body, self.doors)
        msg += "\nThe {0} gets {1} miles per gallon, meaning it will produce {2} pounds of CO2 per 100 miles travelled or {3:,} pounds each year you average 12,000 miles.".format(self.model, self.mpg, carbon100, carbonYear)
        msg += "\n" + self.slogan 
        return msg
            
#===== INSTANTIATE - Car objects
def createObjects():
    global carList
    e1 = EV('Model S', 'Tesla', 'sedan', 2020, 4, 100, 402, 2.3)
    e2 = EV('Model 3', 'Tesla', 'sedan', 2020, 4, 75, 310, 3.2)
    e3 = EV('Coupe', 'Tesla', 'sports car', 2008, 2, 53, 244, 3.7)
    e4 = EV('Leaf', 'Nissan', 'hatchback', 2019, 4, 62, 226, 6.5)
    g1 = IC('Camery', 'Toyota', 'sedan', 2020, 4, 29)
    g2 = IC('Camery Hybrid', 'Toyota', 'sedan', 2020, 4, 51)
    g3 = IC('Explorer', 'Ford', 'SUV', 2018, 4, 19)
    g4 = IC('Ram 1500', 'Dodge', 'pickup truck', 2020, 4, 22)
    g5 = IC('Suburban', 'Chevy', 'SUV', 2020, 4, 15)
    carList = [e1, e2, e3, e4, g1, g2, g3, g4, g5]

#===== PRINT - Car objects
def printObjects():
   print("Car objects:")
   for c in carList:
      print(c.info() + '\n')

#===== MAIN - script to run   
if __name__ == '__main__':
    createObjects()
    printObjects()
