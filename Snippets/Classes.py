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

class pet:
    name = ""
    animal = ""
    breed = ""
    age = 0.0
    feed = ""

class chicken(pet):
    production = False
    daily = 0
    roostPosition = 0

class dog(pet):
    tricks = []
    treat = ""
    bed = ""
    
