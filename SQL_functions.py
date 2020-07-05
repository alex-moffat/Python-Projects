# PYTHON: 3.8.2
# AUTHOR: Alex Moffat
# PURPOSE: General use SQLite3 functions
"""
TAGS:
 SQL, sqlite3.version, error handling, connect, cursor, execute, CREATE, INSERT, SELECT
 slice, upper, fetchall, isinstance, ValueError as 
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

#========== EXECUTE - pass database and a non-parameterized SQL statement
def sqlExecute(db, statement):
    conn = dbUse(db)
    if conn != None: #===== EXECUTE 
        try:
            cur = conn.cursor() # creates cursor object 'cur'
            cur.execute(statement)
            switch = statement[slice(0,6)].upper()
            if switch == 'SELECT': #===== SELECT
                dataset = cur.fetchall()
                if conn: conn.close()
                return dataset
            else:
                conn.commit()
                r = "record"
                if cur.rowcount > 1: r = "records"
                if switch == 'UPDATE': #===== UPDATE
                    printStr = "{} {} updated in database {}".format(cur.rowcount, r, db)
                elif switch == 'DELETE': #===== DELETE
                    printStr = "{} {} deleted in database {}".format(cur.rowcount, r, db)                    
                elif switch == 'INSERT': #===== INSERT
                    printStr = "{} {} inserted in database {}".format(cur.rowcount, r, db)
                else:
                    printStr = "Execute complete in database {}".format(db)
                print(printStr)
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
     
if __name__ == '__main__':
    pass
