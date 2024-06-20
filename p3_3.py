#class polymorphism
class car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model=model
        self.year = year
    def move(self):
        print('drive')
class boat:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model=model
        self.year = year
    def move(self):
        print('sail')
class plane:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model=model
        self.year = year
    def move(self):
        print('fly')

car1=car('abc','def',2001)
print(car1.brand,car1.model,car1.year)
car1.move()
boat1=boat('hij','klm',2001)
print(boat1.brand,boat1.model,boat1.year)
boat1.move()
plane1=plane('nop','qrs',2001)
print(plane1.brand,plane1.model,plane1.year)
plane1.move()
