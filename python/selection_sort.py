def sort(arr: list[int]) -> list[int]:
    min = 0


    for i in range(0, 9):
        min = i
        for j in range(i+1, 10):
            if arr[j] < arr[min]:
                min=j

        arr[min], arr[i] = arr[i], arr[min]

    return arr


