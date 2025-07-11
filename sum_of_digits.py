n = 123456
sum = 0
while n:
    digit = n%10
    sum = sum + digit
    n = n//10
print(sum)
