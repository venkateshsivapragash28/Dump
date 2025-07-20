def f(n, i = None):
    if i is None:
        i = 0
    if i == n:
        return 
    print(i)
    return f(n, i+1)
f(8)