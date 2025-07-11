'''13.) Problem Title: Move Positive Elements First, Negative Elements Last
Problem Statement:
You are given an array containing both positive and negative integers.
Your task is to rearrange the elements so that:
•	All positive numbers come first
•	All negative numbers come after
•	The relative order of the elements should be preserved
Input Format:
•	A single line containing space-separated integers
Output Format:
•	A single line of integers with positives first, followed by negatives
Test Case 1:
Input:
1 -2 3 -4 5 -6
Output:
1 3 5 -2 -4 -6
Explanation:
All positive numbers appear first: 1 3 5
Then all negatives in order: -2 -4 -6
Test Case 2:
Input:
-1 2 -3 4 5 6
Output:
2 4 5 6 -1 -3
Explanation:
Moved all positives (in order): 2 4 5 6
Then negatives: -1 -3
Test Case 3:
Input:
1 2 3 -1
Output:
1 2 3 -1
Explanation:
Already in required order. No rearrangement needed.
'''


def reorder_by_sign(input_list):
    positive_numbers = []
    negative_numbers = []
    for number in input_list:
        if number >= 0:
            positive_numbers.append(number)
        else:
            negative_numbers.append(number)
    return positive_numbers + negative_numbers
