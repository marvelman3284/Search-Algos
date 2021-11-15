import bubble_sort
import binary_search
import linear_search
import quick_sort
from rich.prompt import Prompt
import random
import time


def main():
    choice = Prompt.ask("Would you like to search or sort an array?", choices=['search', 'sort'])
    if choice == 'search':
        search = Prompt.ask("Which sort would you like to use?", choices=['linear', 'binary'])
        if search == 'linear':
            arr, find = linear_search.gen_random_list(100, 0, 1000)
            start = time.time()
            print(linear_search.search(arr, find))
            print(f"Time taken: {time.time() - start}")
        elif search == 'binary':
            lst = []
            for i in range(1000):
                lst.append(i)

            start = time.time()
            print(binary_search.binary_search(lst, random.randint(0, 999)))
            print(f"Time taken: {time.time() - start}")

    elif choice == 'sort':
        sort = Prompt.ask("Which sort would you like to use?", choices=['bubble', 'quick'])
        if sort == 'bubble':
            arr = bubble_sort.gen_random_list(20, 0, 100)
            start = time.time()
            print(bubble_sort.bubbleSort(arr))
            print(f"Time taken: {time.time() - start}")
        elif sort == "quick":
            arr = quick_sort.gen_random_arr(10000, 1000, 1000000)
            start = time.time()
            print(quick_sort.quicksort(arr))
            print(f"Time taken: {time.time() - start}")


if __name__ == "__main__":
    main()
