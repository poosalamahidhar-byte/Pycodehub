'''
    Name Of The Program:Reverse number pattern printer
    Author Of The Program:mahidhar
    Purpose Of The Program:To print a reverse number pattern based on the number entered by the user.
    Date On Which The Program Is Written:10-04-2026
    Description Of The Program (In My Own Words):This Python program takes a number n as input from the user. It uses nested for loops to print numbers in a decreasing order pattern. Each row prints the same number multiple times, increasing the count as the rows go down.
    Expected Input And Expected Outputs:
        Case 1:
              Expected Input:
              Enter a number : 3


              Expected Output:
              3
              2 2
              1 1 1
        Case 2:
              Expected Input:
              Enter a number : 5


              Expected Output:
              5
              4 4
              3 3 3
              2 2 2 2
              1 1 1 1 1
    Conclusion:
    The program demonstrates the use of nested loops and pattern printing in Python to generate a reverse numeric pattern.
'''




n = int(input("Enter a number : "))

for i in range(n,0,-1):
    for j in range(n-i+1):
        print(i,end = " ")
    print()


