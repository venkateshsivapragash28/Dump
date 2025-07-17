ls = [1,1,0,1,1]
ls = set(ls)
ls = list(ls)
nums = []
print(ls)
for i in ls:
    if i > 0:
        nums.append(i)
print(sum(nums))