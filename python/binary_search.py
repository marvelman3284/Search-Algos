import math, random

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


if __name__ == "__main__":
    lst = []

    for i in range(1000):
        lst.append(i)

    binary_search(lst, random.randint(0, 999))

