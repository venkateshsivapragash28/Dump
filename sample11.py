nums = [3,1,-2,-5,2,-4]
pos = []
neg = []
for i in nums:
    if i < 0:
        neg.append(i)
    if i > 0:
        pos.append(i)
for i in range(len(neg)):
    neg.insert(i*2, pos[i])
print(neg)
            