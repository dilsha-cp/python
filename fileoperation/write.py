file=open('text4.txt','w')
file.write("This is new file")
print("create and write successfuly")
file.close()
with open('text5.txt','w')as file:
    file.write("iam file5")
print("create and write")
#To append
file=open('text4.txt','a')
file.write("\nThis is new file appended")
print("updated")