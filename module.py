print(__name__)
print("welcome to module")
def test(a):
    if(a>0):
        print("positive")
    elif(a<0):
        print("negative")
    else:
        print("the number is zero")
# to call this function create a new file and import this file.
# the print statement also work when import
# __name__ print the module name