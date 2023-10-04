# sort(key:optional, reverse:optional)
# sort method can take two parameters a key and a reverse
# reverse takes boolean type and key takes a function as parameters


data = [12,11,12,13,44,55,42,23,23,5]
result = data.sort()
print(result)  #none
print(data) # [5, 11, 12, 12, 13, 23, 23, 42, 44, 55]


data.sort(reverse=True) # descending order
print(data) # [55, 44, 42, 23, 23, 13, 12, 12, 11, 5]


data = ["mango","apple","banana","pineapple","you"]
data.sort()
print(data) # ['apple', 'banana', 'mango', 'pineapple', 'you']

data.sort(reverse=True) # descending order
print(data)  # ['you', 'pineapple', 'mango', 'banana', 'apple']


data =[(10,12),(3,5),(2,1),(40,10),(3,8)]

def get_second_element(element):
    return element[1]

data.sort(key=get_second_element)

print(data)  # [(2, 1), (3, 5), (3, 8), (40, 10), (10, 12)]


