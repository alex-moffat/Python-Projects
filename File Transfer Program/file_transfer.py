# PYTHON: 3.8.2
# AUTHOR: Alex Moffat
# PURPOSE: The Tech Academy Bootcamp - File Transfer Assignment
#=============================================================================
description = """
This program was written by Alex Moffat.\n
This is a demonstration of programming based on requirements given from The Tech Academy Python Course. \n
"""
requirements="""
A program to identify & move all .txt files from one folder to another with the click of a button.
Find all .txt files in source folder modified in the last 24 hours and copy to destination folder.
GUI allowing user to browse and choose a specific folder that will contain the files to copied/moved from.
GUI allowing user to browse and choose a specific folder that will receive the copied files.
GUI allowing user to manually initiate the 'file check' process that is performed by the script.
"""
contact = """
Alex Moffat\n
wamoffat4@gmail.com\n
(917) 674-4820"""

#===== TAGS
"""
 datetime, now, deltatime, total_seconds, open, write, close, os, getmtime, listdir, join,
 shutil, move, filedialog, messagebox, path error checking
"""
#=============================================================================

#===== IMPORTED MODULES
import os
import shutil
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from datetime import *

#===== VARIABLES
tStart = datetime.now() # script timing
tInc = datetime.now() # script increment timing
source = "" # folder where the source files are
destination = "" # folder where files should be transfered to

#========== SCRIPT TIMING - gets elapsed time of script execution, reset increment time
def sTime(name):
    global tInc
    if name != None:
        iTime = round(timedelta.total_seconds(datetime.now() - tInc) * 1000)
        tTime = round(timedelta.total_seconds(datetime.now() - tStart) * 1000)
        print("SCRIPT {} completed in {} ms and total time from start is {} ms\n".format(name, iTime , tTime))
    tInc = datetime.now() 


#=============================================================
#========== TKINTER GUI - CREATE tkinter window with grid
#=============================================================
def createGUI():
    #===== WINDOW =====
    win = Tk()
    #=== title & icon
    win.title('Extract & Transfer txt Files')
    win.iconbitmap('favicon.ico')
    #=== size & position center
    win.resizable(width=False, height=False)
    #===== ENTRIES =====
    v1 = StringVar()
    v2 = StringVar()
    e1 = Entry(win, width=100, textvariable = v1)
    e2 = Entry(win, width=100, textvariable = v2)
    #=== size & position
    e1.grid(row=0, column=1, columnspan=3, padx=(10,20), pady=(40,10), sticky=N+S+W+E)
    e2.grid(row=1, column=1, columnspan=3, padx=(10,20), pady=(0,10), sticky=N+S+W+E)
    #===== BUTTONS =====
    b1 = Button(win, text = "Source")
    b2 = Button(win, text = "Destination")
    b3 = Button(win, text = "Transfer All txt Files")
    b4 = Button(win, text = "Copy Recently Modified Files")
    b5 = Button(win, text = "Close Program")
    #=== configure
    b1.configure(command=lambda obj=v1: getDir(obj))
    b2.configure(command=lambda obj=v2: getDir(obj))
    b3.configure(height=2, command=lambda sPath=v1, dPath=v2: extractTextFiles(sPath, dPath))
    b4.configure(height=2, command=lambda sPath=v1, dPath=v2: copyRecent(sPath, dPath))
    b5.configure(height=2, command=win.destroy)
    #=== size & position
    b1.grid(row=0, column=0, padx=(20,10), pady=(40,10), sticky=W+E)
    b2.grid(row=1, column=0, padx=(20,10), pady=(0,10), sticky=W+E)
    b3.grid(row=2, column=0, padx=(20,10), pady=(0,20))
    b4.grid(row=2, column=1, padx=(10,10), pady=(0,20), sticky=W)
    b5.grid(row=2, column=3, padx=(10,20), pady=(0,20), sticky=E)
    sTime('createGUI') # script timer
    
#========== GET DIR - tkinter askdirectory, invoke dialog modal, get folder path from user, place folderpath into Entry widget
def getDir(obj):
    sPath = filedialog.askdirectory()
    obj.set(sPath)

#========== CHECK PATHS - make sure both paths are valid
def checkPaths(sPath, dPath):
    global source, destination
    source = sPath.get().strip()
    destination = dPath.get().strip()
    if source == "" or destination == "":
        #===== make sure both paths are selected
        messagebox.showwarning("INVALID PATH", "Make sure both the source and destination folders are selected.")
        return False
    elif source == destination:
        #===== make sure both paths different from each other
        messagebox.showwarning("INVALID PATH", "Make sure the source and destination folders are different.")
        return False
    else:
        #===== make sure source path is valid
        try:
            files = os.listdir(source)            
        except:
            messagebox.showwarning("INVALID PATH", "Source path is not valid. Please select another source folder.")
            return False
        try:
            files = os.listdir(destination)            
        except:
            messagebox.showwarning("INVALID PATH", "Destination path is not valid. Please select another destination folder.")
            return False
    return True

#========== EXTRACT TEXT FILES - find all .txt files in source folder
def extractTextFiles(sPath, dPath):
    sTime(None)
    if checkPaths(sPath, dPath): # check if both paths are valid
        rString = ""
        fCount = 0
        #===== search all files in source folder for .txt files
        files = os.listdir(source)
        for f in files:
            fPath = os.path.join(source, f)
            #=== get txt files, count, get last modified date, transfer to destination 
            if fPath.endswith('.txt'):
                fCount += 1
                mTime = date.fromtimestamp(os.path.getmtime(fPath))
                rString = rString + '\n' + f + ' --> Last modified: ' + str(mTime)
                shutil.move(fPath, destination)
        print('There where {} txt files moved from the source folder to the destination folder: {}'.format(fCount, rString))
    sTime('extractTextFiles') # script timer

#========== COPY RECENT - find all .txt files in source folder modified in the last 24 hours and copy to destination folder
def copyRecent(sPath, dPath):
    sTime(None)
    if checkPaths(sPath, dPath): # check if both paths are valid 
        rString = ""
        fCount = 0
        #===== search all files in source folder for .txt files
        files = os.listdir(source)
        for f in files:
            fPath = os.path.join(source, f)
            #=== get txt files, count, get last modified date, copy to destination 
            if fPath.endswith('.txt'):
                mTime = datetime.fromtimestamp(os.path.getmtime(fPath))
                #=== Files modified in the last 24 hours (86400 seconds)
                if timedelta.total_seconds(tStart - mTime) <= 86400: 
                    fCount += 1
                    rString = rString + '\n' + f + ' --> Last modified: ' + str(mTime)
                    shutil.copy(fPath, destination)
        print('There where {} recently modified txt files copied to the destination folder: {}'.format(fCount, rString))
    sTime('copyRecent') # script timer
    
#=============================================================
#========== MAIN
#=============================================================        
if __name__ == '__main__':
    createGUI()    
    
