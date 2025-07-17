arr = [1,2,3,4]
ls = []
for i in range(len(arr)):
    sum = 0
    for j in range(i+1):
        sum = sum+arr[j]
    ls.append(sum)
print(ls)