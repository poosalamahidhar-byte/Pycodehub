"""
    Name Of The Program:Even Position Cube Sum
    Author Of The Program:mahidhar 
    Purpose Of The Program:To calculate the sum of cubes of digits present at even positions in a given number.
    Date On Which The Program Is Written:26-04-2026 
    Description Of The Program (In My Own Words):The program takes an integer input from the user. If the number is negative, it prints "Invalid". Otherwise, it converts the number into a string to access each digit. It then checks each digit’s position (starting from 1). If the position is even, it calculates the cube of that digit and adds it to a total. Finally, it prints the sum.
    Expected Input And Expected Outputs:
        Case 1:
              Expected Input:
              Enter number : 36789

              Expected Output:
              728
        Case 2:
              Expected Input:
              Enter number : 5458

              Expected Output:
              576
        Case 3:
              Expected Input:
              Enter number : 5799653

              Expected Output:
              1197
    Conclusion:This program demonstrates how to work with digits of a number using loops, conditions, and type conversion. It also shows how to apply mathematical operations based on position.
"""




n = int(input("Enter number : "))

if n < 0: 
    print("Invalid")
else:
    s = str(n)
    i = 0
    total = 0
    while i < len(s):
        if (i+1) % 2 == 0:
            digit = int(s[i])
            total+=digit**3
        i = i+1
    print("\n",total)