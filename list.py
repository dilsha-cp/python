name = 'dilsha'
print(name[2])
# name[3]='a'
# print(name) like this we cant replace anything in string for this we use list (immutative)
# LIST
values = ['python', 'c', 'c++']
values[2] = 'laravel'
# mutative
print(values)
print(values[-2:])
print(values[0:1])
print(values[0:2])
values = values + ['php']
print(values)
# to add a value at end of list use append key word
values.append('html')
print(values)
# to add a value at end of the list from user
values.append(input('enter a value in list:'))
print(values)
