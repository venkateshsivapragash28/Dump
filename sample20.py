s = 'coaching'
t = 'coding'

i = 0
j = 0
substring = 0
while i < len(s) and j < len(t):
    if s[i] == t[j]:
        i+=1
        j+=1
    else:
        substring = t[j:]
        break
print(substring)
print(len(substring))