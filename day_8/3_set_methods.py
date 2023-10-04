# object le call garyo vane function navae method


# copy()

s1 = {1,2,3,4,5}
s2 = s1.copy()
print(s1)
print(s2)


# union()

s1 ={1,2,3,4}
s2 ={3,4,5,6}

result = s1.union(s2)
print(result) # {1, 2, 3, 4, 5, 6}
print(s1|s2) # {1, 2, 3, 4, 5, 6}

# intersection

result= s1.intersection(s2)
print(result) # {3, 4}
print(s1&s2)  # {3, 4}

result = s2.intersection(s1)
print(result)  #{3, 4}

# difference

result= s1.difference(s2)
print(result)  # {1, 2}
print(s1-s2)  # {1, 2}

# isdisjoint()

s1 = {1,2,3,4,5,6}
s2 = {5,6,7,8}

print(s1.isdisjoint(s2)) # false


#issubset()

s1={1,2,3,4,5,6}
s2={3,4,5,6}

print(s1.issubset(s2)) # false
print(s2.issubset(s1)) # true

#issuperset()

print(s1.issuperset(s2)) # True
print(s2.issuperset(s1)) # False

# symmetric_difference

s1 ={1,2,3,4}
s2 ={3,4,5,6}

result = s1.symmetric_difference(s2)
print(result) # {1, 2, 5, 6}
print(s1^s2) # {1, 2, 5, 6}

# symmetric_difference_update()  # doesn't return value , set nai change huncha
s1 ={1,2,3,4,5,6}
s2 ={5,6,7,8}
r =s1.symmetric_difference_update(s2)
print(r) # none
print(s1) #  {1, 2, 3,4,7,8}
