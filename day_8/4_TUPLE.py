# Tuple is a immutable datatype in python . They are sequential datatype
# Tuple can take different datatypes regardless they are mutable or immutable

# Indexing and slicing in tuple is same as that of list
# Tuple elements are enclosed with parenthesis i.e. () , small bracket

# creating an empty tuple
t=tuple()
t=()

# creating a non-empty tuple
t=(1,1.1,[1,2,3])   # (1, 1.1, [1, 2, 3])
print(t)

#TUPLE elemets can be of any datatype

a = (1,2,3.4,"hello",[5,6],(6,9))
print(a)
############## Accessing TUPLE Elements ################

# Tuple elements are accessed using indexing and slicing

vowels = ("a","e","i","o","u")

print(vowels[0]) # (a)
print(vowels[4]) # (u)
print(vowels[-1]) # (u)
print(vowels[-3]) # (i)
print(vowels[-10]) # error
print(vowels[20]) # error


data =("a","b","c","d","e","f","g","h","i","j")

print(data[0:7]) # "a","b","c","d","e","f","g","h"
print(data[:5]) # "a","b","c","d","e","f"
print(data[6:]) # "g","h","i","j"
print(data[3:8]) # "d","e","f","g","h"
print(data[6:2]) # ()
print(data[6:-2]) # "g","h"
print(data[-8:-3]) # "c","d","e","f","g"
print(data[-9:8]) # "b","c","d","e","f","g","h"
print(data[-3:-7]) # ()
print(data[2:8:2]) # "c","e","g"
print(data[-9:-2:2]) # "b","d","f" ,"h"

# slicing
data = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j")
print(data[:5])  #( "a","b","c","d","e")
print(data[0:7]) # ("a", "b", "c", "d", "e", "f", "g")
print(data[3:])  # ("d", "e", "f", "g", "h", "i", "j")
print(data[4:8]) # ("e", "f", "g", "h")
print(data[9:3]) # ()
print(data[:-3]) # ("a", "b", "c", "d", "e", "f", "g")
print(data[0:-6]) # (a", "b", "c", "d")
print(data[-7:]) # ( "d", "e", "f", "g", "h", "i", "j")
print(data[-7:-3]) # ("d", "e", "f", "g")
print(data[-2:-6]) # ()
print(data[3:-4]) # ("d", "e", "f")
print(data[-8:7]) # ("c", "d", "e", "f", "g")

print(data[2: 9: 2]) # ("c", "e",  "g",  "i")


del data # it deletes the tuple object