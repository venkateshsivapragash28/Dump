arr = [0,1,2]
nums = []
for i in range(len(arr)):
    if i%10 == arr[i]:
        nums.append(arr[i])
print(nums[0])