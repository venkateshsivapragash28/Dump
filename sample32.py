counter = {}
arr = [1,2,2,3,3,4,1,4,5,6,6]

count = {}
for i in arr:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1


for i in arr:
    if count[i] == 1:
        print(i)
