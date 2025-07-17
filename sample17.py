arr = [1,4,3,2,7,4]
arr.sort(reverse = True)
product = 1
for i in range(3):
    product = product * arr[i]
print(product)
