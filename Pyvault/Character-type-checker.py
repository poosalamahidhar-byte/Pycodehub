"""
    Name Of The Program:Character Type Checker
    Author Of The Program:mahidhar
    Purpose Of The Program:To identify whether the entered character is a digit, letter, or neither.
    Date On Which The Program Is Written:13-04-2026
    Description Of The Program (In My Own Words):This program takes a single character as input from the user and uses built-in string methods to determine its type. It checks if the character is a digit, an alphabet letter, or a special character, and displays the result accordingly.
    Expected Input And Expected Outputs:
        Case 1:
              Expected Input:
              Enter any character : 7

              Expected Output:
              Entered character is a digit!
        Case 2:
              Expected Input:
              Enter any character : r

              Expected Output:
              Entered character is a letter!
        Case 3:
              Expected Input:
              Enter any character : !

              Expected Output:
              Enterd character is nither a letter nor a digit!

    Conclusion:The program effectively classifies a character using simple conditions and built-in functions, making it easy to understand and useful for basic input validation.
"""





ch = input("Enter any character : ")

if ch.isdigit():
    print("\nEntered character is a digit!")
elif ch.isalpha():
    print("\nEntered character is a letter!")
else:
    print("\nEnterd character is nither a letter nor a digit!")