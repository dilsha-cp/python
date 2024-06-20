#global declaration
#inside the function we cant change the value of value eg:value=value+5
#we can declare anthore value as local variable inside function but it doesnt change the global value
value = 30


def disp():
    print(value)
    s = value * 5
    print(s)


disp()
print(value)


def add():
    a = 2
    b = 3
    c = a + b
    print(c)


add()


def student(name, age, dep):
    print("name:" + name + "\nage:" + str(age) + '\ndep:' + dep)


student(name="dilsha", dep="mca", age=23)


def add(num1, num2):
    return (num1 + num2)


result = add(4, 8)
print(result)
