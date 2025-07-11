needle = 'sad'
haystack = 'abcdakjfdslkjfdkljnadskjnsadlkDSJFjnlSDKjfndlkjfndslksjfn'

n = len(needle)
i = 0
while i <= len(haystack) - n:
    if haystack[i:i+n] == needle:
        print(f"Found at index {i}")
    i += 1
print('done')
