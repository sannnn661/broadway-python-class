# Methods are also a function but all the functions are not methods
# Those functions which  are defined inside a class and must he called using the class
# Methods must be called with  object

def addition(a,b): # Function definition
    return a+b

# here addition is just a function but not a method

result = addition(2,3) # Function call => This is a normal function (not a method)
print(result) #5


class Student:
    def get_age_after_10_years (self,current_age):
        return current_age + 10

student = Student()
result =student.get_age_after_10_years(21)
print(result) # 21

# Here  get_age_after_10_years() is a method

a=[3,2,1,5,4,10]
a.sort() # Function call => sort () is a function which is called with object . So, this is called a method

# method ko aagadi kei lagaera call garne

################################## LIST METHODS ##################################

# 1.append()

vowels = ["a","e","i","o"]
vowels.append("u")
print(vowels) # ['a', 'e', 'i', 'o', 'u']


# 2. extend()

data= [1,2,3]
data.extend([4,5,6,7,8])
print(data) # [1, 2, 3, 4, 5, 6, 7, 8]

data= [1,2,3]
result =data.extend([4,5,6,7,8])
print(result) # None

a=[1,2,3]
b=[4,5,6]
a.extend(b)
print(a) # [1,2,3,4,5,6]


# 3 . insert()
# insert (index, value)

vowels = ["a" ,"e","o","u"]
vowels.insert(2,"i")
print(vowels) # ['a', 'e', 'i', 'o', 'u']

a= [1,2,4,5,6]
a.insert(2,3)
print(a) # [1,2,3,4,5,6]

# 4. remove()
vowels = ['a', 'e', 'i', 'o', 'u']
vowels.remove("o")
print(vowels)

# vowels.remove("z")  # Error  # kina ki "z" tyo list ma chaina


# 5. pop()
# pop(index:optional)
vowels = ['a', 'e', 'i', 'o', 'u']
result = vowels.pop()
print(result)  # u
print(vowels)  # ['a', 'e', 'i', 'o']


result=vowels.pop(1) # we can also give index as a parameter
print(result) # e
print(vowels) # ['a', 'i', 'o']

a=[1,2,3,4,5]
result = a.pop()
print(result) # 5
print(a) # 1,2,3,4

a.pop(1)
print(a) # [1,3,4]


# 6. clear ()

vowels.clear()
print(vowels)   # []


# 7. index()

# index (value, start:optional , end:optional )
vowels = ['a', 'e', 'i', 'o', 'u']
result = vowels.index('e')
print(vowels)  # ['a', 'e', 'i', 'o', 'u']
print(result)  # 1

vowels = ['a', 'e', 'i', 'o', 'u','a','i' ,'a','o','a' ]
result = vowels.index("a")
print(result) # 0

result = vowels.index("a",4,8)
print(result) # 5


# 8. count

data =[1,2,3,4,4,4,4,5,6]
result =data.count(4)
print(result)   # 4 4 ota 4

vowels = ['a', 'e', 'i', 'o', 'u','a','i' ,'a','o','a' ]
result = vowels.count("a")
print(result)  # 4


# reverse [6,2,10,1,3,5]

a = [5,3,1,10,2,6]
a.reverse()
print(a) # []

# copy ()

a =[1,2,3]
b= a
print(a)
print(b)
print(a is b) # True . they are the same object


b=a.copy()
print(a)
print(b)
print(a is b) # false. a and b are two different objects


a=[[1,2,3],4]
b=a.copy()
a[0][1]=7
print(a) # [[1, 7, 3], 4]
print(b) # [[1, 7, 3], 4]


 #  here "b" is a shallow copy of "a" . Mutable objects are still the same onject in both "a" and "b" in shallow copy


 #  we can overcome this by using deepcopy

from copy import deepcopy
a = [[1, 2, 3], 4]
b = deepcopy(a)
a[0][1] = 7
print(a)  # [[1, 7, 3], 4]
print(b)  # [[1, 2, 3], 4]
