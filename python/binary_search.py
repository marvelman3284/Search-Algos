import math
from random import randint

def binary_search(lst: list[int], search_value: int) -> None:
    low = 1
    high = len(lst)
    for _ in range(len(lst)):
        mid = math.floor((low + high) / 2)
        if lst[mid] == search_value: 
            print(f"Value {search_value} found at index {mid}")
            break
        elif lst[mid] > search_value:
            high = mid - 1
        elif lst[mid] < search_value:
            low = mid + 1


def gen_random_arr(length: int, min: int, max: int):
    arr = [] 
    for _ in range(length):
        arr.append(randint(min, max))

    find = arr[randint(0, len(lst)-1)]

    return arr, find



if __name__ == "__main__":
    lst, find = gen_random_arr(100, 0, 10000)

    print(binary_search(lst, find))

