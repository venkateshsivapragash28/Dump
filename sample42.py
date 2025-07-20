arr = [1,2,3,4,5,6,7,8,9]


# for i in range(len(arr)):
#     arr.insert(i,arr[-1])
#     arr.pop(-1)
#     print(arr)

i = 0
j = len(arr) - 1 

while i < j:
    arr[i], arr[j] = arr[j], arr[i]
    print(arr)
    i+=1
    j-=1
