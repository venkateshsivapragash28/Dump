arr = [9,8,7,1,2,3,4,11,5,12,15,13]



for k in range(len(arr)):
    i = 0
    j = 1
    while i < len(arr) and j < len(arr):
        if arr[j] < arr[i]:
            arr[j], arr[i] = arr[i], arr[j]
            i+=1
            j+=1
        else:
            i+=1
            j+=1
print(arr)