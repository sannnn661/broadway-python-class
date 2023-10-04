import time


def execution_time(func):
    def inner_func(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print("it took", end-start, "seconds")
        return result

    return inner_func

@execution_time
def test_fxn():
    for i in range(100000):
        pass
    print ("function completed")


test_fxn()


# WAP to make a decorator which prints the time execution of a function
import time


def execution_time(func):
    def inner_func(*args, **kwargs):
        start = time.time()  # 2
        result = func(*args, **kwargs)
        end = time.time()  # 3
        print("Function execution time is", end-start)
        return result
    return inner_func


@execution_time
def test_fxn():
    for i in range(1000000000):
        pass
    print("Function Completed !!")

test_fxn()



# start = time.time()
# test_fxn()
# end = time.time()
# print("Function took", end-start, "seconds !!")