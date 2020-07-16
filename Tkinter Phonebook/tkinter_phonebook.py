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
import icon_converter

#========== VARIABLES
w = 500 # App Window width
h = 330 # App Window height
DB = 'demo_phonebook.db' # demo phonebook database
phoneInsert = 'INSERT INTO phonebook (fName, lName, phone, email) VALUES (?, ?, ?, ?)' # standard SQL INSERT statement
phoneSelect = "SELECT fName, lName, phone, email FROM phonebook WHERE phoneID = '{}'" # standard SQL SELECT statement 
selectRecordCount = 'SELECT COUNT(phoneID) FROM phonebook' # count db records
icon = "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"

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
        #===== title bar & icon
        icon_converter.string2Image(icon, 'temp.ico') # create icon from base64 string
        M.iconbitmap('temp.ico')
        os.remove('temp.ico')
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
