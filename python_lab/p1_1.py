a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
c=input("Chose the symbol\n+\n-\n*\n/\n")
if c=="+":
    print("result:",a+b)
elif c=="-":
    print("result:",a-b)
elif c=="*":
    print("result:",a*b)
elif c=="/":
    if b!=0:
        print("result:",a/b)
    else:
        print("Division is not possible")



