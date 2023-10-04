# Membership Operation ("in" and "not in")
# Membership in dictionary is checked in keys (not in values)
student = {"name":"alex" , "age":30}

print("name" in student) # true

print("alex" in student) # false

print("age" not in student) # false