# Duplicates Not Allowed

student = {
    "name": "dilsha",
    "age": 23,
    "dep": "Mca"
}
print(student)
# To get individual value use get method two method
print(student.get("name"))
print(student["dep"])
# to print length of dictionary
print(len(student))
# to print type of dictionary
print(type(student))
# another way of creating dictionary
thisdict = dict(name="John", age=36, country="Norway")
print(thisdict)
# to change the value
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.keys()
y = car.values()

print(x)  # before the change
print(y)
# To add new value
car["color"] = "white"

print(x)  # after the change
print(y)
# To update the value
car.update({"year": 2018})
print(car)
# To remove item from dictionary
car.pop("model")
print(car)
# To clear entire item from dictionary
car.clear()
print(car)  # output:{}
