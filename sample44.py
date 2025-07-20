# a = 1
# b = 1
# arr = [a,b]


# for i in range(8):
#     c = a+b
#     arr.append(c)
#     a = b
#     b = c
# print(arr)


def f(n, a, b, arr = None):
    if arr is None:
        arr = [a,b]
    if n <= 2:
        return arr
    c = a+b
    arr.append(c)
    return f(n-1, b, c, arr)

print(f(8, 1, 1))