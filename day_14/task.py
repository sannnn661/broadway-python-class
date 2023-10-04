#WAP to delete all the occurrences of a specified character in a given string
#S = “All the occurrences of a specified character in a given string”
#Input = “a”
#Output = “ll occurrences of  specified chrcter in  given string”


sentence = "i am all good"
dell= input("enter what you want to delete")
result = ""
for each in sentence:
    if each==dell:
        continue
    result += each
print(result)



