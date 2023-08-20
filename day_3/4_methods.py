# Methods are also  functions but methods are the functions inside a class
# Methods must be called with  object

def addition(a,b): # Function definition
    return a+b

# here addition is just a function but not a method

result = addition(2,3) # function call
print(result) #5


class Student:
    def get_age_after_10_years (self,current_age):
        return current_age + 10

student = Student()
result =student.get_age_after_10_years(21)
print(result) # 21

# Here  get_age_after_10_years() is a method










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


# 3 . insert()

vowels = ["a" ,"e","o","u"]
vowels.insert(2,"i")
print(vowels) # ['a', 'e', 'i', 'o', 'u']



# 4. remove()
vowels = ['a', 'e', 'i', 'o', 'u']
vowels.remove("o")
print(vowels)

# vowels.remove("z")  # Error kina ki "z" tyo list ma chaina


# 5. pop()
vowels = ['a', 'e', 'i', 'o', 'u']
result = vowels.pop()
print(result)  # u
print(vowels)  # ['a', 'e', 'i', 'o']


result=vowels.pop(1) # we can also give index as a parameter
print(result) # e
print(vowels) # ['a', 'i', 'o']


# 6. clear ()

vowels.clear()
print(vowels)   # []


# 7. index()
vowels = ['a', 'e', 'i', 'o', 'u']
result = vowels.index('e')
print(vowels)  # ['a', 'e', 'i', 'o', 'u']
print(result)  # 1


# 8. count
data =[1,2,3,4,4,4,4,5,6]
result =data.count(4)
print(result)   # 4 4 ota 4
