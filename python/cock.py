from random import randint

def cocktailSort(arr: list[int]) -> list[int]:
    n = len(arr)
    swapped = True
    start = 0
    end = n-1
    while (swapped==True):

        swapped = False

        for i in range(start, end):
            if (arr[i] > arr[i+1]) :
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped=True

        if (swapped==False):
            break

        swapped = False

        end = end-1

        for i in range(end-1, start-1,-1):
            if (arr[i] > arr[i+1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True

        start = start+1

    return arr

def gen_random_arr(length: int, min: int, max: int) -> list[int]:
    res = []
    for _ in range(length):
        res.append(randint(min, max+1))

    return res

if __name__ == "__main__":
    arr = gen_random_arr(100, 0, 100000)
    print(cocktailSort(arr))
