'''
    Name Of The Program: word repetition game
    Author Of The Program:mahidhar
    Purpose Of The Program:To print a given word multiple times based on the number entered by the user, displaying each repetition on a new line.
    Date On Which The Program Is Written:07-04-2026 
    Description Of The Program (In My Own Words):The program takes a word and a number as input, then uses a loop to print the word repeatedly on separate lines.
    Expected Input And Expected Outputs:
        Case 1:
              Expected Input:
              Enter any word :
              Hello world!
              Enter the number :
              4

              Expected Output:
              Hello world!

              Hello world!

              Hello world!

              Hello world!
        Case 2:
              Expected Input:
              Enter any word :
              JAI HIND!!
              Enter the number :
              7

              Expected Output:
              JAI HIND!!

              JAI HIND!!

              JAI HIND!!

              JAI HIND!!

              JAI HIND!!

              JAI HIND!!

              JAI HIND!!
    Conclusion: The program successfully displays the entered word multiple times in a clear, line-by-line format based on user input.
'''




Word = str(input("Enter any word : \n"))

num = int(input("Enter the number : \n"))

#result = Word * num

for i in range(num):
    print("\n",Word)