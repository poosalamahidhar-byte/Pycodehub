"""
    Name Of The Program:Even or Odd Checker
    Author Of The Program:mahidhar
    Purpose Of The Program:To determine whether a given number is even or odd
    Date On Which The Program Is Written:17-04-2026
    Description Of The Program (In My Own Words):This program takes an integer input from the user and checks if it is divisible by 2. If the number is divisible by 2, it prints that the number is even; otherwise, it prints that the number is odd.
    Expected Input And Expected Outputs:
        Case 1:
              Expected Input:
              Enter any number : 2

              Expected Output:
              Entered number is even number
        Case 2:
              Expected Input:
              Enter any number : 72727

              Expected Output:
              Entered number is odd number
        Case 3:
              Expected Input:
              Enter any number : 0
              
              Expected Output:
              Entered number is even number
    Conclusion:The program successfully identifies whether a number is even or odd using a simple conditional statement.
"""




n = int(input("Enter any number : "))

if n % 2 == 0:
    print("\nEntered number is even number")
else:
    print("\nEntered number is odd number")

