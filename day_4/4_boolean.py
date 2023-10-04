# True and False are the boolean types in Python
# True and False are also the keywords in Python



# Operations that give boolean type

a=5
b=10
c=15

# relational operations
print(b>a) # True
print(b!=a) # True
print(a>c) # False


# logical operations

print(b>a and a==c) #False
print(b>a or a==c) #True
print(not a) # False

# membership operation
print(2 in [1,2,3]) #True
print(3 not in [1,2,3]) #False


# Identity Operation

a=1
b=1
print(a==b) # True
print(a is b) # True only for small numbers

a=11212212121233333333334444444444555555555555555555555555555555
b=11212212121233333333334444444444555555555555555555555555555555

print(a==b) # True
print(a is b)

# check id first , id(a)


# Concept of Truthy and Falsy

# Truthy

# All non-empty data types and non-zero numbers are truthy values

# lsit [] , touple () , set {}

a= 12
b=5.7
c=[1,2]
b=(11,99)
f={"name":"john"}
g= True

# We can check the truthiness of the data using bool function

print(bool(b)) # True

# Falsy
## All empty datatypes and zero are falsy values

a= 0
b=0.0
c=[]
b=()
f={}
g= False

print(bool(b)) # False

# Python booleans are the subclass of the integer class . That means True is 1 and False is 0
a= True
b= 3
print(a+b) # 4
print(60*False) # 0

