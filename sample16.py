def findLHS( nums):
    nums.sort()
    arr = set(nums)
    return arr



nums = [1,1,2,2,3,3,4,4,5,5]
print(findLHS(nums))