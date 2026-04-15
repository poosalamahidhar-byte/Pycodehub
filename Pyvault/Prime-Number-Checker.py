"""
    Name Of The Program:Prime Number Checker (Using While Loop)
    Author Of The Program:mahidhar
    Purpose Of The Program:To check whether a given number is prime or not using a while loop.
    Date On Which The Program Is Written:15-04-2026
    Description Of The Program (In My Own Words):This program takes a number as input and checks whether it is divisible by any number from 2 to half of the number. If a divisor is found, it prints "Not a prime"; otherwise, it prints "Prime".
    Expected Input And Expected Outputs:
        Case 1:
              Expected Input:
              Eneter any number : 7654

              Expected Output:
              Entered number is not a prime
        Case 2:
              Expected Input:
              Eneter any number : 97

              Expected Output:
              Entered number is a prime
        Case 3:
              Expected Input:
              Eneter any number : 83

              Expected Output:
              Entered number is a prime
    Conclusion:The program successfully determines whether a number is prime by checking its divisibility and gives the correct result.
"""



n = int(input("Eneter any number : "))

i,c=2,0

while i<=n//2:
    if n%i == 0:
     c=c+1
    i+=1

if c==0:
    print("\nEntered number is a prime")
else:
    print("\nEntered number is not a prime")
    