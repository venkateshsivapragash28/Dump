'''6.) Problem Title: Reverse a Number
Problem Statement:
Given an integer number n, reverse its digits and return the reversed number.
If the input is a negative number, the reversed result should also be negative.
Input Format:
•	A single integer n
Output Format:
•	A single integer representing the reversed number
Example 1:
Input:
1234
Output:
4321
Example 2:
Input:
-987
Output:
-789
Note:
Avoid using string conversion or slicing to reverse the number.
'''


def reverse_number(number):
    is_negative = number < 0
    number = abs(number)
    reversed_number = 0

    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number = number // 10

    if is_negative:
        return -reversed_number
    else:
        return reversed_number
    
print(reverse_number(1234))