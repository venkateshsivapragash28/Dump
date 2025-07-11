list = [1,2,3,4]
product = 1
arr = []
for i in list:
    product = product*i
for i in list:
    arr.append(int(product//i))
print(arr)