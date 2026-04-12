"""
    Name Of The Program:Swap Two Numbers Without Temporary Variable
    Author Of The Program:mahidhar
    Purpose Of The Program:To interchange (swap) the values of two numbers entered by the user without using a temporary variable.
    Date On Which The Program Is Written:12-04-2026
    Description Of The Program (In My Own Words):This program takes two numbers as input from the user, swaps their values using Python’s multiple assignment feature, and then displays the updated (exchanged) values.
    Expected Input And Expected Outputs:
        Case 1:
              Expected Input:
              Enter Number-1 : 737
              Enter Number-2 : 7473

              Expected Output:
              After exchanging the values :-
              
              Num1 :  7473
              Num2 :  737
        Case 2:
              Expected Input:
              Enter Number-1 : 1
              Enter Number-2 : 2

              Expected Output:
              After exchanging the values :-

              Num1 :  2
              Num2 :  1
        Case 3:
              Expected Input:
              Enter Number-1 : 0
              Enter Number-2 : 7

              Expected Output:
              After exchanging the values :-

              Num1 :  7
              Num2 :  0

    Conclusion:
    The program efficiently swaps two numbers in a simple and concise way, demonstrating Python’s ability to exchange values without using an extra variable.
"""




num1 = int(input("Enter Number-1 : "))
num2 = int(input("Enter Number-2 : "))

num1,num2 = num2,num1

print("\nAfter exchanging the values :- \n")

print("Num1 : ",num1)
print("Num2 : ",num2)
