#Chua, Vhal Pearson & Fonseca, Robne Kyle L. 
#CPE106L-B1 - GROUP 3
#LABORATORY 2 (POST-LAB PROBLEM)

"""
3. Filename: generator_modified.py

Modify the sentence-generator program of Case Study 5.3:

    · METIS book: 9781337671019, page 150. 
    · Python source code: generator.py

so that it inputs its vocabulary from a set of text files at startup. The filenames are 
nouns.txt, verbs. txt, articles.txt, and prepositions.txt. (Hint: Define a single new 
function, getWords. This function should expect a filename as an argument. The 
function should open an input file with this name, define a temporary list, read words 
from the file, and add them to the list. The function should then convert the list to a 
tuple and return this tuple. Call the function with an actual filename to initialize each 
of the four variables for the vocabulary.)

"""

import random


def getWords(name):

    #Opens .txt file
    file=open(name)

    #Creates an empty list
    lst=[]

    #Reads .txt file
    data=file.read()

    #Splits string into list 
    lst=data.split("\n")

    #Returns list into a tuple
    return tuple(lst)

articles=getWords("articles.txt")
nouns=getWords("nouns.txt")
verbs=getWords("verbs.txt")
prepositions=getWords("prepositions.txt")

def sentence():
    """Builds and returns a sentence."""
    return nounPhrase() + " " + verbPhrase()

def nounPhrase():
    """Builds and returns a noun phrase."""
    return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():
    """Builds and returns a verb phrase."""
    return random.choice(verbs) + " " + nounPhrase() + " " + \
           prepositionalPhrase()

def prepositionalPhrase():
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + nounPhrase()

def main():
    """Allows the user to input the number of sentences
    to generate."""
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())

if __name__ == "__main__":
    main()

    