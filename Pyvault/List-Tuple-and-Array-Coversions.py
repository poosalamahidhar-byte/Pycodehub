"""
    Name Of The Program:List, Tuple and Array Conversion
    Author Of The Program:mahidhar
    Purpose Of The Program:To read list and tuple inputs and convert them into arrays.
    Date On Which The Program Is Written:22-07-2026
    Description Of The Program (In My Own Words):This program accepts integer inputs as a list and a tuple, converts both into Python arrays using the array module, and displays the original and converted data.
    Expected Input And Expected Outputs:
        Case 1:
              Expected Input:
              0 1 2 3 4
              5 6 7 8 9

              Expected Output:
              [0, 1, 2, 3, 4]
              (5, 6, 7, 8, 9)
              array('i', [0, 1, 2, 3, 4])
              array('i', [5, 6, 7, 8, 9])
        
    Conclusion:The program demonstrates how to convert lists and tuples into arrays and print the results.
"""






import array

list_input = list(map(int,input().split()))

tuple_input = tuple(map(int,input().split()))

list_from_array = array.array('i',list_input)

tuple_from_array = array.array('i',tuple_input)

print(list_input)

print(tuple_input)

print(list_from_array)

print(tuple_from_array)