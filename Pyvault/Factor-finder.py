"""
    Name Of The Program:Factor Finder
    Author Of The Program:mahidhar
    Purpose Of The Program:Finds and prints all factors of a given number.
    Date On Which The Program Is Written:20-04-2026
    Description Of The Program (In My Own Words):This program takes an integer input from the user and checks each number from 1 up to the given number. If a number divides the input exactly, it is printed as a factor.
    Expected Input And Expected Outputs:
        Case 1:
              Expected Input:
              Enter number : 3
              
              Expected Output:
              1 3
              
        Case 2:
              Expected Input:
              Enter number : 6

              Expected Output:
              1 2 3 6

        Case 3:
              Expected Input:
              Enter number : 12


              Expected Output:
              1 2 3 4 6 12
    Conclusion:The program successfully identifies and prints all the factors of a number using a loop and conditional checking.
"""




n = int(input("Enter number : "))
i = 1

while i<=n:
    if n%i==0:
        print(i,end = " ")
    i+=1