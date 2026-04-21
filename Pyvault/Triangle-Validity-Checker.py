"""
    Name Of The Program:Triangle Validity Checker
    Author Of The Program:mahidhar
    Purpose Of The Program:To check whether three given sides can form a triangle.
    Date On Which The Program Is Written:21-04-2026
    Description Of The Program (In My Own Words):This program takes three side lengths as input and verifies the triangle inequality rule.
    Expected Input And Expected Outputs:
        Case 1:
              Expected Input:
              Enter side1 : 60
              Enter side : 90
              Enter side3 : 40
              
              Expected Output:
              It form a trinagle

        Case 2:
              Expected Input:
              Enter side1 : 20
              Enter side : 40
              Enter side3 : 60

              Expected Output:
              It doesn't form a trinagle
    Conclusion:If all three conditions are satisfied, a triangle is possible; otherwise, it is not.
"""





s1 = int(input("Enter side1 : "))
s2 = int(input("Enter side2 : "))
s3 = int(input("Enter side3 : "))

if s1+s2>s3 and s1+s3>s2 and s2+s3>s1:
    print("\nIt form a triangle")
else:
    print("\nIt doesn't form a triangle")
        
