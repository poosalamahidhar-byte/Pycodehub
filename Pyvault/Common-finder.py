"""
    Name Of The Program:common finder
    Author Of The Program:mahidhar
    Purpose Of The Program:To find and display the common elements between two lists without duplicates.
    Date On Which The Program Is Written:28-04-2026
    Description Of The Program (In My Own Words):This program takes two lists of numbers as input from the user. It compares both lists and identifies the elements that are present in both. It ensures that each common element is included only once in the result and then prints the final list of common elements.
    Expected Input And Expected Outputs:
        Case 1:
              Expected Input:
              1,2,3,4,5,6
              3,6,5,9,0,1

              Expected Output:
              [1, 3, 5, 6]
        Case 2:
              Expected Input:
              79,4,30,12,8
              30,12,90,58


              Expected Output:
              [30, 12]
    Conclusion:The program successfully finds the unique common elements between two lists and displays them in a simple and efficient way.
"""




a = list(map(int, input().split(',')))
b = list(map(int, input().split(',')))

result = []

for i in a:
    if i in b and i not in result:
        result.append(i)
print(result)