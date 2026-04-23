"""
    Name Of The Program:Sum of First N Numbers
    Author Of The Program:mahidhar
    Purpose Of The Program:To calculate the sum of numbers from 1 up to a given input number.
    Date On Which The Program Is Written:23-04-2026
    Description Of The Program (In My Own Words):This program takes a number as input and calculates the sum of numbers up to that value using a loop.
    Expected Input And Expected Outputs:
        Case 1:
              Expected Input:
              Enter number : 10
              
              Expected Output:
              Sum =  55
        Case 2:
              Expected Input:
              Enter number : 70

              Expected Output:
              Sum =  2485

        Case 3:
              Expected Input:13

              Expected Output:
              Sum = 91
    Conclusion:The program successfully computes the sum of numbers up to the given input using a simple loop.
"""






num = int(input("Enter number : "))

s = 0
i = 0

while(i<=num):
    s = s + i
    i = i + 1
else:
    if num<0:
        while i>=1:
            s = s + i
            i = i - 1

print("\nSum = ",s)
