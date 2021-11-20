from random import randint

def sort(arr: list[int]) -> list[int]:
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key

    return arr

def gen_Array(length:int, min: int, max: int) -> list[int]:
    arr = []

    for _ in range(length):
        arr.append(randint(min, max))

    return arr

def main():
    arr = gen_Array(100, 0, 10000)
    print(f"Unsorted array {arr}")
    sorted = sort(arr)
    print(f"sorted array {sorted}")

if __name__ == "__main__":
    main()
