# Adding and updating dictionary elements

student={"name":"jane","age":30,"address":"KTM"}
student["roll_no"]=21
print(student) #{"name":"jane","age":30,"address":"KTM","roll_no":21}

student["name"]="jon"
print(student)# {"name":"jon","age":30,"address":"KTM","roll_no":21}

other_info = {"institute": "Broadway", "phone_no": 9890989878}
student.update(other_info)
print(student)
# {"name": "Jon", "age": 30, "address": "KTM", "roll_no": 21, "institute": "Broadway", "phone_no": 9890989878}

student.update(last_name="ABC")
print(student) # {'name': 'jon', 'age': 30, 'address': 'KTM', 'roll_no': 21, 'institute': 'Broadway', 'phone_no': 9890989878, 'last_name': 'ABC'}


# Removing Dictionary Elements

student = {"name": "Jon", "age": 30, "address": "KTM",
           "roll_no": 21, "institute": "Broadway", "phone": 9890989878}

student.pop("phone")
print(student) # {'name': 'Jon', 'age': 30, 'address': 'KTM', 'roll_no': 21, 'institute': 'Broadway'

#phone_no = student.pop("phone")
#print(phone_no) #


key,value = student.popitem() # ("email" , "ajne@gm.com") # popitem le dictionary ko last element nikalcha
print(student)
print(key)
print(value)


