import time
import multiprocessing

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

if __name__ == "__main__":
    arr = [2,3,8,9,11]

    p1 = multiprocessing.Process(target = calc_square,args=(arr,))
    p2 = multiprocessing.Process(target = calc_cube,args=(arr,))

    p1.start()
    p1.join()

    p2.start()
    p2.join()