#different method to create a file open is key word used for creation and open
# method 1
file_path="C:\\MCA\\SEM3\python\\fileoperation\\text1.txt"
with open(file_path,'w')as f:
    f.write("Hello World")
print("file created successfully")
# method 2

from pathlib import Path
file_path=Path("C:\\MCA\\SEM3\python\\fileoperation\\text3.txt")
file_path.touch()
print("created successfully")
#in os and pathlib empty file will be created
