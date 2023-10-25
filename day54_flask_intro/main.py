import time

current_time=time.time()
print(current_time)  # seconds since 1/1/1970


def decorator(function):
    def wrapper():
        start_time=time.time()
        function()
        end_time=time.time()
        print(f"{function.__name__}run speed:{end_time - start_time}s")
    return wrapper


@decorator
def fast_function():
    for i in range(1000000):
        i * i

@decorator
def slow_function():
    for i in range(10000000):
        i * i


fast_function()
slow_function()

