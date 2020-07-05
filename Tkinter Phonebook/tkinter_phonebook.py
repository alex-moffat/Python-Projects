# Python: 3.8.2
# Author: Alex Moffat
# Purpose: Tkinter Demo Phonebook. Demonstrating OOP, Tkinter GUI module using Tkinter Parent and Child relationships. 
#=============================================================
"""TAGS:
tkinter, Tk(), master, Frame, grid, row, column, label, entry, button,
iconbitmap, title, resizeable, config, padx, pady, sticky, WM_DELETE_WINDOW
columnspan, font, fg, bg, format, mainloop, destroy, SQL, sqlite3.version
error handling, connect, cursor, execute, CREATE, INSERT, SELECT,
slice, upper, fetchall, lambda, command, Listbox, Scrollbar, bind, set,
ListboxSelect, yview, yscrollcommand, exportselection, winfo_screenwidth,
winfo_screenheight, messgaebox, event, widget, withdraw, clipboard_clear,
clipboard_append, clipboard_get, update, open, write, read, close
"""
#=============================================================
description = """
This program was written by Alex Moffat.\n
This is a demonstration of OOP using the Python Tkinter GUI module with parent and child relationships.\n
This app uses a custom module 'SQL_functions.py' that wraps the SQLite3 module with error handling and reporting."""

use = """
This demo creates and populates a database on first start. You can ADD, UPDATE or DELETE users.\n
ADD: Fill in first name, last name, 10 digit phone number, and email address, then press 'Add'. Entries with the same first and last name are not permitted.\n
UPDATE: Select an entry from the list box and edit the phone number and/or email address in the entry fields, then press 'Update'. Name changes are not permitted.\n
DELETE: Select an entry from the list box, then press 'Delete'.\n
COPY & EXPORT: From the 'File' menu, copy individual selected records to the clipboard or export the entire database to a .txt file."""

contact = """
Alex Moffat\n
wamoffat4@gmail.com\n
(917) 674-4820"""
#=============================================================

#========== IMPORTED MODULES
import os
import tkinter as tk
from tkinter import * # this is required to make all widgets in tkinter available
from tkinter import messagebox
import SQL_functions

#========== VARIABLES
w = 500 # App Window width
h = 330 # App Window height
DB = 'demo_phonebook.db' # demo phonebook database
phoneInsert = 'INSERT INTO phonebook (fName, lName, phone, email) VALUES (?, ?, ?, ?)' # standard SQL INSERT statement
phoneSelect = "SELECT fName, lName, phone, email FROM phonebook WHERE phoneID = '{}'" # standard SQL SELECT statement 
selectRecordCount = 'SELECT COUNT(phoneID) FROM phonebook' # count db records

