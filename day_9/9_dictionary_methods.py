# removing elements from dictionary

student = {"name":"Jon", "age":"30","address":"KTM"}

#pop

# it takes key as an argument

result =student.pop("age")
print(result) # 30
print(student) # {'name': 'Jon', 'address': 'KTM'}

#student.pop("phone") # it raises KeyError as "phone" is not present in the dict

#popitem()

student = {"name":"Jon", "age":"30","address":"KTM"}
result=student.popitem()
print(result) #('address', 'KTM')
print(student) # {'name': 'Jon', 'age': '30'}


# clear()

student = {"name":"Jon", "age":"30","address":"KTM"}
student.clear()
print(student)  # {}

del student   # it deletes the obj named student

# copy()

student = {"name":"Jon", "age":"30","address":"KTM"}
student1 = student.copy()
print(student)  # {'name': 'Jon', 'age': '30', 'address': 'KTM'}
print(student1)


# get
student = {"name":"Jon", "age":"30","address":"KTM"}
name = student.get("name")
print(name) # Jon
phone = student.get("phone")
print(phone) # none
phone=student.get("phone", 982323232)
print(phone) # 982323232



# keys
student = {"name":"Jon", "age":"30","address":"KTM"}
keys = student.keys()
print(keys) # dict_keys(['name', 'age', 'address'])

# values
value=student.values()
print(value) # dict_values(['Jon', '30', 'KTM'])

#items
item= student.items()
print(item) # dict_items([('name', 'Jon'), ('age', '30'), ('address', 'KTM')])

items =list(student.items())
key,value = items[0]
print(key)
print(value)



# fromkeys

y={}
result=y.fromkeys([1,2],"hello")
print(y)
print(result)



#setdefault

student = {"name":"Jon", "age":"30","address":"KTM"}
student.setdefault("phone",90909090)
print(student)   # {'name': 'Jon', 'age': '30', 'address': 'KTM', 'phone': 90909090}

# keys()
student = {"name": "Jon", "age": 30, "address": "KTM"}
print(student.keys())  # dict_keys(["name", "age", "address"])


# values()
print(student.values())  # dict_values(["Jon", 30, "KTM"])


# items()
items = student.items()
print(items)  # dict_items([("name", "Jon"), ("age", 30), ("address", "KTM")])

for key, value in items:
    print(key)  # name
    print(value)  # Jon