# arr = [1,2,3,4,5,6,1,2,3]
# nums = []
# left = 0
# right = 0
# total = []

# for i in range(len(arr)):
#     right = i+1
#     total = arr[i]
#     nums.append(arr[i])
#     while arr[right] not in nums:
#         total += arr[right]
#         right+=1

arr = [1, 2, 3, 4, 5, 6, 1, 2, 3]
max_sum = 0

for i in range(len(arr)):
    nums = set() 
    total = 0
    for j in range(i, len(arr)):
        if arr[j] in nums:
            break
        nums.add(arr[j])s
        total += arr[j]
    max_sum = max(max_sum, total)

print(max_sum)
