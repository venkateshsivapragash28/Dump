s = 'abcdeeee'
max_count = 0
count = 1
# for i in range(len(s)):
#     count = 1
#     for j in range(i+1, len(s)):
#         if s[j] != s[i]:
#             count = count+1
#             max_count = max(max_count, count)
#         else:
#             break
# print(max_count)

string = ''
max_count = 0

for i in range(len(s)):
    string = ''
    count = 1
    string += s[i]
    for j in range(i+1, len(s)):
        if s[j] not in string:
            count+=1
            string+=s[j]
            max_count = max(max_count, count)

        else:
            break
print(max_count)