#=============================================================
#========== TKINTER PARENT WINDOW
#=============================================================
class ParentWindow(Frame):
    def __init__ (self, master, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        #===== master window
        self.master = master
        M = self.master # Assign self.master to single digit variable "M" for cleaner code        
        #===== protocol - built-in tkinter method to catch user click the corner "X" on Windows OS, calls function in '_func' module
        M.protocol("WM_DELETE_WINDOW", lambda: askQuit(self))
        
        #========== MENU ==========
        #===== title bar
        M.iconbitmap('phonebook_icon.ico')
        M.title('Tkinter Phonebook Demo')
        #===== dropdown menus - Instantiate the Tkinter menu dropdown object - this menu will appear at the top of our window
        menubar = Menu(M)
        #=== file menu
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Copy", underline=1,command=lambda: onCopy(self))
        filemenu.add_command(label="Export", underline=1,command=lambda: onExport(self))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", underline=1,command=lambda: askQuit(self))
        menubar.add_cascade(label="File", underline=0, menu=filemenu)
        #=== help menu
        helpmenu = Menu(menubar, tearoff=0) # defines the particular drop down colum and tearoff=0 means do not separate from menubar
        helpmenu.add_command(label="How to use this program", command=lambda: helpMenu('use'))
        helpmenu.add_command(label="About Phonebook Demo", command=lambda: helpMenu('about')) # add_command is a child menubar item of the add_cascade parent item
        helpmenu.add_separator()
        helpmenu.add_command(label="Contact Author", command=lambda: helpMenu('contact')) # add_command is a child menubar item of the add_cascade parent item
        menubar.add_cascade(label="Help", menu=helpmenu) # add_cascade is a parent menubar item (visible heading)
        M.config(menu=menubar, borderwidth='1')        

        #========== WINDOW ==========
        #===== color
        M.config(bg='#F0F8FF')
        #===== size & position
        M.resizable(width=False, height=False)
        x = int((M.winfo_screenwidth()/2) - (w/2)) # calling built-in tkinter function to get display width
        y = int((M.winfo_screenheight()/2) - (h/2)) # calling built-in tkinter function to get display height
        M.geometry('{}x{}+{}+{}'.format(w, h, x, y))
        
        #========== GUI ==========
        #===== labels
        Label(M, text='First Name ', bg='#F0F8FF').grid(row=0, column=0, padx=(27,0), pady=(10,0), sticky=N+W)
        Label(M, text='Last Name ', bg='#F0F8FF').grid(row=2, column=0, padx=(27,0), pady=(10,0), sticky=N+W)
        Label(M, text='Phone Number ', bg='#F0F8FF').grid(row=4, column=0, padx=(27,0), pady=(10,0), sticky=N+W)
        Label(M, text='Email Address ', bg='#F0F8FF').grid(row=6, column=0, padx=(27,0), pady=(10,0), sticky=N+W)
        Label(M, text='Database: ', bg='#F0F8FF').grid(row=0, column=2, padx=(0,0), pady=(10,0), sticky=N+W)
        #===== entries
        self.E_fName = Entry(M, text='First') # VAR E_fName 
        self.E_fName.grid(row=1, column=0, rowspan=1, columnspan=2, padx=(30,40), pady=(0,0), sticky=N+E+W)
        self.E_lName = Entry(M, text='Last') # VAR E_lName
        self.E_lName.grid(row=3, column=0, rowspan=1, columnspan=2, padx=(30,40), pady=(0,0), sticky=N+E+W)
        self.E_phone = Entry(M, text='Phone') # VAR E_phone
        self.E_phone.grid(row=5, column=0, rowspan=1, columnspan=2, padx=(30,40), pady=(0,0), sticky=N+E+W)
        self.E_email = Entry(M, text='Email') # VAR E_email
        self.E_email.grid(row=7, column=0, rowspan=1, columnspan=2, padx=(30,40), pady=(0,0), sticky=N+E+W)
        #===== scrollbar & listbox
        self.phoneIDs = [] # stores unique phoneID for each person in the list
        self.sBar = Scrollbar(M, orient=VERTICAL) # VAR sBar
        self.sBar.grid(row=1, column=5, rowspan=7, columnspan=1, padx=(0,0), pady=(0,0), sticky=N+S+E)
        self.lBox = Listbox(M, exportselection=0, yscrollcommand=self.sBar.set) # VAR lBox
        self.lBox.grid(row=1, column=2, rowspan=7, columnspan=3, padx=(0,0), pady=(0,0), sticky=N+S+E+W)
        #===== cross-reference: scrollbar & listbox
        self.sBar.config(command=self.lBox.yview) 
        self.lBox.bind('<<ListboxSelect>>', lambda event: onSelect(self,event)) # the "event' object is passed to this function with the class object "self"
        #===== buttons
        self.B_add =  Button(M, width=12, height=2, text='Add', bg='#A8D7FF', command= lambda: onAdd(self))
        self.B_add.grid(row=8, column=0, padx=(25,0), pady=(45,10), sticky=W)
        self.B_update = Button(M, width=12, height=2, text='Update', bg='#A8D7FF', command= lambda: onUpdate(self))
        self.B_update.grid(row=8, column=1, padx=(15,0), pady=(45,10), sticky=W)
        self.B_delete = Button(M, width=12, height=2, text='Delete', bg='#A8D7FF', command= lambda: onDelete(self))
        self.B_delete.grid(row=8, column=2, padx=(15,0), pady=(45,10), sticky=W)
        self.B_close = Button(M, width=12, height=2, text='Close', bg='#A8D7FF', command= lambda: askQuit(self))
        self.B_close.grid(row=8, column=4, padx=(15,0), pady=(45,10), sticky=E)
        #===== functions
        createDB()
        onRefresh(self)        

#=============================================================
#========== TKINTER FUNCTIONS
#=============================================================

#========== ON COPY - copy a selected database person to the clipboard
def onCopy(self):
    if not checkSelect(self): return # Determine if a selection from listbox is made
    index = self.lBox.curselection()[0] # Returns the line number of variable lBox (tkinter listbox) - used [0] to get first item from curselection() tuple return
    dataSet = SQL_functions.sqlExecute(DB, phoneSelect.format(self.phoneIDs[index]))
    info = "{}, {}, {}, {}".format(dataSet[0][0], dataSet[0][1], dataSet[0][2], dataSet[0][3])
    r = Tk()
    r.withdraw() # keep window from popping up
    r.clipboard_clear()
    r.clipboard_append(info)
    r.update()
    print("{} copied to clipboard".format(r.clipboard_get()))

#========== ON EXPORT - export entire database to a .txt using the os module
def onExport(self):
    fileName = 'phonebook_data.txt'
    filePath = os.getcwd()
    abPath = os.path.join(filePath, fileName)
    dataSet = SQL_functions.sqlExecute(DB, "SELECT lName, fName, phone, email FROM phonebook ORDER BY lName, fName")
    f = open(fileName, 'w') # w = overwrite
    f.write('Last Name\tFirst Name\tPhone Number\tEmail Address\r')
    f.close()
    f = open(fileName, 'a') # a = append what exists
    records = 0
    for d in dataSet:
        records += 1
        f.write('{}\t{}\t{}\t{}\r'.format(d[0], d[1], d[2], d[3]))
    f.close()    
    messagebox.showinfo("EXPORT COMPLETE", '{} records saved to {}'.format(records, abPath))
    
#========== ASK QUIT - make sure user wants to exit App - use tkinter method messagebox
def askQuit(self):
    if messagebox.askokcancel("Exit Program", "Are you sure you want to exit the program?"): # returns True if user selects "OK"
        self.master.destroy()
        os._exit(0) # prevents memory leaks by purging variables and widgets associated with the application

#========== HELP MENU - tell about this program
def helpMenu(m):
    if m == 'use':
        messagebox.showinfo("How to use Phonebook Demo", use)
    elif m == 'about':
        messagebox.showinfo("About Phonebook Demo", description)
    elif m == 'contact':
        messagebox.showinfo("Contact Developer", contact)

#========== CHECK FORMAT - make sure all data is formatted correctly
def checkFormat(fName, lName, phone, email):
    msg = ""
    if len(fName) == 0 or len(lName) == 0 or len(phone) == 0 or len(email) == 0: #===== all fields are filled out
        msg = "Make sure you have filled out all four fields"
    elif not "@" or not "." in email: #===== email format
        msg = "Incorrect email format"
    elif len(phone) != 10: #===== phone 10 digits
        msg = "Phone number must have exactly 10 digits"
    else: #===== phone numbers only
        try: 
            int(phone)
        except ValueError:
            msg = "Phone number must contain numbers only"
    return msg

#========== ON CLEAR - clear all Entry widgets
def onClear(self):
    self.E_fName.delete(0, END) # deletes data (text) from the beginning (Position 0) of text box to the end
    self.E_lName.delete(0, END)
    self.E_phone.delete(0, END)
    self.E_email.delete(0, END)    

#=============================================================
#========== SQL related
#=============================================================

#========== CREATE DB - create database and table
def createDB():
    #===== Create database
    SQL_functions.dbConnect(DB)
    #===== Create table
    sCreateTable = "CREATE TABLE IF NOT EXISTS phonebook(\
        phoneID INTEGER PRIMARY KEY AUTOINCREMENT,\
        fName VARCHAR(30),\
        lName VARCHAR(30),\
        phone VARCHAR(10),\
        email VARCHAR(255))"
    SQL_functions.sqlExecute(DB, sCreateTable)
    #===== populate DB - check if first time through, if so add an entry
    dbCount = SQL_functions.sqlExecute(DB, selectRecordCount) # dataset return is a list
    if not bool(dbCount[0][0]):
        data = [
            ('John', 'Doe', '1111111111', 'jdoe@email.com'),
            ('Alex', 'Moffat', '9176744820', 'wamoffat4@gmail.com'),
            ('Zuli', 'Kitty', '2223334444', 'zuli@kitty.com'),
            ('Albert', 'Einstein', '2062321010', 'albert@einstein.com'),
            ('Nikola', 'Tesla', '2123331010', 'nikola@tesla.com'),
            ('Thomas', 'Edison', '1847001931', 'thomas@edison.com'),
            ('Benjamin', 'Franklin', '1706001790', 'ben@franklin.com'),
            ('Henry', 'Ford', '1863001947', 'henry@ford.com'),
            ('Alexander', 'Graham Bell', '1847001922', 'alex@bell.com'),
            ('Steve', 'Jobs', '1955002011', 'steve@jobs.com'),
            ('Bill', 'Gates', '1955000000', 'bill@gates.com')]
        SQL_functions.sqlInsert(DB, phoneInsert, data)
    else:
        print("Database already exists")

#========== ON SELECT
def onSelect(self, event):
    listBox = event.widget # REDUNDANT: event.widget is the widget element (.!listbox) that triggered the event - in this case the tkinter Listbox 
    select = listBox.curselection()[0] # REDUNDANT: Returns the line number of selected event widget (tkinter listbox) 
    index = self.lBox.curselection()[0] # Returns the line number of variable lBox (tkinter listbox) - used [0] to get first item from curselection() tuple return
    fullName = listBox.get(index) # returns the text (fullName) of the line selected
    print(fullName)
    dataSet = SQL_functions.sqlExecute(DB, phoneSelect.format(self.phoneIDs[index]))
    onClear(self)
    for d in dataSet:
        self.E_fName.insert(0, d[0]) # inserts data (text) starting from the beginning of the text box (0) 
        self.E_lName.insert(0, d[1])
        self.E_phone.insert(0, d[2])
        self.E_email.insert(0, d[3])

#========== ON ADD - get text in 'Entry' widgets, normalize data, data format check, write data to database     
def onAdd(self):
    #===== variables
    fName = self.E_fName.get()
    lName = self.E_lName.get()
    phone = self.E_phone.get()
    email = (self.E_email.get()).strip()
    #===== normalize & concatenate name
    fName = (fName.strip()).title() 
    lName = (lName.strip()).title()
    phone = phone.strip(' ,().-') #removing all other characters accept numbers
    #===== data format checking
    msg = checkFormat(fName, lName, phone, email)
    if msg !="": #===== message - only if data format error
        messagebox.showerror("Invalid Data Entered", msg)
    else: #===== check for duplicate name
        dbCount = SQL_functions.sqlExecute(DB, "SELECT COUNT(phoneID) FROM phonebook WHERE fName = '{}' and lName = '{}'".format(fName, lName)) # dataset return is a list
        if not bool(dbCount[0][0]):
            SQL_functions.sqlInsert(DB, phoneInsert, (fName, lName, phone, email))
            onRefresh(self) # refresh Listbox with new fullName            
        else:
            messagebox.showerror("Invalid Data Entered","{} {} already exists in the database".format(fName, lName))
        onClear(self)
    
#========== ON DELETE - checks if last entry in database, ask for confirmation of delete, execute SQL delete
def onDelete(self):
    if not checkSelect(self): return # Determine if a selection from listbox is made
    index = self.lBox.curselection()[0] # index of the listbox selection
    fullName = self.lBox.get(index) # the selected fullName value in the Listbox
    #===== check DB record count - cannot delete the last record or error will occur
    dbCount = SQL_functions.sqlExecute(DB, selectRecordCount) # dataset return is a list
    if dbCount[0][0] > 1:
         #===== delete - check if want to delete first, if OK is select execute SQL delete 
        if messagebox.askokcancel("Delete Confirmation", "All information associated with {} \nwill be permenantly deleted. Ok to continue?".format(fullName)): # returns True if user selects "OK"
            SQL_functions.sqlExecute(DB, "DELETE FROM phonebook WHERE phoneID = '{}' ".format(self.phoneIDs[index]))             
            onClear(self)
            onRefresh(self)
    else:
        messagebox.showerror("Last Record Error", "{} is the last record in the database and cannot be deleted.".format(fullName))
    
#========== ON REFRESH - clear Listbox, SQL select all 'fullName' records, populate Listbox will all records
def onRefresh(self):
    self.phoneIDs = []
    self.lBox.delete(0, END)
    dataSet = SQL_functions.sqlExecute(DB, "SELECT phoneID, fName, lName FROM phonebook ORDER BY lName, fName")
    for d in dataSet:
        self.phoneIDs.append(d[0]) #put unique phoneID at the end of the phoneIDs list variable
        self.lBox.insert(END,"{} {}".format(d[1],d[2])) #put "full name" at the end of the listbox

#========== CHECK SELECT - Determine if a selection from listbox is made 
def checkSelect(self):
    try:
        index = self.lBox.curselection()[0] # index of the listbox selection
        return True
    except:
        messagebox.showinfo("Missing Selection","Please select a name from the list.")
        return False

#========== ON UPDATE - determine selection made, normalize data, check data formated correctly, update email and/or phone record
def onUpdate(self):
    if not checkSelect(self): return # Determine if a selection from listbox is made
    index = self.lBox.curselection()[0]
    fullName = self.lBox.get(self.lBox.curselection()) # the selected fullName value in the Listbox
    nameParse = fullName.split() # dividing the full name into a list [fName, lName]
    #===== normalize data
    phone = (self.E_phone.get()).strip(' ,().-') #removing all other characters accept numbers
    email = (self.E_email.get()).strip()
    #===== check if data changed
    dataSet = SQL_functions.sqlExecute(DB, phoneSelect.format(self.phoneIDs[index]))
    if dataSet[0][2] == phone and dataSet[0][3] == email:
        messagebox.showinfo('Cancelled Request', 'No changes to email or phone number have been detected.')
        return
    #===== data format checking
    msg = checkFormat(nameParse[0], nameParse[1], phone, email)
    if msg != "": #===== message - only if data format error
        messagebox.showwarning("Invalid Data Entered", msg)
    else: #===== update - confirm first
        if messagebox.askokcancel('Update Request', '{} will be updated: \nPhone: {} \nEmail: {}'.format(fullName, phone, email)): # returns 'True' if OK is clicked
            SQL_functions.sqlExecute(DB, "UPDATE phonebook SET phone = '{}', email = '{}' WHERE phoneID = '{}'".format(phone, email, self.phoneIDs[index]))
            onRefresh(self)
        else:
            messagebox.showinfo('Cancelled Request', 'No changes have been made to {} {}.'.format(nameParse[0], nameParse[1]))
        onClear(self)    
    
#=============================================================
#========== MAIN
#=============================================================
if __name__ == '__main__':
    master = Tk() # Tkinter call
    App = ParentWindow(master) #calls function with customiztion and provides Tk object as argument 
    master.mainloop() # keeps window open
