"""
    Name Of The Program:Digit Occurrence Counter
    Author Of The Program:mahidhar
    Purpose Of The Program:To count how many times a given digit appears in a range of numbers.
    Date On Which The Program Is Written:24-04-2026
    Description Of The Program (In My Own Words):This program takes three inputs: a digit (n1) and two numbers (n2 and n3). It checks each number in the given range and counts how many times the digit appears in all those numbers by separating digits using modulus and division.
    Expected Input And Expected Outputs:
        Case 1:
              Expected Input:
              Enter number-1 : 6
              Enter number-2 : 60
              Enter number-3 : 69

              Expected Output:
              11
        Case 2:
              Expected Input:
              Enter number-1 : 9
              Enter number-2 : 97
              Enter number-3 : 98

              Expected Output:
              2
    Conclusion:The program successfully counts the total occurrences of a digit within a specified range using loops and basic arithmetic operations.
"""



n1 = int(input("Enter number-1 : "))
n2 = int(input("Enter number-2 : "))
n3 = int(input("Enter number-3 : "))

c=0

for u in range(n2,n3+1):
    i=u
    while i>0:
        if n1==i%10:
            c = c+1
        i= i//10
print(c)
    