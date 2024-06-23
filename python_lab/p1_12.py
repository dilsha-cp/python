import os
import sys
def create_dir(path):
    try:
        os.makedirs(path)
        print(f"directory {path} is created")
    except OSError as e:
        print("error",e)
def listdir(path):
    try:
        files=os.listdir(path)
        print(f"content of {path}")
        for file in files:
           print(file)
    except OSError as e:
      print("error",e)
def searchfile(path):
    try:
        py_files=[f for f in os.listdir(path) if f.endswith('.py')]
        print(f"python file in {path}")
        for file in py_files:
            print(file)
    except OSError as e:
        print("error",e)
def removefile(path):
   try:
       os.remove(path)
       print(f"file {path} is removed")
   except OSError as e:
       print("error",e)
directory_newpath=r"C:\MCA\SEM3\python\python_lab\directory1"
dtr_listpath=r"C:\MCA\SEM3\python\python_lab"
dir_rempath=r"C:\MCA\SEM3\python\python_lab\file3.txt"
create_dir(directory_newpath)
listdir(dtr_listpath)
searchfile(dtr_listpath)
removefile(dir_rempath)
# to get the current path of directory
print(os.getcwd())
script_directory = os.path.dirname(os.path.abspath(sys.argv[0])) 
print(script_directory)
