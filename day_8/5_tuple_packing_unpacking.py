a=1
print(type(a)) # int

a= (1)
print(type(a)) # int

a=(1,)
print(type(a)) # tuple

a=1,
print(type(a)) # tuple and this is a tuple packing

a=1,2,3
print(a) # (1, 2, 3)
print(type(a))

#  TUPLEs in python can be packed and unpacked

# Tuple packing
a=1 , # this is tuple packing
print(a)

a= 2,3,4 # this is also a tuple packing


vowels = "a","e","i","o","u"
print(vowels) # ("a","e","i","o","u")


# unpacking

a,b,c=1,2,3
print(a) #1
print(b) #2
print(c) #3

# possible errors in tuple packing and unpacking

#a,b = 1,2,3 # too many values to unpack
print(a)
#a,b,c = 1,2 # not enough values to unpack
print(a)

# swapping values in python

a =1
b =2

temp = a
a=b
b= temp

print(a) #2
print(b) #1

a,b = b,a # always write a code that runs generally
print(a)
print(b)