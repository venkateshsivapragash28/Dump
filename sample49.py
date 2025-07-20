counter = {}

arr = [1,1,2,3,4,5,5,5,6,9]

for i in arr:
    if i in counter:
        counter[i]+=1
    else:
        counter[i] = 1
print(counter[5])