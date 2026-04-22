"""
    Name Of The Program:Arithmetic Calculator
    Author Of The Program:mahidhar
    Purpose Of The Program:To perform basic arithmetic operations like addition, subtraction, multiplication, division, and modulus based on user input.
    Date On Which The Program Is Written:22-04-2026
    Description Of The Program (In My Own Words):This program takes two numbers and an operator from the user. It then performs the selected arithmetic operation using conditional statements and displays the result. It also handles errors like division or modulus by zero and invalid operator input.
    Expected Input And Expected Outputs:
        Case 1:
              Expected Input:
              Enter Num1 : 1
              Enter Num2 : 2

              Enter an operator (+, -, *, /, %): +

              Expected Output:
              Result: 3.0
        Case 2:
              Expected Input:
              Enter Num1 : 2
              Enter Num2 : 3

              Enter an operator (+, -, *, /, %): *

              Expected Output:
              Result: 6.0
    Conclusion:This program is a simple and user-friendly calculator that demonstrates the use of input handling, conditional statements, and basic error checking in Python.
"""




a = float(input("Enter Num1 : "))
b = float(input("Enter Num2 : "))

op = input("\nEnter an operator (+, -, *, /, %): ")

if op == '+':
    print("\nResult:", a + b)
elif op == '-':
    print("\nResult:", a - b)
elif op == '*':
    print("\nResult:", a * b)
elif op == '/':
    if b != 0:
        print("\nResult:", a / b)
    else:
        print("\nError: Division by zero is not allowed.")
elif op == '%':
    if b != 0:
        print("\nResult:", a % b)
    else:
        print("\nError: Modulus by zero is not allowed.")
else:
    print("\nInvalid operator entered.")