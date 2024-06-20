ans=0
def sum(a):
    if(a!=0):
        return a+sum(a-1)
    else:
        return 0
ans=sum(10)
print("result:",ans)