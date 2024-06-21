def is_Substring(main_str,sub_str):
    return sub_str in main_str
def count_char(main_str,character):
     return main_str.count(character)
def replace_str(main_str,old_Sub,new_Sub):
     return main_str.replace(old_Sub,new_Sub)
def capital_string(main_str):
     return main_str.upper()

def Main():
    main_str=input("Enter the Main String:")
    sub_str=input("Enter the Sub String:")
    print("1.Check if the String is a Substring of Another String")
    print("2.Count Occurrences of Character")
    print("3.Replace a substring with another substring")
    print("4.Convert to Capital Letters")
    choice=int(input("Enter your choice:"))
    if choice==1:
        is_Substring(main_str,sub_str)
        if is_Substring(main_str,sub_str)==True:
            print({sub_str},"is a part of main string ",{main_str})
        else:
            print({sub_str},"is not a part of main string ",{main_str})
    elif choice==2:
           character=input("Enter the char to count:")
           count=count_char(main_str,character)
           print("the character ",{character},"occure ",count,"times in main string",{main_str})
    elif choice == 3:
        old_sub = input("Enter the substring to replace: ")
        new_sub = input("Enter the new substring: ")
        result = replace_str(main_str, old_sub, new_sub)
        print(f"New string is: '{result}'")
    elif choice==4:
         cap_str=capital_string(main_str)
         print("string in capital letter:",cap_str)
    else:
         exit
         print("Wrong choice!")
Main()
         






# to check not the string present in substring use "not" keyword like substring not in mainstring