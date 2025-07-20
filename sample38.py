def pascal(arr):
    res = []
    for i in range(len(arr)-1):
        res.append(arr[i]+arr[i+1])
    return [1] + res + [1]
    

arr = [1]
print(arr)
for i in range(5):
    arr = pascal(arr)
    print(arr)