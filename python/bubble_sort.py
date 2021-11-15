import random
def bubbleSort(lst):
    n = len(lst)

    for i in range(n-1):

        for j in range(0, n-i-1):

            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst 

def gen_random_list(l: int, min: int, max: int) -> list[int]: 
    lst = []
    for _ in range(l):
        lst.append(random.randint(min, max))

    return lst 


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]

    bubbleSort(arr)

#     print ("Sorted array is:")
#     for i in range(len(arr)):
#         print ("% d" % arr[i]),
# 
