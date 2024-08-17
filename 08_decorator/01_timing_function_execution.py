#Timing Function Execution
#Write a decorator that measures the time a fuction takes to execute.

import time

def time_calculation(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        function(*args, **kwargs)
        result = function(*args, **kwargs)
        end = time.time()
        print(f"{function.__name__} ran in {end-start} time")
        return result
    return wrapper
@time_calculation
def example_function(n):
    time.sleep(n)

example_function(1)


