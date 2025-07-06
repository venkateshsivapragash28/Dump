'''3.) Problem Statement: Train Seat Berth Type Finder
You are given a seat number in a train coach that has 9 cabins, with 8 seats per cabin, making a total of 72 seats.
The seating pattern for each cabin follows this fixed order:
[Lower, Middle, Upper, Lower, Middle, Upper, Side Lower, Side Upper]
The seat numbers range from 1 to 72, and this pattern repeats for all cabins.
Task:
Given a seat number, write a program to determine the berth type (e.g., Lower Berth, Middle Berth, Upper Berth, Side Lower Berth, or Side Upper Berth).
Input Format:
•	A single integer n representing the seat number.
Constraints:
•	1 ≤ n ≤ 72
Output Format:
•	Print the seat number followed by the berth type in the following format:
Seat <n> is a <berth type>.
If the seat number is invalid (less than 1 or more than 72), print:
Invalid seat number. Must be between 1 and 72.
Example Input 1:
45
Example Output 1:
Seat 45 is a Lower Berth.
Example Input 2:
71
Example Output 2:
Seat 71 is a Side Lower Berth.
Example Input 3 (Invalid Input):
100
Example Output 3:
Invalid seat number. Must be between 1 and 72.

'''

berth_type = {
    1: "Lower Berth",
    2: "Middle Berth",
    3: "Upper Berth",
    4: "Lower Berth",
    5: "Middle Berth",
    6: "Upper Berth",
    7: "Side Lower Berth",
    0: "Side Upper Berth"
}

def berth(n = 17):
    n = n%8
    return berth_type[n]


print(berth())