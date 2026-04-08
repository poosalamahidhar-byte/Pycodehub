'''
    Name Of The Program:Number sign checker
    Author Of The Program:mahidhar
    Purpose Of The Program:To check whether the number entered by the user is positive, negative, or zero.
    Date On Which The Program Is Written:08-04-2026
    Description Of The Program (In My Own Words):This program takes a number from the user and uses if-elif-else conditions to determine whether the number is positive, negative, or zero, then displays the result.
    Expected Input And Expected Outputs:
        Case 1:
              Expected Input:
              Enter any number : 4

              Expected Output:
              Entered number is a positive number

        Case 2:
              Expected Input:
              Enter any number : -100


              Expected Output:
              Entered number is a negative number
        Case 3:
              Expected Input:
              Enter any number : 0

              Expected Output:
              Entered number is 0(zero)

    Conclusion:
    The program successfully identifies whether the entered number is positive, negative, or zero using conditional statements.
'''



num = int(input("Enter any number : "))

if num > 0:
    print("Entered number is a positive number")
elif num < 0:
    print("Entered number is a negative number")
else:
    print("Entered number is 0(zero)")