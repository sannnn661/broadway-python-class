# Unlike list tuple doesn't have methods like append , sort , remove , pop etc  because tuple is an immutable datatype
# Tuple is immutable datatype.So,we ony have two methods in tuple count() and index()

#count()

a=(2,5,1,1,2,2,2,3,3,5)
result=a.count(2)
print(result) #4

#index()
# index (value , start:optional , end:optional)

a=(2,5,1,1,2,2,2,3,3,5)
result =a.index(2)
print(result) #0

result=a.index(2,3,8)
print(result) #4 .This type indexing  method is also valid in list.


