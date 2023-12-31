# We can access string elements using indexing and slicing which is similar to the list
# forward indexing starts from 0 and reverse indexing from -1

# indexing

message="hello world"
print(message[0]) # h
print (message[-1]) # d
print(message[5]) # space
#print(message[69])  # Error
#print(message[-6969]) # Error

# slicing

message ="i am learning python"
print(message[:6]) #i am l
print(message[0:5])#i am
print(message[3:8])# m lea
print(message[4:]) # learning python
print(message[7:2]) # ''
print(message[-8:-2]) # g pyth
print(message[-6:-8]) # ''
print(message[3:-3]) # m learning pyt
print(message[9:-11]) #



# Creating the object (empty and non empty)

# Accessing the elements ( Indexing / slicing /accessing element using Key )

# Operations

# Methods

# Built in functions

message = "Hello"

#message[2] = [L] # It is not possible because string is immutable

 # print (message)

del message # del is a keyword that deletes the object


data = "hello world. I am learning python"

print (data[:6]) #  "hello "
print(data[4:]) #  " o world. I am learning python "
print(data[0:4]) #  "hell"
print(data[2:8]) # "llo wo"
print(data[9:3]) # " "
print(data[-2:-8]) # " "
print(data[-9:-2]) # "ng pyth"
print(data[-8:7]) # " "
print(data[2:9:2]) # "lowr"



