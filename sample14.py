tickets = [5,1,1,1]
k = 0
i = 0
count = 0
n = len(tickets)
while tickets[k] > 0:
    if i == n:
        i = 0
    else:
        tickets[i]  = tickets[i] - 1
        if tickets[i] == 0:
            tickets.pop(i)    
        n = len(tickets)         
        count = count + 1
        i = i + 1
print(count)