"""
    Name Of The Program:Leap Year Checker
    Author Of The Program:mahidhar
    Purpose Of The Program:To check whether a given year is a leap year or not.
    Date On Which The Program Is Written:16-04-2026
    Description Of The Program (In My Own Words):This program takes a year as input from the user and uses conditional statements to determine if it satisfies leap year conditions (divisible by 400, 100, or 4). It then displays whether the year is a leap year or not.
    Expected Input And Expected Outputs:
        Case 1:
              Expected Input:
              Enter year : 1947

              Expected Output:
              The Entered year is not a leap year!

        Case 2:
              Expected Input:
              Enter year : 2013

              Expected Output:
              The Entered year is not a leap year
        Case 3:
              Expected Input:
              Enter year : 2012
              
              Expected Output:
              The Entered year is a leap year!
    Conclusion:The program correctly identifies leap years based on standard rules and helps in understanding conditional logic in Python.
"""




year = int(input("Enter year : "))

if year%400 == 0:
    print("\nThe Entered year is a leap year!")
elif year%100 == 0:
    print("\nThe Entered year is not a leap year!")
elif year%4 == 0:
    print("\nThe Entered year is a leap year!")
else:
    print("\nThe Entered year is not a leap year!")
    