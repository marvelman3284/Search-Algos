from os import system as run
from random import randint, shuffle
import time

def sort(arr: list[int]) -> list[int]:
    start = time.perf_counter()
    done = False
    iters = 0

    while not done:
        try:
            iters += 1
            
            shuffle(arr)

            run('clear')
            print(f"Iteration number: {iters}")

            with open("data/bozo.txt", "a") as f:
                f.write("\n" + str(arr))

            if arr == sorted(arr): done = True
        except TimeoutError:
            print("Timeout Error :(")
            quit()
    print(f"Total time taken: {time.perf_counter() - start}")
    return arr

def gen_random_arr(length: int, min: int, max: int) -> list[int]:
    res = []
    for _ in range(length):
        res.append(randint(min, max+1))

    return res

if __name__ == "__main__":
    arr = gen_random_arr(10, 0, 10)
    sort(arr)
