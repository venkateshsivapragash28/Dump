def f(n, sum = None):
    if sum is None:
        sum = 0
    if n == 0:
        return sum
    sum = sum + n
    return f(n-1, sum)


print(f(3))