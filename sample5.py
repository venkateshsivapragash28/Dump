# arr = [2,4,1]
# min = arr[0]
# for i in range(len(arr)):
#     if arr[i] < min:
#         min = arr[i]
#         if min == arr[-1]:
#             arr.remove(arr[-1])
#         index = i
# arr = arr[index:]
# print(arr)
# max = arr[0]
# for i in range(len(arr)):
#     if arr[i] > max:
#         max = arr[i]
# print(max)


arr = [7,1,5,3,6,4]
min = arr[0]



def minimum(arr):
    min_val = arr[0]
    index = 0
    for i in range(1, len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]
            index = i
    return min_val, index
min_val, index = minimum(arr)
if index == len(arr) - 1:
    arr.pop(index)
    min_val, index = minimum(arr)
arr = arr[index:]
max = arr[0]
for i in arr:
    if i > max:
        max = i
print(max-min_val) 