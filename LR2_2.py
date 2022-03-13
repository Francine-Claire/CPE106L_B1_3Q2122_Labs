#PUNZALAN, FRANCINE CLAIRE (TARRA)
#CPE106L-B1 - GROUP 3
#LABORATORY 2 (POST-LAB PROBLEM)

"""

2. Filename: LR2_2.py
Write a program that allows the user to navigate the lines of text in a file. The program
should prompt the user for a filename and input the lines of text into a list. The program
then enters a loop in which it prints the number of lines in the file and prompts the user
for a line number. Actual line numbers range from 1 to the number of lines in the file. If
the input is 0, the program quits. Otherwise, the program prints the line associated with
that number.

"""

#Prompt the user to enter input file name
inputfile = input("Enter the input file name: ")

#Open the file for reading
file = open(inputfile, 'r')

#Create an empty list
linecount = 0

#Loop read the content of input file line by line and
#store each line into variable 'line' until the end of input file
for line in file:
    linecount = linecount + 1

 #Print total number of lines in file   
print("The file has",linecount,"lines.")
while True:
    linenum = 0

    #Prompt and read line number from file
    num = int(input("Enter a line number or enter 0 to exit the program: "))
    if num >=1 and num <= linecount:
        file = open(inputfile, 'r')
        for lines in file:
            linenum = linenum + 1
            if linenum == num:
                
                #Print content of line desired by user
                print(num,":",lines)
    elif num == 0:

        #Close file
        break
    else:
        if num!= linecount:
            print("ERROR: line number must be less than",linecount)