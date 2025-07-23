# nums = []
# count = 0
# k = 3
# for i in range(len(arr)):
#     for j in range(i+1, len(arr)+1):
#         nums.append(arr[i:j])
# print(nums)

# for i in nums:
#     if sum(i) == k:
#         count+=1
# print(count)


# count = 0
# if arr is None:
#     print(0)
# for i in range(len(arr)):
#     total = 0
#     for j in range(i, len(arr)):
#         total = total + arr[j]
#         if total == k:
#             count+=1
# print(count)



# count = 0
# n = len(arr)
# for i in range(n):
#     total = 0
#     for j in range(i, n):
#         total += arr[j]
#         if total == k:
#             count += 1
# print(count)


arr = [1,1,1]
k = 2
o_sum = 0
count = 0
n_sum = 0
for i in range(len(arr)):
    n_sum+=arr[i]
    print(n_sum)
    if n_sum - o_sum == k:
        count+=1
        o_sum = n_sum
        
print(count)