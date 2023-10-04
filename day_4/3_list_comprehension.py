# List comprehension is an elegant way of creating a list oin one line

a=[]
for i in range(5):
    a.append(i)
print(a)  # [0, 1, 2, 3, 4]

a = [i for i in range(5)] # List comprehension
print(a) # [0, 1, 2, 3, 4]
