# def __init__(self) is act as constructor
class MyClass2:
    year=2022
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def add_age(self):
        self.age=self.age+1
    def realocate(self,place):
        self.place=place
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("place:",self.place)
        print("year",str(MyClass2.year))
    @classmethod
    def add_year(cls):
        year=cls.year+1



x=MyClass2("dilsha",23,"malappuram")
y=MyClass2("anshad",24,"wynaad")
x.display()
y.display()
MyClass2.year=MyClass2.year+1
print("after age change")
x.add_age()
x.display()
print("after location change")
y.realocate("tirur")
y.display()
print("after year change")
MyClass2.add_year()
x.add_age()
y.add_age()
x.display()
y.display()