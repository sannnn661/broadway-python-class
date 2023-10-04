# Set is a mutable datatype in Python .But the elements of the set must be immutable.
# Unlike list, set is unordered. So, indexing and slicing is not possible in python
# Set elements are always unique
# Ser are unordered .In set {1,2} is equal to {2,1}

# Set are created by enclosing objects in curly braces

# Creating an empty set
s=set()

# s = {} # this is not an empty set. It is an empty dictionary.


# Creating a non-empty set

s = {1,1.1,(1,2),True}
print(s)

s1=set([1,1,2,3,4,5,1,2,3,4,5,2,1,2])
print(s1)

data  ={1,2,3,4} # Set of integers and all elements are immutable

fruits = {"apple","mango","cherry","peach"} # Set of strings and all elements are immutable

a = {1,"a",(1,2),2.2} # Ser of mixed type but all elements are immutable

s = {1,[1,2],3}   # this is invalid set because it has list as an element which is mutable
s ={1,2,(1,2,[3,4])} # This is also invalid because tuple has a mutable element

