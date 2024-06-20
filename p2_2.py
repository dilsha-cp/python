#inheritance
class person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    def display(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Address: ", self.address)
class student(person):
    def __init__(self,name,age,address,rollno,marks):
        super().__init__(name,age,address)
        self.rollno = rollno
        self.marks = marks
    def display(self):
        super().display()
        print("Roll No: ", self.rollno)
        print("Marks: ", self.marks)
stud1=student('dilsha','23','ade','18','34')
stud1.display()