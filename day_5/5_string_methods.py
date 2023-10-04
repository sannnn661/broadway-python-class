

message = "hello world bABE"

# 1.  capitalize()
result = message.capitalize() # it returns because string is immutable
print(result) #  Hello world

# 2. title()
result = message.title()
print(result) #Hello World

# 3. upper
result =message.upper()
print(result) # HELLO WORLD

# 4. lower
result = message.lower()
print(result)


# 5. split()
message = "hello world"
result = message.split()
print(result)  # ['hello', 'world']

message = "I,am,learning,python"
result = message.split(',')
print(result)  # ['I', 'am', 'learning', 'python']

message = "hello world"
result = message.split("o")
print(result)  # ["hell", ' w', 'rld']

message = "hello world"
result = message.split("l")
print(result)  # ["he, "", "o wor", "d"]

# 6. join()
data = ["hell", ' w', 'rld']
result = "o".join(data)
print(result)  # hello world

data = ["hello", "world"]
result = " ".join(data)
print(result)  # "hello world"

data = ["hello","world"]
result = " ".join(data)
print(result)




# 7. find()
message = "hello world"
result = message.find('orl')

print(result)  # 7

message = "hello world"
result = message.find('abc')
print(result)
# If we give the subset not present in the string then find() returns -1


# 8. replace()

message="hello world"
result = message.replace("hello","hElLo")
print(result)