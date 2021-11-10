import random

def search(lst: list[int], val: int) -> None:
    for i, j in enumerate(lst):
        if lst[i] == val: print(f"Value {j} found at index {i}") 

def gen_random_list(l: int, min: int, max: int): 
    lst = []
    for _ in range(l):
        lst.append(random.randint(min, max))

    find_val = lst[random.randint(0, (len(lst) - 1))]
    return lst, find_val


if __name__ == "__main__":
    l, find = gen_random_list(10, 0, 100)
    print(l)
    search(l, find)
