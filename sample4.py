arr = [1,2,3]
num = ""
result = []
for i in arr:
    num = num + str(i)
number = int(num)
number = number+1
string = str(number)
for i in string:
    result.append(int(i))
print(result)


