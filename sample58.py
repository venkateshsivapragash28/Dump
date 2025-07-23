arr = [11,13,14,15,17,18,19,20,20,21,22,23]
arr.sort()
max_count = 0
count = 1

for i in range(len(arr)-1):
    if arr[i+1] == arr[i]+1:
        count+=1
    elif arr[i+1] == arr[i]:
        continue
    else:
        max_count = max(max_count, count)
        count = 1
max_count = max(max_count, count)
print(max_count)