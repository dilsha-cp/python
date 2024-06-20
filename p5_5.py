#file handling
#read and write operations
import os
f=open('text1.txt','r')
print(f.read())
f=open('text1.txt','a')
f.write("this is appended text")
f.close()
f=open('text1.txt','r')
print(f.read())
# to create a new file
f=open('newfile.txt','x')
print("created successfully!")
