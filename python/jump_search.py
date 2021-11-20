import math
from random import randint

def jump_search(arr: list[int], find_val: int):
    jump = math.floor(math.sqrt(len(arr))) 
    step = jump
    for _ in range(len(arr)):
        if arr[step] < find_val:
            step += jump
        if arr[step] > find_val:
            step -= jump
            for i in arr[0:step]:
                if i == find_val:
                   return f"Value {find_val} found at index at {i}"
                else: continue
 
def gen_random_arr(length: int, min: int, max: int):
    arr = [] 
    for _ in range(length):
        arr.append(randint(min, max))

    find = arr[randint(0, len(arr)-1)]

    return arr, find

def main():
    arr, find = gen_random_arr(100, 0, 10000)
    print(jump_search(arr, find))

if __name__ == "__main__":
    main()
