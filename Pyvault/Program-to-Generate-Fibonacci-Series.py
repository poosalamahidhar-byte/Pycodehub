"""

Name Of The Program:
Fibonacci Series Generator

Author Of The Program:
mahidhar

Purpose Of The Program:
To generate and display the Fibonacci series up to a given number of terms entered by the user.

Date On Which The Program Is Written:
17 April 2026

Description Of The Program (In My Own Words):
This program takes the number of terms as input from the user and prints the Fibonacci series. 
The Fibonacci series starts with 0 and 1, and each next number is the sum of the previous two numbers. 
The program uses a loop to calculate and display each term in the sequence.

Expected Input And Expected Outputs:

    Case 1:
        Expected Input:
        Enter number of terms : 5

        Expected Output:
        0 1 1 2 3

    Case 2:
        Expected Input:
        Enter number of terms : 1

        Expected Output:
        0

    Case 3:
        Expected Input:
        Enter number of terms : 7

        Expected Output:
        0 1 1 2 3 5 8

Conclusion:
The program successfully generates the Fibonacci series using a simple loop and variable swapping method. 
It helps in understanding basic programming concepts like loops, variables, and sequence generation.
"""





n = int(input("Enter number of terms : "))

t1 = 0
t2 = 1
for i in range (n):
    print(t1,end = " ")
    nt = t1+t2
    t1 = t2
    t2 = nt