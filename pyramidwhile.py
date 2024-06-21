num_rows = int(input("Enter the number of row:"))
row = 1
pattern = ""
while row <= num_rows:
    space = "  " * (num_rows - row)
    star = "*   " * row
    pattern = pattern + space + star.rstrip() + '\n'
    row = row + 1
print(pattern)

# The rstrip() method in Python is a string method that removes any trailing characters (spaces are the default) from the right end of the string.
# It is commonly used to clean up strings by removing unwanted characters at the end.
# Syntax
# str.rstrip([chars])