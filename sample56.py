arr = [-5, 3, 2, 1, -3, -3, 7, 2, 2]

for i in range(len(arr)):
    for j in range(0, (len(arr) - 1) - i):
        if arr[j+1] < arr[j]: 
            arr[j+1], arr[j] = arr[j], arr[j+1]

print(arr)
