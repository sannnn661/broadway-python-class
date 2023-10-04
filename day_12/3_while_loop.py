# While is another type of loop in Python which iterates until the condition after the ..
# while state is truthy. The loop stops once the condition becomes falsy

# The condition parameter must be updated from inside the loop , otherwise loop goes in infinite iteration



# print first 20 even numbers

num =0
count = 0

while count != 20 :
    if num % 2 ==0:
        print(num)
        count += 1
    num += 1