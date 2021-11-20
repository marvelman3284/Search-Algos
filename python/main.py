import bubble_sort
import binary_search
import linear_search
import quick_sort
import jump_search
from rich.prompt import Prompt
import random, time


def main():
    choice = Prompt.ask("Would you like to search or sort an array?", choices=['search', 'sort'])
    if choice == 'search':
        search = Prompt.ask("Which sort would you like to use?", choices=['linear', 'binary', 'jump'])
        if search == 'linear':
            arr, find = linear_search.gen_random_list(100, 0, 1000)
            start = time.perf_counter()
            print(linear_search.search(arr, find))
            print(f"Time taken: {time.perf_counter() - start}")
        elif search == 'binary':
            lst = []
            for i in range(1000):
                lst.append(i)

            start = time.perf_counter()
            print(binary_search.binary_search(lst, random.randint(0, 999)))
            print(f"Time taken: {time.perf_counter() - start}")

        elif search == 'jump':
            arr, find = jump_search.gen_random_arr(100, 0, 1000)
            start = time.perf_counter()
            print(jump_search.main())
            print(f"Time taken: {time.perf_counter() - start}")

    elif choice == 'sort':
        sort = Prompt.ask("Which sort would you like to use?", choices=['bubble', 'quick'])
        if sort == 'bubble':
            arr = bubble_sort.gen_random_list(20, 0, 100)
            start = time.perf_counter()
            print(bubble_sort.bubbleSort(arr))
            print(f"Time taken: {time.perf_counter() - start}")
        elif sort == "quick":
            arr = quick_sort.gen_random_arr(10000, 1000, 1000000)
            start = time.perf_counter()
            print(quick_sort.quicksort(arr))
            print(f"Time taken: {time.perf_counter() - start}")


if __name__ == "__main__":
    main()
