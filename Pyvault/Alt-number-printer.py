"""
    Name Of The Program:Alt Number Printer
    Author Of The Program:mahidhar
    Purpose Of The Program:To print alternate numbers within a user-defined range based on the chosen starting value.
    Date On Which The Program Is Written:04-05-2026
    Description Of The Program (In My Own Words):This program takes starting and ending values from the user and prints numbers at an interval of 2, generating an alternate sequence (even or odd) based on the starting number.
    Expected Input And Expected Outputs:
        Case 1:
              Expected Input:
              Enter starting  number : 0

              Enter ending  number : 20

              Expected Output:
              0

              2

              4

              6

              8

              10

              12

              14

              16

              18

              20
        Case 2:
              Expected Input:
              Enter starting  number : 7

              Enter ending  number : 17
              
              Expected Output:
              7

              9

              11

              13

              15

              17
        Case 3:
              Expected Input:
              Enter starting  number : 5

              Enter ending  number : 13

              Expected Output:
              5

              7

              9

              11

              13
    Conclusion:The program efficiently generates and displays alternate numbers within a given range based on user input.
"""





start = int(input("Enter starting  number : "))

end = int(input("\nEnter ending  number : "))

for i in range(start,end+1,2):
    print("\n",i)