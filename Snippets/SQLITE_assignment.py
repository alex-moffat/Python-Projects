# PYTHON: 3.8.2
# AUTHOR: Alex Moffat
# PURPOSE: The Tech Academy Bootcamp - SQLITE ASSIGNMENT
#=============================================================================
"""
TAGS:
 SQL, sqlite3.version, error handling, connect, cursor, execute, CREATE, INSERT, SELECT
 slice, upper, fetchall, executescript, 'with' sqlite3.connect()
"""
# ============================================================================

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
            if statement[slice(0,6)].upper() == 'SELECT': #===== SELECT
                dataset = cur.fetchall()
                if conn: conn.close()
                return dataset
            elif statement[slice(0,6)].upper() == 'UPDATE': #===== UPDATE
                conn.commit()
                print(cur.rowcount, " record updated.")
            elif statement[slice(0,6)].upper() == 'DELETE': #===== DELETE
                conn.commit()
                print(cur.rowcount, " record deleted.")
        except ValueError as e:
            print("DB Execute Error: {}".format(e))
        finally:
            if conn: conn.close()            
    else:
        print("DB Connection Error...cannot execute SQL statement")

#========== INSERT - can pass SQL db, table statement, values statement (can be single tuple or list of tuples)
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

#=============================================================
#========== ASSIGNMENT
#=============================================================
db = "test_database.db"
tempDB = ':memory:' # saves to RAM and is gone once connection is closed

def assignment():
    con1 = sqlite3.connect(db)
    con2 = sqlite3.connect(tempDB)
    c1 = con1.cursor()
    c2 = con2.cursor()
    #===== create database
    c1.execute("CREATE TABLE IF NOT EXISTS people (firstName TEXT, lastName TEXT, age INT)")
    c2.execute("CREATE TABLE IF NOT EXISTS people (firstName TEXT, lastName TEXT, age INT)")
    #===== insert data
    c1.execute("INSERT INTO people VALUES ('Ron', 'Obvious', 42)")
    c2.execute("INSERT INTO people (firstName, lastName, age) VALUES (?, ?, ?)",('Ron', 'Obvious', 42))
    con1.commit()
    con2.commit()
    #===== select data
    c1.execute("SELECT * FROM people")
    c2.execute("SELECT * FROM people")
    print(c1.fetchall())
    print(c2.fetchall())    
    #===== close connection
    if con1: con1.close()
    if con2: con2.close() # database ':memory:' is gone when connection closed 
    #===== USING 'with' to simplify code - changes are commited automatically, but still need to close the connection
    with sqlite3.connect(db) as con3: # 
        c3 = con3.cursor()
        c3.execute("INSERT INTO people VALUES ('Alex', 'Moffat', 49)") # no need for commit
        c3.execute("SELECT * FROM people") # new value 'Alex Moffat' already present in database  
        print(c3.fetchall())
    if con3: # this will trigger outside with block
        print("Connection still open") 
        con3.close()
    else:
        print("Connection already closed")
    #===== OPEN 'with' to drop table --> create table --> insert --> select --> insert --> select
    with sqlite3.connect(db) as con4: 
        c4 = con4.cursor()
        #=== executescript() - non-parameterized code - note the comma seperated inserted values
        c4.executescript("""
            DROP TABLE IF EXISTS people;
            CREATE TABLE people (firstName TEXT, lastName TEXT, age INT);
            INSERT INTO people VALUES ('Ron', 'Obvious', 42), ('Alex', 'Moffat', 49);                      
            """)
        print("===== Created new table & added 2 records =====")
        c4.execute("SELECT * FROM people")
        print(c4.fetchall())
        #=== executemany() - parameterized statement that takes a list or tuple of tuples
        pTuple = (('Luigi', 'Vercotti', 43), ('Arthur', 'Belling', 28))
        pList = [('Royal', 'Albert', 12), ('Zuli', 'Kitty', 2)]
        c4.executemany("INSERT INTO people VALUES (?,?,?)", pTuple)
        c4.executemany("INSERT INTO people VALUES (?,?,?)", pList)
        print("===== Insert 2 records in tuple & 2 in list =====")
        c4.execute("SELECT * FROM people")
        print(c4.fetchall())
    if con4: con4.close()
    #===== INPUT - get data from user and insert with parameterized insert statement
    go = True
    fName = input("Enter your first name: ").title()
    lName = input("Enter your last name: ").title()
    while go:
        age = input("Enter your your age: ")
        try:
            age = int(age)
            go = False
        except:
            print('You must enter an integer for age.')
    data = (fName, lName, age)
    with sqlite3.connect(db) as con5: 
        c5 = con5.cursor()
        c5.execute("INSERT INTO people VALUES (?,?,?)", data)
        c5.execute("UPDATE people SET age=? WHERE firstName=? AND lastName=?", (45, 'Luigi', 'Vercotti'))
        print("===== select records with last name 'Vercotti' or 'Moffat' =====")
        c5.execute("SELECT * FROM people WHERE lastName=? OR lastName=?", ('Vercotti', 'Moffat'))
        print(c5.fetchall())
        print("===== select records with input first name =====")
        c5.execute("SELECT * FROM people WHERE firstName=?", (fName,))
        print(c5.fetchall())
    if con5: con5.close()
    #===== SELECT - using fetchall, fetchone, fetchmany
    with sqlite3.connect(db) as con6: 
        c6 = con6.cursor()
        pList = [('Peep', 'Chicken', 12), ('Plurp', 'Chicken', 3), ('Papaya', 'Chicken', 3), ('Supreme', 'Chicken', 1)]
        c6.executemany("INSERT INTO people VALUES (?,?,?)", pList)
        c6.execute("SELECT firstName, lastName, age FROM people WHERE age < 30 ORDER BY age DESC")
        #=== NOTE: Each time you fetch a row it is gone from the retrieved dataset
        print("===== fetchone() =====")
        for row in c6.fetchone(): 
            print(row)
        print("===== fetchmany(3) =====")
        for row in c6.fetchmany(3):
            print(row)
        print("===== fetchall() =====")
        for row in c6.fetchall():
            print(row)
        print("===== count =====")
        c6.execute("SELECT COUNT(*) FROM people WHERE age < 30")
        print("The select statement had {} records before each fetch".format(c6.fetchone()[0]))
        print("===== fetch one row at a time =====")
        c6.execute("SELECT firstName, lastName, age FROM people WHERE age < 30 ORDER BY age DESC")
        while True: # infinite loop requires a break
            row = c6.fetchone()
            if row is None: break
            print(row)
    if con6: con6.close()

        
if __name__ == '__main__':
    assignment()
