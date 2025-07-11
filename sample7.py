nums = [12,345, 2,6, 7896]
count = 0
for num in nums:
    num = str(num)
    if len(num)%2 == 0:
        count = count + 1
print(count)