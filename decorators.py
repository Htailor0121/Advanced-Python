import time
def time_it(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        execution_time = (end-start)*1000
        print(f"execution time {(func.__name__)} took {execution_time} ms ")
        # print(func.__name__ + " took " + str((end - start)*1000)+ "mil sec.")
        return result
    return wrapper()
@time_it
def cal_square(numbers):
    result = []
    for number in numbers:
        result.append(number * number)
    return result
@time_it 
def cal_cube(numbers):
    result = []
    for number in numbers:
        result.append(number * number * number)
    return result
array = range(1,100000)
out_square = cal_square(array)
out_cube = cal_cube(array)

