def reverse(a):
    rev = 0
    while a != 0:
        dig = a % 10
        rev = rev * 10 + dig
        a = a // 10
    return rev
def is_palindrome(num):
    return (reverse(num)==num)


def addition(num):
    reversed_number = reverse(num)
    print("Reversed number:", reversed_number)
    sum=num+reversed_number
    print("sum is:",sum)
    # sum_rev=reverse(sum)
    # print("reversed sum is:",sum_rev)
    if is_palindrome(sum):
        print("Sum is a palindrome")
    else:
        print("Sum is not a palindrome")
        addition(sum)  # Recursively process the sum



num = int(input("Enter the number: "))
addition(num)