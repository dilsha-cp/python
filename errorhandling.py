b=10
c=0
try:
    print(10/b)
    print(10/0)
except ZeroDivisionError:
    print("denominator is zero")
print("completed")