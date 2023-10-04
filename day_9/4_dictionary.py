# Dictionary is the mutable datatypes in Python.
# They are the key-value pairs enclosed within curly braces.
# They are mutable

# creating an empty dictionary.
a={}
print(a) # {}
a=dict()  # using built-in function
print(a) # {}

#Creating non-empty dictionary
student={"name":"jane","age":30,"address":"KTM"}
print(student) #  {"name":"jane","age":30,"address":"KTM"}

student=dict(name="jane",age=30,address="KTM") # here you shouldn't give space such as first name is wrong
# it should be first_name
print(student)  #  {"name":"jane","age":30,"address":"KTM"}



#Accessing elements of a dictionary

#Dictionary elements are accessed using keys

student={"name":"jane","age":30,"address":"KTM"}
name=student["name"] # a = [1,2,3,4] # a[3]
print(name)

age=student["age"]
print(age) #30

address=student["address"]
print(address)#Ktm

# print(student["roll_no"]) #It raises key error

#Accessing dictionary elements using .get() method

student={"name":"jane","age":30,"address":"KTM"}
name=student.get("name")
print(name)#Jane

roll_no=student.get("roll_no")
print(roll_no)#None



# learn more about get , key bata tanne ma


####### Accessing dictionary elements ##############
student = {"name": "Jane", "age": 30, "address": "KTM"}
address = student['address']  # a = [1, 2, 3, 4]  # a[3]
print(address)  # KTM
print(student["roll_no"])  # KeyError

name = student.get("name")
print(name)  # Jane
print(student.get("roll_no"))  # None
