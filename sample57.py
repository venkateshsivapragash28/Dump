arr = [5, -3, 2, 1, -3, -3, 7, 2, 2]

for i in range(1,len(arr)):
    for j in range(i, 0, -1):
        if arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
print(arr)