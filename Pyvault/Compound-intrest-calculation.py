"""
    Name Of The Program:Compound-intrest-calculation
    Author Of The Program:mahidhar
    Purpose Of The Program:To calculate compound interest very easily.
    Date On Which The Program Is Written:21-07-2026
    Description Of The Program (In My Own Words):This program takes the principal amount, rate of interest, and time as input, calculates the compound amount using the compound interest formula, and displays the result with two decimal places.
    Expected Input And Expected Outputs:
        Case 1:
              Expected Input:
              1000
              5
              2
              Expected Output:
              1102.50
        Case 2:
              Expected Input:
              5000
              3
              1
              Expected Output:
              5150.00
    Conclusion:The program successfully calculates and displays the compound amount.
"""


p = float(input())

r = float(input())

t = float(input())

ci = p*(1+r/100)**t

print(f"{ci:.2f}")