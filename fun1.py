#def is a key word used to define a function
# function should define first.
# in function argument doesnt need any datatype.

def hey():
    print('hello world using function')


hey()


def disp(name, age):
    print('my name is ', name + 'age:' + str(age))


disp('dilsha', 23)


def hello(*values):
    print(values)
    #values will print like tuple.
    print('first:' + values[0])
    #this will print the first value.


hello("dilsha", "basheer", "anshad","sainba")
