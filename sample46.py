def f(n, name):
    if n == 0:
        return 
    print(name)
    return f(n-1, name)

f(8, 'venkat')