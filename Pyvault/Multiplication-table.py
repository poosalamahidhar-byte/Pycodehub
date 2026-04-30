"""
    Name Of The Program:multiplication table
    Author Of The Program:mahidhar
    Purpose Of The Program:To generate and display the multiplication table of a given number up to a specified number of rows, with a maximum limit of 20 rows.
    Date On Which The Program Is Written:30-04-2026
    Description Of The Program (In My Own Words):This program takes a number and a row limit as input, then prints its multiplication table. If the given row limit exceeds 20, it restricts the output to 20 rows.
    Expected Input And Expected Outputs:
        Case 1:
              Expected Input:
              Enter number : 2
              Enter number of rows : 10

              Expected Output:
              2 * 1 = 2
              2 * 2 = 4
              2 * 3 = 6
              2 * 4 = 8
              2 * 5 = 10
              2 * 6 = 12
              2 * 7 = 14
              2 * 8 = 16
              2 * 9 = 18
              2 * 10 = 20
        Case 2:
              Expected Input:
              Enter number : 17
              Enter number of rows : 4

              Expected Output:
              17 * 1 = 17
              17 * 2 = 34
              17 * 3 = 51
              17 * 4 = 68
    Conclusion:The program successfully generates a multiplication table while enforcing a maximum row limit, ensuring correct and controlled output.
"""



x = int(input("Enter number : "))
y = int(input("Enter number of rows : "))

if y<=20:
    for i in range(1,y+1):
        print(f"{x} * {i} = {x * i}")
else:
    print("Rows are limited to 20")
    
    for i in range(1,21):
        print(f"{x} * {i} = {x * i}")