# Python: 3.8.2
# Author: Alex Moffat
# Purpose: Misc assignments during Tech Academy Boot Camp
#Tags: dir, str, help, OS, open, close, read, write, append
#=======================================================


#===== METHODS lookup 
print(dir(str))
#print(help(str))

#===== OS METHODS
import os
#print(dir(os))
print(os.getcwd())

#===== I/O OPEN READ METHODS
def readFile():
    with open('test.txt','r') as f: # r = read only
        data = f.read()
        print(data)
        f.close()

#===== I/O OPEN WRITE METHODS
def writeData():
    data = '\nI love Python and wrote this using Python script'
    f = open('test.txt', 'a') # a = append what exists, w = overwrite 
    f.write(data)
    f.close()
    

if __name__ == '__main__':
    #readFile()
    #writeData()
    #readFile()
