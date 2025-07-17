nums = [-2,1,-3,4,-1,2,1,-5,4]
max = 0
temp = []
for i in range(len(nums)+1):
    for j in range(i+1, len(nums)+1):
        if sum(nums[i:j]) > max:
            max = sum(nums[i:j])
            temp = nums[i:j]
print(max)
print(temp)
