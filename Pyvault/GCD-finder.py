"""
    Name Of The Program:GCD Finder
    Author Of The Program:mahidhar
    Purpose Of The Program:To calculate the greatest common divisor (GCD) of two numbers using the Euclidean algorithm.
    Date On Which The Program Is Written:05-05-2026
    Description Of The Program (In My Own Words):This program takes two non-zero integers as input and uses the Euclidean algorithm (repeated division) to find their greatest common divisor (GCD). It ensures that zero values are not accepted and outputs the final GCD.
    Expected Input And Expected Outputs:
        Case 1:
              Expected Input:
              x : 0

              y : 50

              Expected Output:
              Value must be non zero!
        Case 2:
              Expected Input:
              x : 75

              y : 15

              Expected Output:
              gcd :  15
    Conclusion:The program efficiently finds the GCD of two numbers using a simple and reliable method, ensuring accurate results for valid inputs.
"""




x = int(input("x : "))
y = int(input("\ny : "))

if x == 0 or y == 0:
    print("\nValue must be non zero!")
else:
    while y!=0:
        r = x%y
        x = y
        y = r
    print("\ngcd : ",x)