def isArraySpecial(self, nums):
    def sub(a, b):
        return abs(a-b)

    i = 0
    temp = 2
    while i < len(nums):
        if sub(nums[i], nums[i+1]) % 2 != temp:
            temp = sub(nums[i], nums[i+1] %2)
            i+=1