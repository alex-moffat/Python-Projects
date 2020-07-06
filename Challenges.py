# PYTHON: 3.8.2
# AUTHOR: Alex Moffat
# PURPOSE: The Tech Academy Bootcamp - MISCELLANEOUS CHALLENGES
#=============================================================================
description = """
This program was written by Alex Moffat.\n
This is a demonstration of programming based on requirements given from The Tech Academy Python Course. \n
"""
requirements="""
SQL:
Create a database table in RAM named Roster that includes the fields ‘Name’, ‘Species’ and ‘IQ’
Populate your new table with the following values: ---> GIVEN
Update the Species of Korben Dallas to be Human
Display the names and IQs of everyone in the table who is classified as Human
RANGE:
Use the Python range() function with one parameter to display the following: --> GIVEN
TIME ZONE:
Create a script that will find out the current times in the Portland HQ and NYC and London branches.
Compare that time with each branch's hours to see if they are open or closed.
Print out to the screen the three branches and whether they are open or closed.
TKINTER:
Script will need to use Python 3 and the Tkinter module.
Script will need to re-create an exact copy of a GUI from the supplied image: --> GIVEN
Invoke a dialog modal that allows user to select a folder directory from their system.
Use the askdirectory() method from the Tkinter module.
Show the user’s selected directory path in the text field.
"""
contact = """
Alex Moffat\n
wamoffat4@gmail.com\n
(917) 674-4820"""

#===== TAGS
"""
 SQL, sqlite3, connect, cursor, execute, CREATE, INSERT, SELECT, fetchall,
 'with' sqlite3.connect(), range, datetime, pytz, strftime, now, deltatime, total_seconds,
 pytz.country_timezones, pytz.country_name, pytz.timezone(), askdirectory()
"""
#=============================================================================

#===== IMPORTED MODULES
import os
import sqlite3
import pytz
from datetime import *
from tkinter import *
import tkinter.filedialog

#===== VARIABLES
tStart = datetime.now() # script timing
tInc = datetime.now() # script increment timing
tempDB = ':memory:' # saves to RAM and is gone once connection is closed
given = (('Jean-Baptiste Zorg', 'Human', 122), ('Korben Dallas', 'Meat Popsicle', 100), ("Ak'not", "Mangalore", -5)) # challenge 1


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

#========== SCRIPT TIMING - gets elapsed time of script execution, reset increment time
def sTime(name):
    global tInc
    iTime = round(timedelta.total_seconds(datetime.now() - tInc) * 1000)
    tTime = round(timedelta.total_seconds(datetime.now() - tStart) * 1000)
    print("SCRIPT {} completed in {} ms and total time from start is {} ms\n".format(name, iTime , tTime))
    tInc = datetime.now() 

#===== PRINT TEXT - prints text inside button
def printText(var):
    pString = "Button pressed: {}"    
    if isinstance(var,str): #STRING INPUT
        print(pString.format(var))
    else: #OBJECT INPUT
        print(pString.format(var.cget('text'))) #gets info from widget object with '.cget()'
        

#=============================================================
#========== CHALLENGES
#=============================================================

#========== SQL
def cSQL():
    with sqlite3.connect(tempDB) as con:
        c = con.cursor()
        #===== create database
        c.execute("CREATE TABLE IF NOT EXISTS roster (rosterID INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(30), species VARCHAR(20), IQ INT)")
        #===== insert values
        c.executemany("INSERT INTO roster (name, species, IQ) VALUES (?,?,?)", given)
        #===== update value
        c.execute("UPDATE roster SET species = ? WHERE name = ?", ('Human', given[1][0]))
        #===== select & display the name & IQ of 'humans'
        c.execute("SELECT name, IQ FROM roster WHERE species = 'Human'")
        for row in c.fetchall(): print('Name: {}\t IQ: {}'.format(row[0],row[1]))
    if con: con.close()
    sTime('cSQL') # script timer

