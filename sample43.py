def reverse(arr, i, j):
    if i >= j:
        return 
    arr[i], arr[j] = arr[j], arr[i]
    reverse(arr, i+1, j-1)
    return arr


arr = [1,2,3,4,5,6,7,8,9,10]
print(reverse(arr, 0, len(arr)-1))