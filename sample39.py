# from itertools import permutations
# arr = [1,2,3]
# sorted = arr.copy()
# sorted.sort()
# perm = list(permutations(sorted))
# print(perm)
# for i in range(len(perm)):
#     if list(perm[i]) == arr:
#         res = i
#         break
# if res+1 == len(perm):
#     print(list(perm[0]))  
# else:
#     print(perm[res+1])

from itertools import permutations

def nextPermutation( arr):
    sorted = arr.copy()
    sorted.sort()
    perm = list(permutations(sorted))
    for i in range(len(perm)):
        if list(perm[i]) == arr:
            res = i
            break
    if res+1 == len(perm):
        return list(perm[0])
    else:
        return perm[res+1]
arr = [1,2,3]
print(nextPermutation(arr))