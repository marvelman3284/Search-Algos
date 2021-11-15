import math
def jump_search(arr: list[int], find_val: int):
    jump = math.floor(math.sqrt(len(arr))) 
    step = jump
    for _ in range(len(arr)):
        print(step)
        if arr[step] < find_val:
            step += jump
        if arr[step] > find_val:
            step -= jump
            for i in arr[0:step]:
                if i == find_val:
                   return f"Index at {i}"
                else: continue

    
#     for i in range(len(arr)):
#         i += jump
#         if arr[i] == find_val:
#         elif arr[i] > find_val:
#             for j in arr[:jump]:
#                if j == find_val:
#                    return f"Index at {arr.index(j)}"
#                else: continue
#         elif arr[i] < find_val:
#             for j in arr[jump:]:
#                 if j == find_val:
#                    return f"Index at {arr.index(j)}"
#                 else: continue
# 

print(jump_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 5))
