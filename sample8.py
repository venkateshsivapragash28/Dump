n = 8
arr = []
for i in range(1,n,2):
    arr.append(i)
    arr.append(int(-i))
if n%2 != 0:
    arr.append(0)
print(arr)