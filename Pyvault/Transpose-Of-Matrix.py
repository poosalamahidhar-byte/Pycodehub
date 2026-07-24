"""
    Name Of The Program:Transpose-of-Matrix
    Author Of The Program:mahidhar
    Purpose Of The Program:To read a matrix from the user and display its transpose using NumPy.
    Date On Which The Program Is Written:24-07-2026
    Description Of The Program (In My Own Words):This program accepts a matrix as input, uses NumPy's transpose() function to swap its rows and columns, and prints the transposed matrix.
    Expected Input And Expected Outputs:
        Case 1:
              Expected Input:
              2
              3
              1 2 3
              4 5 6

              Expected Output:
              result:
              1 4 
              2 5
              3 6
              
    Conclusion:The program successfully transposes a matrix and displays the result.
*/

"""


import numpy as np

r = int(input())

c = int(input())

matrix = []

for _ in range(r):
    matrix.append(list(map(int,input().split())))
transposed_matrix = np.transpose(matrix)

print("result:")

for row in transposed_matrix :
    print(" ".join(map(str,row)))