"""
    Name Of The Program:palindrome checker
    Author Of The Program:mahidhar
    Purpose Of The Program:To identify palindromes easily with this program
    Date On Which The Program Is Written:29-04-2026
    Description Of The Program (In My Own Words):This program checks if the given input string is a palindrome by comparing it with its reverse and prints "True" or "False".
    Expected Input And Expected Outputs:
        Case 1:
              Expected Input:
              madam
              
              Expected Output:
              True
        Case 2:
              Expected Input:
              level

              Expected Output:
              True
        Case 3:
              Expected Input:
              lakh

              Expected Output:
              False
    Conclusion:The program successfully determines whether a given string is a palindrome and displays the result as "True" or "False".
"""







def palindrome(s):
    if s == s[::-1]:
        return "True"
    else:
        return "False"
s = input()
print(palindrome(s))