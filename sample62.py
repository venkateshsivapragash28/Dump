arr = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1]
count = 0
max_count = 0
for i in arr:
    if i == 1:
        count+=1
    else:
        max_count = max(max_count, count)
        count = 0
max_count = max(max_count, count)
print(count)
print(max_count)