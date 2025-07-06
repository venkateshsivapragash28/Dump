'''2.) Problem Title: Count and List Prime Numbers up to N
Problem Statement:
You are given an integer n.
Your task is to count how many numbers from 1 to n (inclusive) have exactly two distinct factors (including 1 and itself), and also print those numbers.
These numbers are known as prime numbers.
Input Format:
•	A single integer n
Output Format:
•	First line: An integer denoting the total count of such numbers
•	Second line: The space-separated list of those numbers

Test Case 1:
Input:
10
Output:
4
2 3 5 7
Explanation:
The prime numbers ≤ 10 are: 2, 3, 5, 7
Test Case 2:
Input:
20
Output:
8
2 3 5 7 11 13 17 19
Explanation:
The prime numbers ≤ 20 are: 2, 3, 5, 7, 11, 13, 17, 19
'''


def prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = 10
ls = []
for i in range(2, n):
    if prime(i) == True:
        ls.append(i)

print(len(ls))
print(' '.join(str(i) for i in ls))