# we have different methods to addd and remove items in a set

# Set does not support indexing and slicing because set is unordered

#add

s={1,2,3}
result = s.add(4)
print(result) # none
print(s) # {1, 2, 3, 4}

# update()

s.update([4,5,6])
print(s) # {1, 2, 3, 4, 5, 6} # to add more than one value

#discard

s.discard(4) #discard takes element as an argument
print(s)  # {1, 2, 3, 5, 6}
s.discard(10) # it doesn't raise error

# remove

s.remove(5)
print(s)  # {1, 2, 3, 6}
# s.remove(10) # this raises an error

# pop()

s= {1,2,3,4,5,6}
s.pop()
print(s) # randomly pops out any one element from the set


# clear
s.clear()
print(s) # empty set {}








