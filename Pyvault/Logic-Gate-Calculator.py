"""
    Name Of The Program:Logic Gate Calculator
    Author Of The Program:mahidhar
    Purpose Of The Program:To perform basic logic gate operations using Boolean inputs.
    Date On Which The Program Is Written:23-07-2026
    Description Of The Program (In My Own Words):This Python program accepts two binary inputs (0 or 1), converts them into Boolean values, and performs the basic logic gate operations: AND, OR, NOT (for both inputs), and XOR. It then displays the result of each logic gate operation.
    Expected Input And Expected Outputs:
        Case 1:
              Expected Input:
              0
              1
              
              Expected Output:
              AND GATE:False
              OR GATE:True
              NOT GATE FOR A:True
              NOT GATE FOR B:False
              XOR GATE:True
       
        Case 2:
              Expected Input:
              1
              1
              Expected Output:
              AND GATE:True
              OR GATE:True
              NOT GATE FOR A:False
              NOT GATE FOR B:False
              XOR GATE:False
        
    Conclusion:This program demonstrates the working of basic logic gates using Boolean operations in Python and helps understand fundamental digital logic concepts.
"""


A = bool(int(input()))

B = bool(int(input()))

and_gate = A and B

or_gate = A or B

not_a = not A

not_b = not B

xor_gate = A!=B

print(f"AND GATE:{and_gate}")

print(f"OR GATE:{or_gate}")

print(f"NOT GATE FOR A:{not_a}")

print(f"NOT GATE FOR B:{not_b}")

print(f"XOR GATE:{xor_gate}")


