"""
    Name Of The Program:Word Concatenation Program
    Author Of The Program:mahidhar
    Purpose Of The Program:To take two words from the user and combine them into a single word.
    Date On Which The Program Is Written:14-04-2026
    Description Of The Program (In My Own Words):This program takes two words as input from the user, combines them into one string, and displays the result.
    Expected Input And Expected Outputs:
        Case 1:
              Expected Input:
              Enter word1 : Pyt
              
              Enter word2 : hon

              Expected Output:
              combined_word =  Python
        Case 2:
              Expected Input:
              Enter word1 : data

              Enter word2 : structure

              Expected Output:
              combined_word =  datastructure
    Conclusion:
    The program successfully combines two user-input words and displays the merged result in a simple and clear way.
"""



word1 = str(input("Enter word1 : "))
word2 = str(input("\nEnter word2 : "))

combined_word = word1+word2

print("\ncombined_word = ",combined_word)