# To print multiplication table
num = int(input('enter the number for table:'))
r = int(input('enter the range: '))
for i in range(1, r + 1):
    print(str(i) + "*" + str(num) + "=" + str(i * num))
