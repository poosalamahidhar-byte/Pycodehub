'''
    Name Of The Program: Greatest of three numbers
    Author Of The Program: mahidhar
    Purpose Of The Program:To find and display the greatest number among three numbers entered by the user.
    Date On Which The Program Is Written:09-04-2026
    Description Of The Program (In My Own Words):This program takes three numbers as input from the user and uses conditional statements (if-elif-else) to compare them and display which number is the greatest.
    Expected Input And Expected Outputs:
        Case 1:
              Expected Input:
              Enter number-1 : 10
              Enter number-2 : 20
              Enter number-3 : 30

              Expected Output:
              Number-3 is greater than the other 2 numbers!

        Case 2:
              Expected Input:
              Enter number-1 : 30
              Enter number-2 : 30
              Enter number-3 : 500

              Expected Output:
              Number-3 is greater than the other 2 numbers!
        Case 3:
              Expected Input:
              Enter number-1 : 1000
              Enter number-2 : 1000
              Enter number-3 : 1000

              Expected Output:
              Given three numbers are equal!
    Conclusion:
    Thus, the program successfully compares three numbers and displays the greatest among them.
'''




num1 = int(input("Enter number-1 : "))
num2 = int(input("Enter number-2 : "))
num3 = int(input("Enter number-3 : "))

if num1>num2 and num1>num3:
    print("Number-1 is greater than the other 2 numbers!")
elif num2>num1 and num2>num3:
    print("Number-2 is greater than the other 2 numbers!")
elif num3>num1 and num3>num2:
    print("Number-3 is greater than the other 2 numbers!")
else:
    print("Given three numbers are equal!")