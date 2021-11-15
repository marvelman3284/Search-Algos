from random import randint
import time

start = time.time()
def quicksort(array: list[int]) -> list[int]:
    if len(array) < 2: return array

    low, same, high = [], [], []

    pivot = array[randint(0, len(array) - 1)]
    for item in array:
        if item < pivot:
            low.append(item)

        elif item == pivot:
            same.append(item)

        elif item > pivot:
            high.append(item)


    return quicksort(low) + same + quicksort(high)

def gen_random_arr(length: int, min: int, max: int) -> list[int]:
    res = []
    for _ in range(length):
        res.append(randint(min, max+1))

    return res


print(f"Total time taken: {time.time() - start}")
