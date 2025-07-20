def f(s, i, j):
    if i > j:
        return True
    if s[i] != s[j]:
        return False
    return f(s, i+1, j-1)


s = [1,2,2,1]
print(f(s, 0, len(s)-1))