'''14.) Problem Title: Supermarket Discount Calculator
Problem Statement:
A supermarket provides the following discounts:
•	10% discount if the customer is a member
•	Additional 5% discount if the total bill exceeds 1000
Your task is to calculate the final bill amount after applying the applicable discounts.
The final amount should be rounded to 2 decimal places.
Input Format:
•	A list of integers prices representing item prices
•	A boolean is_member indicating membership status (True or False)
Output Format:
•	A float representing the final bill amount, rounded to 2 decimal places
Constraints:
•	Each price: 1≤price≤105
•	Number of items: 1≤n≤105
Discount Rules:
•	If the customer is a member, apply 10% off the total
•	If the (possibly discounted) total exceeds 1000, apply additional 5% off
Test Case 1:
Input:
prices = [500, 700, 300]  
is_member = True
Output:
1282.5
Explanation:
•	Total = 1500
•	10% off → 1500 × 0.9 = 1350
•	Additional 5% off → 1350 × 0.95 = 1282.5
Test Case 2:
Input:
prices = [300, 400]  
is_member = False
Output:
700.00
Explanation:
Total = 700 → No discount applies.
Test Case 3:
Input:
prices = [600, 500]  
is_member = False
Output:
1045.00
Explanation:
•	Total = 1100
•	Not a member → skip 10%
•	Apply 5% discount → 1100 × 0.95 = 1045.00
'''


def calculate_final_bill(prices, is_member):
    total_amount = sum(prices)
    if is_member:
        total_amount = total_amount * 0.9
    if total_amount > 1000:
        total_amount = total_amount * 0.95
    return round(total_amount, 2)