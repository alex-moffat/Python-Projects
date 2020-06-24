# PYTHON: 3.8.2
# AUTHOR: Alex Moffat
# PURPOSE: Tech Academy Boot Camp, Step 162 Assignment
"""
Requirements:
-Write a script that creates a database and adds new data into that database.
-Your script will need to use Python 3 and the sqlite3 module.
-Your database will require 2 fields: an auto-increment primary integer field and a field with the data type "string".
-Your script will need to read from the supplied list of file names at the bottom of this page and determine only the files from the list which end with a “.txt” file extension.
-Next, your script should add those file names from the list ending with “.txt” file extension within your database.
-Finally, your script should legibly print the qualifying text files to the console.

TAGS:
 SQL, sqlite3.version, error handling, connect, cursor, execute, CREATE, INSERT, SELECT
 slice, upper, fetchall
"""
# ============================================================================
#===== Required input variable
fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

#===== IMPORTED MODULES
import sqlite3

#========== CONNECT - establish connection to DB and print sqlite3 version
def dbConnect(db):
    conn = None
    try:
        conn = sqlite3.connect(db) # creates a db if one does not exist
        print(sqlite3.version)
    except ValueError as e:
        print("DB Connection Error: {}".format(e))
    finally:
        if conn: conn.close() # close db connection if open

#========== USE CONNECTION - establish connetion to DB and return open connection
def dbUse(db):
    conn = None
    try:
        conn = sqlite3.connect(db) # creates a db if one does not exist        
    except ValueError as e:
        print("DB Connection Error: {}".format(e))        
    return conn

#========== EXECUTE - can pass SQL statement
def sqlExecute(db, statement):
    conn = dbUse(db)
    if conn != None: #===== EXECUTE 
        try:
            cur = conn.cursor() # creates cursor object 'cur'
            cur.execute(statement)
            if statement[slice(0,6)].upper() == 'SELECT':
                dataset = cur.fetchall()
                if conn: conn.close()
                return dataset
        except ValueError as e:
            print("DB Execute Error: {}".format(e))
        finally:
            if conn: conn.close()            
    else:
        print("DB Connection Error...cannot execute SQL statement")

#========== INSERT - can pass SQL db, table statement, values statement (can be single tuple or list of tuples
def sqlInsert(db, statement, iValue):
    conn = dbUse(db)
    if conn != None: #===== INSERT 
        try:
            cur = conn.cursor() # creates cursor object
            if isinstance(iValue, list): #===== MULTIPLE ROW INSERT
                cur.executemany(statement, iValue)
                conn.commit()
                print(cur.rowcount, " records inserted.")
            elif isinstance(iValue, tuple): #===== SINGLE ROW INSERT
                cur.execute(statement, iValue)
                conn.commit()
                print(cur.rowcount, " record inserted.")
            else:
                print("DB INSERT Error: Values are not formatted correctly - need list or tuple")
        except ValueError as e:
            print("DB INSERT Error: {}".format(e))
        finally:
            if conn: conn.close()            
    else:
        print("DB Connection Error...cannot execute SQL statement")
     
#========== STATEMENTS - SQL statements to pass

#===== CREATE TABLE - files
sCreateFiles = "CREATE TABLE IF NOT EXISTS files(\
    fileID INTEGER PRIMARY KEY AUTOINCREMENT,\
    fName VARCHAR(50))"   

#===== INSERT - populate TABLE files
sFiles = "INSERT INTO files (fName) VALUES (?)"
                 


#========== MAIN - STEP 162 - main script to run
#=================================================
def step162():
    #===== Create database
    dbConnect('test_2.db')
    #===== Create table
    sqlExecute('test_2.db', sCreateFiles)
    #===== Find .txt files from list/tuple --> add to new list
    txtList = []
    for f in fileList:
        if '.txt' in f:
            t = (f,) # add single element tuple to list (NOTE: comma is needed or just string is added)
            txtList.append(t) 
    #===== INSERT .txt files into files TABLE if exist
    if txtList != []: sqlInsert('test_2.db', sFiles, txtList)
    #===== SELECT .txt files from files TABLE - print to screen
    s1 = "SELECT fName FROM files WHERE fName LIKE '%.txt'"
    dataset = sqlExecute('test_2.db', s1)
    if dataset != []:
        printString = ""
        for r in dataset:
            printString += "{}\n".format(r[0])
        print("There are {} txt files: \n".format(len(dataset)) + printString)
    else:
        print("There are no txt files")

    
if __name__ == '__main__':
    step162()
