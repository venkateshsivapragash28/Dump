def searchMatrix( arr, target):
        i = 0
        j = 0
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if arr[i][j] == target:
                    return True
        else:
                return False


arr = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(searchMatrix(arr, target))
