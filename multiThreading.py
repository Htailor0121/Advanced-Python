import time
import threading
def calc_square(numbers):
    print("Calculated Square Number Is:")
    time.sleep(0.2)
    for number in numbers:
        print("square -->",number * number)

def calc_cube(numbers):
    print("Calculated Cube Number Is:")
    time.sleep(0.2)
    for number in numbers:
        print("cube -->",number * number * number)

# def calc_sum(numbers):
#     print("Calculated Sum Is:")
#     time.sleep(0.2)
#     for number in numbers:
#         print("sum -->",number + number)

# def calc_subs(numbers):
#     print("Calculated Substract Is:")
#     time.sleep(0.2)
#     for number in numbers:
#         print("substract -->",number - number)

# def calc_division(numbers):
#     print("Calculated Division Is:")
#     for number in numbers:
#         print("Division -->",number / number)

arr = [2,3,8,9,11]

t = time.time()

t1 = threading.Thread(target = calc_square,args=(arr,))

t2 = threading.Thread(target = calc_cube,args=(arr,))

# t3 = threading.Thread(target = calc_sum,args=(arr,))

# t4 = threading.Thread(target = calc_subs,args=(arr,))

t1.start()

t2.start()

# t3.start()

# t4.start()

t1.join()

t2.join()

# t3.join()

# t4.join()

print("Done In:",time.time()-t)