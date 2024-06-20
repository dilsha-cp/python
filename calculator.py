# calculator
a = float(input('Enter the first number:'))
b = float(input('Enter thesecond number:'))
op = (input('select the operator:\n+\n-\n*\n/\n'))
if op == '+':
    add = a + b
    print('result:', add)
elif op == '-':
    dif = a -b
    print('result:', dif)
elif op == '*':
    mul = a * b
    print('result:', mul)
elif op == '/':
    if b == 0:
        print('division is not possible')
    else:
        div = a / b
        print('result:', div)
