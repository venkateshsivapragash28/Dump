'''10.) Problem Title: Sum of Digits of Each Number in a List
Problem Statement:
You are given a list of non-negative integers.
Your task is to return a new list where each element is the sum of digits of the corresponding element in the original list.
Input Format:
•	A list of non-negative integers
Output Format:
•	A list of integers representing the sum of digits of each input number
Constraints:
•	0≤element≤106
•	List size ≤ 10⁵
Test Case 1:
Input:
[12, 101, 34]
Output:
[3, 2, 7]
Explanation:
•	1 + 2 = 3
•	1 + 0 + 1 = 2
•	3 + 4 = 7
Test Case 2:
Input:
[0, 5, 999]
Output:
[0, 5, 27]
Explanation:
•	0 → 0
•	5 → 5
•	9 + 9 + 9 = 27
Test Case 3:
Input:
[100, 200]
Output:
[1, 2]
Explanation:
•	1 + 0 + 0 = 1
•	2 + 0 + 0 = 2
'''


def sum_of_digits_list(number_list):
    result = []
    for number in number_list:
        digit_sum = 0
        for digit in str(number):
            digit_sum = digit_sum + int(digit)
        result.append(digit_sum)
    return result