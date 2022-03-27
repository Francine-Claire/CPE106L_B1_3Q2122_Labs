#PUNZALAN, FRANCINE CLAIRE (TARRA)
#CPE106L-B1 - GROUP 3
#LABORATORY 3 (POST-LAB PROBLEM - PROJECT 2 (Lambert Book p. 349) )

"""
PROJECTS

2. This project assumes that you have completed Project 1. 
Place several Student objects into a list and shuffle it. 
Then run the sort method with this list and dis- play all of the students information.

"""



"""
File: student.py
Resources to manage a student's name and test scores.
"""

class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name
  
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
   
    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self._scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)
 
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))
    
    #ADDED METHODS
    #All 3 Methods will accept two names as their parameters for conditional purposes

    def __eq__(self, student):
        return self.name==student.name
    
    def __lt__(self, student):
        return self.name<student.name
    
    def __ge__(self, student):
        return self.name>=student.name

def main():

    """
    #A simple test.
    student = Student("Ken", 5)
    print(student)
    for i in range(1, 6):
        student.setScore(i, 100)
    print(student)
    """
    #Declare and Initialize Class Methods for Testing

    student = Student("John", 11)
    print(student)
    for i in range(1, 6):
        student.setScore(i, 100)

    print("\nStudent 1: ")
    print(student)
    student2 = Student('John', 8)
    print("\nStudent 2:")
    print(student2)
    
    print("\nTesting Equality Method\nComparing Student 1 and Student 2")
    #Case 1 - Equal
    print(student==student2)

    print("Testing Less Than Method\nComparing Student 1 and Student 2")
    #Case 2 - Less Than
    print(student<student2)

    print("Testing Greater Than or Equal Method\nComparing Student 1 and Student 2")
    #Case 3 - Greater Than
    print(student>=student2)

    """Tests sorting."""
    #Create the list.
    list = []

    #Place the 5 students into the list using for loop.
    for count in reversed(range(5)):
        s = Student("Name" + str(count + 1), 10)
        list.append(s)

    #Complete the definition of the main function.
    print("\nSorted list of students:")

    #Using the import statement random, shuffle the list.
    import random
    random.shuffle(list)

    #sort() method is used to sort the list.
    list.sort()

    #Display the student list.
    for obj in list:
        print(obj.__str__())

#Execute Main to Check Outputs
if __name__ == "__main__":
    main()


