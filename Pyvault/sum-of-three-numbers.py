'''
    Name Of The Program:sum of three numbers
    Author Of The Program:mahidhar
    Purpose Of The Program:To take three numbers as input from the user and calculate their sum.
    Date On Which The Program Is Written:06-04-2026 
    Description Of The Program (In My Own Words):A simple Python program that reads three numbers from the user and displays their total sum.
    Expected Input And Expected Outputs:
        Case 1:
              Expected Input:
              Enter the Number-1 : 1
              Enter the Number-2 : 2
              Enter the Number-3 : 3


              Expected Output:
              Sum of three numbers =  6

        Case 2:
              Expected Input:
              Enter the Number-1 : 10
              Enter the Number-2 : 20
              Enter the Number-3 : 30
              
              Expected Output:
              Sum of three numbers =  60
        Case 3:
              Expected Input:
              Enter the Number-1 : 100
              Enter the Number-2 : 200
              Enter the Number-3 : 2



              Expected Output:
              Sum of three numbers =  302
    Conclusion:
    The program successfully adds three user-input numbers and displays the result.
'''



Num1 = int(input("Enter the Number-1 : "))
Num2 = int (input("Enter the Number-2 : "))
Num3 = int (input("Enter the Number-3 : "))

sum = Num1 + Num2 + Num3

print("\nSum of three numbers = ",sum)
    