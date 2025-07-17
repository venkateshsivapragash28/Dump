s = 'loveleetcode'
c = 'e'

a = []
b = []

for i in range(len(s)):
    a.append(i)
print(a)


for i in range(len(s)):
    if s[i] == c:
        b.append(i)
print(b)


nums = []
minimum_arr = []

for i in range(len(a)):
    minimum_arr = []
    for j in range(len(b)):
        diff = abs(b[j] - a[i])
        minimum_arr.append(diff)
        if len(minimum_arr) == len(b):
            nums.append(min(minimum_arr))
print(nums)