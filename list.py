thislist=['apple','orange','mango']
print(thislist[0])
# to add item according to index
thislist[0]='pineapple'
print(thislist)
# to add at end of list
thislist.append('grape')
print(thislist)
# insert element at index position
thislist.insert(1,'banana')
print(thislist)
# negative index
print(thislist[-1])
# to remove elemnt
thislist.remove('grape')
print(thislist)
# to remove element using index
thislist.pop(1)
print(thislist)
# remove last element
thislist.pop()
print(thislist)
# to compain two list
list1=['abey','dilsha']
thislist.extend(list1)
print(thislist)