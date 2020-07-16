# Python: 3.8.2
# Author: Alex Moffat
# Purpose: Convert Image to String, Convert String to Image 
#=============================================================
"""TAGS:
base64, b64encode, b64decode
"""
#=============================================================
description = """
This program was written by Alex Moffat.\n
This module designed to convert an image to a base64 string and a base64 string to image.\n
This module has 3 methods:\r
1. image2String(i) - takes image path (i) - reads 'image' and returns base64 string.\r
2. image2Text(i) - takes image name in same folder (i) - reads 'image' and writes base64 string to txt file with same name.\r
3. string2Image(s, f) - takes base64 string (s) & 'fileName.png' (f) - writes 'image' file"""

contact = """
Alex Moffat\n
wamoffat4@gmail.com\n
(917) 674-4820"""
#=============================================================

#========== IMPORTED MODULES
import base64

#========== IMAGE 2 STRING - takes image path (i) - uses "rb" read binary switch, reads "image" and returns base64 string
def image2String(i):
    with open(i, "rb") as imageFile:
        rStr = base64.b64encode(imageFile.read())
        print(rStr)
        return rStr

#========== IMAGE 2 Text - takes image name in same folder (i) - uses "rb" read binary switch, reads "image" and writes base64 string to txt file with same name
def image2Text(i):
    bStr=image2String(i)
    fileName = i.split('.')[0] + '.txt'
    newFile = open(fileName, "wb")
    newFile.write(bStr)
    newFile.close()

#========== STING 2 IMAGE - takes base64 string (s) & "fileName.png" (f) - uses "wb" write binary switch, writes "image"
def string2Image(s, f):
    newFile = open(f, "wb")
    newFile.write(base64.b64decode(s))
    newFile.close()


#=============================================================
#========== MAIN
#=============================================================
if __name__ == '__main__':
    pass
