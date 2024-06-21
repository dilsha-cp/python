factorial_dic={}
def factorial(n):
    if n in factorial_dic:
        return factorial_dic[n]
    if n == 0 or n==1:
        #factorial_dic[n]=1
        return 1
    else:
        result= n * factorial(n-1)
        #factorial_dic[n]=result
        return result
    
num=int(input("Enter the number:"))
result=factorial(num)
factorial_dic[num]=result
print("The factorial of",num,"is",result)
print("factorial dictionary:",factorial_dic)