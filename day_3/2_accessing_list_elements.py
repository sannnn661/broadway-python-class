# List elements are accessed using indexing and slicing

# Indexing
# Indexing in python starts from 0 for forward indexing and -1 for reverse indexing
vowels=["a","e","i","o","u"]
print (vowels[0])  # a
print (vowels[3])  # o
# print (vowels[5])  # IndexError. List index out of range

print(vowels[-1])  # u
print(vowels[-4])  # e
# print(vowels[-6]) # IndexError. List index out of range


# Slicing
# Slicing is done using ":" with start and end values
# #always goes from left to right
data = ["a","b","c","d","e","f","g","h","i","j"]
print(data[:]) # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(data[2:9]) # ["c","d","e","f","g","h","i"]
print(data[4:7]) # ["e","f","g"]
print(data[:5])  # ["a","b","c","d","e"]
print(data[0:5])  # ["a","b","c","d","e"]
print(data[3:])  # ["d","e","f","g","h","i","j"]
print(data[8:2]) # [] empty right to left


print(data[-8:-2]) # ['c', 'd', 'e', 'f', 'g', 'h']
print(data[:-3])   # ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(data[-4:])   # ['g', 'h', 'i', 'j']

print(data[-3:-9]) # []
print(data[1:9:2]) # ['b', 'd', 'f', 'h']


values = ["a","b","c","d","e","f","g","h","i","j"]
print(values[2:9]) # "c","d","e","f","g","h","i"
print(values[4:]) # "e","f","g","h","i","j"
print(values[0:5]) # "a","b","c","d","e"
print(values[8:3]) # []
print(values[:6]) # "a","b","c","d","e","f"
print(values[-8:-3]) # "c","d","e","f","g"
print(values[-2:-6]) # []
print(values[-9:7]) # "b","c","d","e","f","g"
print(values[-9:-2:2]) # ["b","d","f","h"]