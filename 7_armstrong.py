'''7.) Problem Title: Armstrong Number Checker
Problem Statement:
A number is called an Armstrong number if the sum of its digits each raised to the power of the number of digits is equal to the number itself.
You are given an integer n. Determine whether it is an Armstrong number.
Input Format:
•	A single integer n
Output Format:
•	Print "Yes" if n is an Armstrong number
•	Print "No" otherwise
Constraints:
        1≤n≤109
Example 1:
Input:
153
Output:
Yes
Explanation:
13+53+33=1+125+27=153
Example 2:
Input:
123
Output:
No
Example 3:
Input:
9474
Output:
Yes
Explanation:
94+44+74+44=6561+256+2401+256=
9474

'''


def is_armstrong_number(number):
    number_of_digits = len(str(number))
    temp = number
    total_sum = 0

    while temp > 0:
        digit = temp % 10
        total_sum = total_sum + (digit ** number_of_digits)
        temp = temp // 10

    if total_sum == number:
        return "Yes"
    else:
        return "No"


print(is_armstrong_number(153))