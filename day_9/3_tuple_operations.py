#Concatenation(+)

a=(1,2,3)
b=(4,5,6)
print(a + b) #(1,2,3,4,5,6)

#Repetition / Broadcast (*)
a=(1,2)
print(a * 2)#(1,2,1,2)

#Membership Operation

a=(1,2,3)
print(2 in a) #True
print(3 not in a)#False
print (5 in (1,2,3,4,5)) # true
print (2 in (1,3,4,)) # False

# Built-in-functions
#Some functions that can be used with Tuple , whcih takes tuple as an argument


a=(1,2,3,4,5)
print(sum(a))#15
print(max(a))#5
print(min(a))#1

a=(5,2,3,1,4)
result=sorted(a)
print(result) # [1,2,3,4,5]


result=reversed(a)
print(tuple(result))# [4,1,3,2,5]

a = (3,2,5,1,7,4)
r = reversed(a)
print(list((r))) # [4, 7, 1, 5, 2, 3]




