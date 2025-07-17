def max_distance(arr):
    for i in range(len(arr)):
        if arr[i] != arr[-1]:
            return abs(i - len(arr))-1














arr = [0,1]
print(max_distance(arr))