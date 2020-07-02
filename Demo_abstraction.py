# Python: 3.8.2
# Author: Alex Moffat
# Purpose: Tech Academy Boot Camp - Abstraction Assignment
#===================================================================
Requirements = """
Create a class that utilizes the concept of abstraction.
1. Your class should contain at least one abstract method and one regular method.
2. Create a child class that defines the implementation of its parents abstract method.
3. Create an object that utilizes both the parent and child methods.
"""
contact = """
Alex Moffat \r
wamoffat4@gmail.com \r
(917) 674-4820"""
#=============================================================

#========== IMPORTED MODULES
from abc import ABC, abstractmethod

#=============================================================
#========== PARENT CLASS - Cart <-- Abstract
#=============================================================
class Cart(ABC):
    #========== INITIALIZE
    def __init__(self, items, subtotal, shipping, state):
        self.items = items
        self.subtotal = subtotal
        self.shipping = shipping
        self.state = state
        self.shipCost = 'calc' 
        #self.calcShip()
        #self.calcTax()
    #========== GET CART - display summary of shopping cart
    def getCart(self):
        multi = ""
        if (self.items > 1): multi = "s"
        txt = "You have {} item{} in your cart with a subtotal of ${} shipping {} to {} state.".format(self.items, multi, self.subtotal, self.shipping, self.state)
        if self.shipCost == 'calc':
            txt = txt + "\nShipping still needs to be calculated."
        elif self.shipCost == 0:
            txt =  txt + "\nShipping is FREE for this order!"
        return txt
    #========== CALC SHIP (abstraction) - input zipcode and weight to calculate shipping cost bacsed on shipping preference 
    @abstractmethod
    def calcShip(self, zipCode, weight):
        pass
    #========== CAL TAX (abstraction) - input zipcode to calculate state and local sales tax
    #@abstractmethod
    #def calcTax(self, zipCode):
        #pass

#========== CHILD CLASS - Discount <-- Cart - input code string to apply discount
#=============================================================
class Discount(Cart):
    #========== INITIALIZE
    def __init__(self, items, subtotal, shipping, state, code):
        super().__init__(items, subtotal, shipping, state)
        self.code = code
        self.calcShip()
    #========== CALC SHIP - checks if coupon code applies to shipping
    def calcShip(self):
        if self.code == 'SHIPFREE':
            self.shipCost = 0
            print("Coupon Code applied to cart")
        else:
            print("Coupon Code not valid for shipping")
        
#=============================================================
#========== DEMO - create abstract parent class, cerate child class, use methods
#=============================================================
def demo():
    #===== Create class objects
    user1 = Discount(4, 120.00, 'ground', 'WA', 'SHIPFREE')
    user2 = Discount(1, 50.50, '2-day', 'OR', '10%OFF')
    user3 = Discount(2, 500, '1-day', 'NY', '')
    #===== Call method - getCart() - not abstracted in parent
    print("User 1: ", user1.getCart())
    print("User 2: ",user2.getCart())
    print("User 3: ",user3.getCart())
    #===== ERROR - calling the abstract class with abstract method causes error
    try:
        user4 = Cart(2, 500, '1-day', 'NY')
    except Exception as e:
        print("ERROR: {}".format(e))
    
       
#============================================================= 
#========== MAIN
#=============================================================
if __name__ == '__main__':
    demo()
