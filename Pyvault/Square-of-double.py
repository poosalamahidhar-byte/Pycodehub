"""
    Name Of The Program:Square Of Double
    Author Of The Program:mahidhar
    Purpose Of The Program:To calculate the square of a number after doubling it.
    Date On Which The Program Is Written:06-05-2026
    Description Of The Program (In My Own Words):This program takes a number as input, doubles it using a function, and then squares the result using another function. The final output displays the squared value of the doubled number.
    Expected Input And Expected Outputs:
        Case 1:
              Expected Input:
              Enter the number : 10

              Expected Output:
              double,squaring the number :  400
        Case 2:
              Expected Input:
              Enter the number : 13

              Expected Output:
              double,squaring the number :  676
        Case 3:
              Expected Input:
              Enter the number : 5

              Expected Output:
              double,squaring the number :  100
    Conclusion:The program demonstrates function usage by performing operations step-by-step, making the code simple, reusable, and easy to understand.
"""


def square(x):
    return x*x

def double(x):
    return 2*x
    
n = int (input("Enter the number : "))

print("\ndouble,squaring the number : ",square(double(n)))