#========== RANGE 
def cRange():
    print("===== print 0,1,2,3 =====")
    for i in range(4):
        print(i)
    print("===== print 3,2,1,0 =====")
    for i in range(4,-1,-1):
        print(i)    
    print("===== print 8,6,4,2 =====")
    for i in range(8,0,-2):
        print(i)    
    sTime('cRange') # script timer
    
#========== TIME ZONE
def cTimeZone():
    #===== Returns the list of all the supported timezones by the pytz module
    '''print('The timezones supported by pytz module: ', pytz.all_timezones, '\n')'''
    #===== Returns a dict of country ISO Alpha-2 Code as key and country full name as value
    '''print('country_names =')
    for key, val in pytz.country_names.items():
        print(key, '=', val, end=',')
    print('\n')'''
    #===== Returns Country names
    gbName = pytz.country_names['GB']
    print('GB full name =', pytz.country_names['GB'])
    usName = pytz.country_names['US']
    print('US full name =', pytz.country_names['US'])
    #===== Returns Country timezones
    """print(pytz.country_timezones['GB'])
    print(pytz.country_timezones['US'])"""
    #===== Fetching time of a given time-zone
    print('Datetime of UTC Time-zone: ', datetime.now(tz=pytz.utc))
    #===== Challenge - Print out to the screen the three branches and whether they are open or closed
    #=== create timezone objects
    portland = pytz.timezone('America/Los_Angeles')
    nyc = pytz.timezone('America/New_York')
    london = pytz.timezone('Europe/London')
    offices = [portland, nyc, london]
    #=== print office and open status
    for i in offices:
        #=== get office
        if i == portland:
            sStart = "The Portland office"
        elif i == nyc:
            sStart = "The New York office"
        elif i == london:
            sStart = "The London office"
        #=== get the hour of the current local time at the office as integer compare to open/close times
        localTime = int(datetime.now(tz=i).strftime('%H')) 
        if localTime >= 9 and localTime < 17: #open
            sEnd = "is currently OPEN."
        else: #closed
            sEnd = "is currently CLOSED."
        print(sStart, sEnd)
    sTime('cTimeZone') # script timer

#========== TKINTER GUI - CREATE tkinter window with grid
def cGUI():
    #===== WINDOW =====
    win = Tk()
    #=== title & icon
    win.title('Check files')
    win.iconbitmap('favicon.ico')
    #=== size & position center
    win.resizable(width=False, height=False)
    #===== ENTRIES =====
    v1 = StringVar()
    v2 = StringVar()
    e1 = Entry(win, width=70, textvariable = v1)
    e2 = Entry(win, width=70, textvariable = v2)
    #=== size & position
    e1.grid(row=0, column=1, columnspan=3, padx=(10,20), pady=(40,10), sticky=N+S+W+E)
    e2.grid(row=1, column=1, columnspan=3, padx=(10,20), pady=(0,10), sticky=N+S+W+E)
    #===== BUTTONS =====
    b1 = Button(win, text = "Browse...")
    b2 = Button(win, text = "Browse...")
    b3 = Button(win, text = "Check for files...")
    b4 = Button(win, text = "Close Program")
    #=== configure
    b1.configure(command=lambda obj=v1: getDir(obj))
    b2.configure(command=lambda obj=v2: getDir(obj))
    b3.configure(height=2, command=lambda obj=b3: printText(obj))
    b4.configure(height=2, command=lambda obj=b4: printText(obj))
    #=== size & position
    b1.grid(row=0, column=0, padx=(20,10), pady=(40,10), sticky=W+E)
    b2.grid(row=1, column=0, padx=(20,10), pady=(0,10), sticky=W+E)
    b3.grid(row=2, column=0, padx=(20,10), pady=(0,20))
    b4.grid(row=2, column=3, padx=(10,20), pady=(0,20), sticky=E)
    sTime('cGUI') # script timer
    
#========== GET DIR - tkinter askdirectory, invoke dialog modal, get folder path from user, place folderpath into Entry widget
def getDir(obj):
    sPath = tkinter.filedialog.askdirectory()
    obj.set(sPath)
    

#=============================================================
#========== MAIN
#=============================================================        
if __name__ == '__main__':
    cSQL()
    cRange()
    cTimeZone()
    cGUI()
