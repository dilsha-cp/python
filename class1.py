class MyClass:
    def hello(self, name):
        self.name=name
    def print(self):
        print("hello "+self.name)


x = MyClass()
y=MyClass()
name="anshad"
name1 = "dilsha"
x.hello(name)
y.hello(name1)
x.print()
y.print()
#MyClass.hello(x)
# self is the argument pass to the function here x is the arrgument pass to self.
