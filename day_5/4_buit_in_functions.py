# 1.  len() => It gives the length of any sequential objects

ab= "boss"
print(len(ab)) # 4

# 2. type() => It gives datatype of the object

print(type(ab)) # str
print(type([1,2,23,4])) # list

# 3.  slice() => It takes start and end values
s = slice(2, 5)
m = "Hello"
print(m[s])  # 'llo'