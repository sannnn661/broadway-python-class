# copy() method creates a new copy of the existing list

a= [1,2,3]
b=a
print(a) # [1, 2, 3]
print(b) # [1, 2, 3]

a.append(4)
print(a)  # [1, 2, 3, 4]
print(b) #  # [1, 2, 3, 4] a and b share same memory location

a= [1,2,3]
b = a.copy()

print(a) # [1, 2, 3]
print(b) # [1, 2, 3]

a.append(4)
print(a) # [1, 2, 3, 4]
print(b) # [1, 2, 3]


# shallow copy

a=[[1,2,3],4,5]

b= a.copy()

print(a) # [[1, 2, 3], 4, 5]
print(b) # [[1, 2, 3], 4, 5]

a[0][1] = 5
print(a) # [[1, 5, 3], 4, 5]
print(b) # [[1, 5, 3], 4, 5] # list bhitra ko mutable ni change huncha


# deep copy

from copy import deepcopy
a = [[1, 2, 3], 4, 5]
b= deepcopy(a)

print(a) # [[1, 2, 3], 4, 5]
print(b) # [[1, 2, 3], 4, 5]

a[0][1] =5
print(a) # [[1, 5, 3], 4, 5]
print(b) # [[1, 2, 3], 4, 5]