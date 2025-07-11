nums = [1,1,1,2,2,3,4,4,5,6]

def removeDuplicates(self, nums):
    for i in range(len(nums)+1):
        if nums[i]==nums[i]+1:
            nums = nums.remove(nums[i+1])
    return nums

print(nums)