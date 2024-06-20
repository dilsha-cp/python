class sem3:
    def __init__(self,name,age):
      self.name=name
      self.age=age
    def student(self):
        subjects={
            'sub1':'Data mining',
            'sub2':'Information security',
            'sub3':'theory of computation'
        }
        print(subjects)
stud1=sem3('anshad',24)
print(stud1.name, '\n', stud1.age)
stud1.student()
class person:
    def __init__(self, firstname,lastname):
        self.firstname = firstname
        self.lastname=lastname
    def printname(self):
            print(self.firstname,self.lastname)
myself=person('dilsha','basheer')
myself.printname()