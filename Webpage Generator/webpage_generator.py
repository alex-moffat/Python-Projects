# PYTHON: 3.8.2
# AUTHOR: Alex Moffat
# PURPOSE: The Tech Academy Bootcamp - WEBPAGE GENERATOR
#=============================================================================
description = """
This program was written by Alex Moffat.\n
This is a demonstration of programming based on requirements given from The Tech Academy Python Course. \n
"""
requirements="""
Create a tool that can automatically create a basic HTML web page.
The page is very simple. It will simply have the text "Stay tuned for our amazing summer sale!" on the page.
Use a Python script that will automatically create the .html file needed.
Create a GUI with Tkinter that enables users to set body text for web page.
"""
contact = """
Alex Moffat\n
wamoffat4@gmail.com\n
(917) 674-4820"""

#===== TAGS
"""
 datetime, now, deltatime, total_seconds, open, write, close, tkinter, Text, Button, grid,
 delete, insert, isinstance, destroy, lambda, title, iconbitmap, Tk(), row, column, resizeable,
 config, padx, pady, sticky,columnspan
"""
#=============================================================================

#===== IMPORTED MODULES
import os
from tkinter import *
from datetime import *

#===== VARIABLES
tStart = datetime.now() # script timing
tInc = datetime.now() # script increment timing
webPage = ''
title = "Automated webpage" # webpage title
body = 'Stay tuned for our amazing summer sale!' # webpage body text  

#========== SCRIPT TIMING - gets elapsed time of script execution, reset increment time
def sTime(name):
    global tInc
    if name != None:
        iTime = round(timedelta.total_seconds(datetime.now() - tInc) * 1000)
        tTime = round(timedelta.total_seconds(datetime.now() - tStart) * 1000)
        print("SCRIPT {} completed in {} ms and total time from start is {} ms\n".format(name, iTime , tTime))
    tInc = datetime.now() 

#========== RESET TEXT - set text in text fields to default
def resetText(obj, txt):
    obj.delete("1.0", END)
    obj.insert('1.0', txt)

#=============================================================
#========== TKINTER GUI - CREATE tkinter window with grid
#=============================================================
def createGUI():
    #===== WINDOW =====
    win = Tk()
    #=== title & icon
    win.title('Insert Webpage Content')
    win.iconbitmap('favicon.ico')
    #=== size & position center
    win.resizable(width=False, height=False)
    #===== TEXT =====
    t1 = Text(win, width=50, height=1, wrap=NONE)
    t2 = Text(win, width=50, height=4, wrap=WORD)
    #=== size & position
    t1.grid(row=0, column=1, columnspan=3, padx=(10,20), pady=(40,10), sticky=N+S+W+E)
    t2.grid(row=1, column=1, columnspan=3, padx=(10,20), pady=(0,10), sticky=N+S+W+E)
    #===== BUTTONS =====
    b1 = Button(win, text = "Default Title")
    b2 = Button(win, text = "Default Body")
    b3 = Button(win, text = "Create Webpage")
    b4 = Button(win, text = "Close Program")
    #=== configure
    b1.configure(command=lambda obj=t1, txt=title: resetText(obj, txt))
    b2.configure(command=lambda obj=t2, txt=body: resetText(obj, txt))
    b3.configure(height=2, command=lambda newTitle=t1, newBody=t2: insertContent(newTitle, newBody))
    b4.configure(height=2, command=lambda : win.destroy())
    #=== size & position
    b1.grid(row=0, column=0, padx=(20,10), pady=(40,10), sticky=W+E)
    b2.grid(row=1, column=0, padx=(20,10), pady=(0,10), sticky=W+E)
    b3.grid(row=2, column=0, padx=(20,10), pady=(0,20))
    b4.grid(row=2, column=3, padx=(10,20), pady=(0,20), sticky=E)
    sTime('createGUI') # script timer
    

#=============================================================
#========== WEBPAGE
#=============================================================

#========== CREATE PAGE - create framework with indexed insert wildcards
def createPage():
    global webpage
    webpage = """
        <!DOCTYPE html>
        <html lang='en'>
            <head>
                <title>{0}</title>
                    <meta charset='utf-8'>
            </head>
            <body>
                {1}
            </body>
        </html>    
        """
    print("Webpage framework created:|n",webpage)
    sTime('createPage')

#========== INSERT PAGE CONTENT - insert contents into webpage framework
def insertContent(newTitle, newBody):
    sTime(None)
    global webpage
    if isinstance(newTitle,str) and isinstance(newBody,str): #string format
        newPage = webpage.format(newTitle, newBody)
    else: # text widget object
        newPage = webpage.format(newTitle.get("1.0",END).strip(), newBody.get("1.0",END).strip())
    print(newPage)   
    sTime('insertContent')
    writePage(newPage)    
    
#========== WRITE PAGE 
def writePage(newPage):
    file = open('webpage.html','w') # a = append what exists, w = overwrite
    file.write(newPage)
    file.close()
    print("Webpage created in this path:\n{}".format(os.getcwd()))
    sTime('writePage')
    


#=============================================================
#========== MAIN
#=============================================================        
if __name__ == '__main__':
    createGUI()
    createPage()
    
