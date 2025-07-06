''' 
 
1.) Second Smallest Number in Array Without Sorting
Problem Statement:
Given an array of integers, find the second smallest unique element. If there is no second smallest (all elements same), print -1.
Constraints:
•	1 <= n <= 100
•	-1000 <= nums[i] <= 1000
Input Format:
•	First line: Integer n (size of array)
•	Second line: n space-separated integers (array elements)
Output Format:
Print the second smallest element or -1.
Test Case 1:
Input:
5
4 2 1 3 2
Output:
2
Test Case 2:
Input:
4
5 5 5 5
Output:
-1
 
'''

def second_smallest_number(list):
    min = list[0]
    for i in list:
        if i <= min:
            min = i
    list.remove(min)
    second_min = list[0]
    for i in list:
        if i <= second_min:
            second_min = i
    return second_min


arr = list(map(int, input("Enter numbers separated by space: ").split()))
print(second_smallest_number(arr))