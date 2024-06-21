# A Set in Python programming is an unordered collection data type that is iterable, 
# mutable and has no duplicate elements. 
#normal_set=set(['1','2','3'])
#print(normal_set)
#secon={3,4}
#print(secon)
def set_creation(prompt):
    user_input=input(prompt)
    user_list=user_input.split()
    return set(map(int,user_list))
A=set_creation("Enter the elements of the set Awith space: ")
B=set_creation("Enter the elements of the set B with space: ")
#set operations
#union
union_result=A.union(B)
#intersection
intersection_result=A.intersection(B)
#difference
difference_resultAB=A.difference(B)
difference_resultBA=B.difference(A)
print("Set A:",A)
print("Set B:",B)
print("Union of A and B",union_result)
print("Intersection of A and B:",intersection_result)
print("Difference of A to B:",difference_resultAB)
print("Difference of B to A:",difference_resultBA)