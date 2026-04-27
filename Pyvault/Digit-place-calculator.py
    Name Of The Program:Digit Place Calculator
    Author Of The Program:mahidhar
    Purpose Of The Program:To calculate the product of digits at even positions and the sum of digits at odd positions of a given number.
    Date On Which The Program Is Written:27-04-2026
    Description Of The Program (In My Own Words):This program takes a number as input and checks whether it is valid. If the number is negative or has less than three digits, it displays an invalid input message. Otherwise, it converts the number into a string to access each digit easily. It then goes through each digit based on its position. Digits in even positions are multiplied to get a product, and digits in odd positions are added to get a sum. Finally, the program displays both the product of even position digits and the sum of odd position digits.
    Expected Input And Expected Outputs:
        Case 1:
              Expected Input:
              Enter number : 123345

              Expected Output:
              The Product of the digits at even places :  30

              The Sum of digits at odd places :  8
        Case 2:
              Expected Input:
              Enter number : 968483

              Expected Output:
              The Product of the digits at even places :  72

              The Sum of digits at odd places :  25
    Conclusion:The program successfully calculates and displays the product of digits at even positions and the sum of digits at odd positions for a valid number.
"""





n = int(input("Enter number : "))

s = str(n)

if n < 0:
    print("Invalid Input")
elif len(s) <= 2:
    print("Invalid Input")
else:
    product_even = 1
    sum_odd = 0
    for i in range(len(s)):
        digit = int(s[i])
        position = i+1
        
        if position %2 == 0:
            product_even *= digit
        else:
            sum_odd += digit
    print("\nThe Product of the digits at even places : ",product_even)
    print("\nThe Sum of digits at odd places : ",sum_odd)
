"""
    Name Of The Program:Digit Place Calculator
    Author Of The Program:mahidhar
    Purpose Of The Program:To calculate the product of digits at even positions and the sum of digits at odd positions of a given number.
    Date On Which The Program Is Written:27-04-2026
    Description Of The Program (In My Own Words):This program takes a number as input and checks whether it is valid. If the number is negative or has less than three digits, it displays an invalid input message. Otherwise, it converts the number into a string to access each digit easily. It then goes through each digit based on its position. Digits in even positions are multiplied to get a product, and digits in odd positions are added to get a sum. Finally, the program displays both the product of even position digits and the sum of odd position digits.
    Expected Input And Expected Outputs:
        Case 1:
              Expected Input:
              Enter number : 123345

              Expected Output:
              The Product of the digits at even places :  30

              The Sum of digits at odd places :  8
        Case 2:
              Expected Input:
              Enter number : 968483

              Expected Output:
              The Product of the digits at even places :  72

              The Sum of digits at odd places :  25
    Conclusion:The program successfully calculates and displays the product of digits at even positions and the sum of digits at odd positions for a valid number.
"""





n = int(input("Enter number : "))

s = str(n)

if n < 0:
    print("Invalid Input")
elif len(s) <= 2:
    print("Invalid Input")
else:
    product_even = 1
    sum_odd = 0
    for i in range(len(s)):
        digit = int(s[i])
        position = i+1
        
        if position %2 == 0:
            product_even *= digit
        else:
            sum_odd += digit
    print("\nThe Product of the digits at even places : ",product_even)
    print("\nThe Sum of digits at odd places : ",sum_odd)
    
