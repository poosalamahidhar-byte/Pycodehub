"""
    Name Of The Program:Sum of Even Series
    Author Of The Program:mahidhar
    Purpose Of The Program:To calculate and display the sum of all even numbers up to the given number (n).
    Date On Which The Program Is Written:25-04-2026
    Description Of The Program (In My Own Words):The program takes a number as input, generates even numbers starting from 2 up to that number, adds them, and displays the total sum.
    Expected Input And Expected Outputs:
        Case 1:
              Expected Input:
              Enter number : 12

              Expected Output:
              Sum =  42
        Case 2:
              Expected Input:
              Enter number : 0

              Expected Output:
              Sum =  0
    Conclusion:Thus, the program successfully calculates and displays the sum of even numbers up to the given number.
"""




n = int(input("Enter number : "))
sum = 0
i = 2

while i<=n:
    sum = sum + i
    i = i+2
print("\nSum = ",sum)
    