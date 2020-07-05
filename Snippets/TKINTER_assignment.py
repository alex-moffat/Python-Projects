# PYTHON: 3.8.2
# AUTHOR: Alex Moffat
# PURPOSE: The Tech Academy Bootcamp - TKINTER ASSIGNMENT
#=============================================================================
"""
TAGS:
Tkinter, Tk(), master, Frame, grid, row, column, label, entry, button,
iconbitmap, title, resizeable, config, padx, pady, sticky, WM_DELETE_WINDOW,
columnspan, font, fg, bg, format, mainloop, destroy, lambda, configure, get, cget,
textvariable
"""
# ============================================================================

#===== IMPORTED MODULES
import tkinter
from tkinter import *

#=============================================================
#========== FUNCTIONS
#=============================================================

#===== PRINT TEXT - prints text inside button
def but2():
    print("Button 'Two' was pressed. This function can't take parameters.")

#===== PRINT TEXT - prints text inside button
def printText(var):
    pString = "Button {} was pressed. This function can take parameters."    
    if isinstance(var,str): #STRING INPUT
        print(pString.format(var))
    else: #OBJECT INPUT
        print(pString.format(var.cget('text'))) #gets info from widget object with '.cget()'
    
#===== CHANGE TEXT - prints text inside button
def changeText(obj):
    if obj.get() != "":
        print("This script will change the text in variable 'v1' from {} to something else".format(obj.get()))
        obj.set('Ha Ha try again!')
    obj = "Does this work?" # setting variables in Tkinter don't work like this
    


#=============================================================
#========== ASSIGNMENT
#=============================================================

#===== CREATE tkinter window with pack
win = Tk()
b1 = Button(win, text = "One", command=lambda txt="One": printText(txt))
b1.pack(side=LEFT, padx = 10)
b2 = Button(win, text = "Two", command=lambda txt="Two": printText(txt))
b2.pack(side=LEFT, padx = 10)
b3 = Button(win, text = "Three", command=lambda txt="Three": printText(txt))
b3.pack(side=RIGHT, padx = 10)
b4 = Button(win, text = "Four", command=lambda txt="Four": printText(txt))
b4.pack(side=BOTTOM, padx = 10)
b5 = Button(win, text = "Five", command=lambda txt="Five": printText(txt))
b5.pack(padx = 10)
b6 = Button(win, text = "Six", command=lambda txt="Six": printText(txt))
b6.pack(side=BOTTOM, padx = 10)
b7 = Button(win, text = "Seven", command=lambda txt="Seven": printText(txt))
b7.pack(side=LEFT, padx = 10)
win.destroy()

#===== CREATE tkinter window with grid
win = Tk()
#=== buttons
b1 = Button(win, text = "One", command=lambda txt="One": printText(txt))
b1.grid(row=0, column=0)
b2 = Button(win, text = "Two", command=lambda txt="Two": printText(txt))
b2.grid(row=1, column=1)
#=== labels
l1 = Label(win, text="This is label 1")
l1.grid(row=0, column = 1)
l2 = Label(win, text="This is label 2")
l2.grid(row=1, column = 0)
win.destroy()

#===== CREATE tkinter window with pack
win = Tk()
# win.geometry('{}x{}+{}+{}'.format(win.winfo_reqwidth(), win.winfo_reqheight(), 300, 300))
f = Frame(win)
b1 = Button(f, text = "One", command=lambda txt="Uno": printText(txt))
b2 = Button(f, text = "Two", command=lambda txt="Two": printText(txt))
b3 = Button(f, text = "Three", command=lambda txt="Three": printText(txt))
b4 = Button(f, text = "Input")
b1.pack(side=LEFT, padx=10, pady=10)
b2.pack(side=LEFT, padx=10)
b3.pack(side=LEFT, padx=10)
b4.pack(side=LEFT, padx=10)
l1 = Label(win, text="This label is over all buttons") # notice this is packed to the win not Frame
l1.pack(pady=20)
f.pack() # frame is packed second

#===== CONFIGURE - Any keyword argument that we can pass when creating a widget may also be passed to its "configure" method.
b1.configure(bg="salmon", command=lambda obj=b1: printText(obj)) # can reference itself (object) when using configure (after originally instantiated)
b2.configure(bg="mediumpurple", command=but2)

#===== ENTRY
v1 = StringVar() # Tkinter keyword for string variable
e1 = Entry(win, textvariable = v1, bg="darkgrey", fg="white") #Tkinter keyword to assign a StringVar to the entry value entered by user
e1.pack(pady=10)
print("variable v1 is {}".format(v1)) # object reference
print("variable e1 is {}".format(e1)) # object reference
b4.configure(bg="darkgrey", fg='white', command=lambda obj=v1: changeText(obj))

#===== LISTBOX - Creates a menu of items to choose from where the "height" parameter limits how many lines will show
items = StringVar()
items.set("Albert Zuli Barbus Peep Plurp") # can add items to listbox with a variable 
lBox = Listbox(win, listvariable=items, selectmode=MULTIPLE, height=4) # assign variable to populate when instantiating, selectmode is default SINGLE
lBox.pack(side=LEFT, pady=10)
lBox.insert(END, "first insert") #places item at the end of the list wth "END" - Note at this point in the code this is the first item then others get added after
lBox.insert(END, "second insert")
lBox.insert(END, "third insert")
lBox.insert(0, "forth insert, first item") # places item at the beginning of list with "0"
#=== Scrollbar - A listbox may be used in conjunction with a scroll bar
sBar = Scrollbar(win, orient=VERTICAL, command= lBox.yview)
sBar.pack(side=LEFT, pady=10, fill=Y)
#=== crosslink scrollbar to listbox
#sBar.configure(command= lBox.yview) - can crosslink with configure or like above when Scrollbar is instantiated
lBox.configure(yscrollcommand=sBar.set)

   

#=============================================================
#========== MAIN
#=============================================================
if __name__ == '__main__':
    pass
