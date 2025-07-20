nums = [4, 0, 4, 3, 3]
k = 5
best = sum(nums[:k])/k
current = sum(nums[:k])
for i in range(k,len(nums)):
    current = current + nums[i] - nums[i-k]
    best = max(best, current)
print(best)