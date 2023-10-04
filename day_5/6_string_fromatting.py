# We do string formatting using f-string

name = "Jon"

message = "i am name"

print(message) # i am name

message = f"i am {name}"
print(message) # i am Jon

name = "baby boss"
age = "69"

message = f"i am {name}. I am {age} years old"
print(message) # i am baby boss. I am 69 years old



# using format specifier (%s, %d, %f etc)

print('I am %s and I am %d years old' % (name, age))

# using .format() method
print('I am {}'.format(name)) #