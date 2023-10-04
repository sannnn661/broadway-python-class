# *args and *kwargs are the arbitrary arguments

# these arguments are like the expandable bucket


def addition(*args):
    print(args)

addition(1,2)
addition(1,2,3,)
addition(1,2,3,4)
addition(1,2,3,4,5)

def addition(*args):
    return sum(args)


print(addition(1, 2))  # (1, 2)  # 3
print(addition(1, 2, 3))  # (1, 2, 3)  # 6
print(addition(1, 2, 3, 4))  # (1, 2, 3, 4)
# addition(1, 2, 3, "Hello", [1, 2])   # (1, 2, 3, "Hello", [1, 2])





def addition (**kwargs):
    print(kwargs)

addition(a=2 ,b=3)
addition(a=2 ,b=3 ,c=3)
addition(a=2 ,b=3 ,c=3,d=4)


def addition(**kwargs):
    print(kwargs)  # {"a": 2, "b": 3, "c": 4}
    return sum(kwargs.values())


addition(a=2, b=3)
addition(a=2, b=3, c=4)
addition(a=2, b=3, c=4, d=5)
