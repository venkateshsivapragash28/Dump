sentence = ['flow', 'flower', 'flight', 'fly']
min_count = float('inf')
min_count = 0
for word in sentence:
    i = 0
    j = 0
    while i < len(word) and j < len(sentence[0]):
        count = 0
        if word[i] == sentence[0][j]:
            count += 1
            i+=1
            j+=1
        else:
            min_count = min(min_count, count)
print(min_count)