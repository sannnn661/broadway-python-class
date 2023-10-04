# Comprehension is the elegant way of creating list and dictionary in python
# Comprehension is supported in dictionary and list only.


# List Comprehension
data = [2, 3, 4, 5, 6]
result = []
for each in data:
    result.append(each**2)
print(result)  # [4, 9, 16, 25, 36]

result = [i**2 for i in data]  # this is list comprehension
print(result)  # [4, 9, 16, 25, 36]


result = [i for i in range(15) if i % 2 == 0]  # list comprehension with condition
print(result)  # 0, 2, 4, 6, 8, 10, 12, 14



# Dictionary Comprehension
student = [("name", "Jon"), ("age", 30), ("address", "KTM")]
result = dict(student)
print(result)  # {"name": "Jon", "age": 30, "address": "KTM"}

result = {}
for key, value in student:
    result[key] = value
print(result)  # {"name": "Jon", "age": 30, "address": "KTM"}

result = {}
for key, value in student:
    result.update({key: value})
print(result)  # {"name": "Jon", "age": 30, "address": "KTM"}


result = {k: v for k, v in student}  # dictionary comprehension
print(result)

data = (i for i in range(30)) # it might look like a tuple comprehension but it is not
# it is called as generator expression


