
arr = [[1,0,3], [6,1,5], [9,2,7]]
row = []
column = []
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == 0:
            row.append(i)
            column.append(j)

for i in row:
    for j in range(len(arr[i])):
        arr[i][j] = 0
print(arr)


for i in column:
    for j in range(len(arr)):
        arr[j][i] = 0
print(arr)