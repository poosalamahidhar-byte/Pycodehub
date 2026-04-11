'''
    Name Of The Program:Character Type Identifier
    Author Of The Program:mahidhar
    Purpose Of The Program:To identify and display the type of input entered by the user (digit, lowercase, uppercase, or special character).
    Date On Which The Program Is Written:11-04-2026
    Description Of The Program (In My Own Words):This program takes a user input and checks whether it is a digit, lowercase letter, uppercase letter, or a special character using built-in string methods, then displays the corresponding result.
    Expected Input And Expected Outputs:
        Case 1:
              Expected Input:
              s

              Expected Output:
              Entered a Lowercase character!

        Case 2:
              Expected Input:
              U


              Expected Output:
              Entered a Uppercase character!
        Case 3:
              Expected Input:
              @


              Expected Output:
              Entered a Special character!
    Conclusion:
    The program successfully classifies user input into different types and displays the appropriate message based on its category.
'''



s = str(input())

if s.isdigit():
    print("You Entered a digit!")
elif s.islower():
    print("Entered a Lowercase character!")
elif s.isupper():
    print("Entered a Uppercase character!")
else:
    print("Entered a Special character!")