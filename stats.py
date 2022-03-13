#GOPOLE, KHYLE MATTHEW (PABLO)
#CPE106L-B1 - GROUP 3
#LABORATORY 2 (POST-LAB PROBLEM)


"""
1. Filename: stats.py

A group of statisticians at a local college has asked you to create a set 
of functions that compute the median and mode of a set of numbers, as 
defined in the below sample programs: 

· mode.py 
· median.py

Define these functions in a module named stats.py. 
Also include a function named mean, which computes the average of a set 
of numbers. Each function should expect a list of numbers as an argument 
and return a single number. Each function should return 0 if the list is empty. 
Include a main function that tests the three statistical functions with a given list

"""
#define function for Mode

def GetMode(listNum):
    #Return 0 if list is empty
    if len(listNum) == 0:
        return 0
    else:
        #initialize list for the occurrence of each element in listNum
        freqNum = {}
        #traverse the list to check the occurrences
        for num in listNum:
            #initialize hold variable for conditional purposes
            hold = freqNum.get(num, None)
            #condition for the first occurrence
            if hold == None:
                freqNum[num] = 1
            else:
                #if not first occurence, add for annother occurrence
                freqNum[num] = hold + 1
        #initialize occurrence values
        highestFreq = max(freqNum.values())
        #traverse list to check which number in the list had the most occurrence
        for highFreqNum in freqNum:
            if freqNum[highFreqNum] == highestFreq:
                return highFreqNum


#define function for Median
def GetMedian(listNum):
    #Return 0 if list is empty
    if len(listNum) == 0:
        return 0
    else:
        #sort the list first in ascending order
        listNum.sort()
        #check midpoint by checking first if the number of elements in the list is an even number
        midpoint = len(listNum) // 2

        if len(listNum) % 2 == 1:
            #if yes, return the median
            return listNum[midpoint]
        else:
            #if not, add the two consecutive midpoint and divide by 2 to get the median
            return (listNum[midpoint] + listNum[midpoint-1]) / 2


#define function for Mean
def GetMean(listNum):
    #Return 0 if list is empty
    if len(listNum) == 0:
        return 0
    else:
        #initialize sum equal to zero
        sum = 0
        #traverse the list by adding all elements one by one
        for i in listNum:
            sum += i

        #return the mean
        return sum/len(listNum)


#define main
def main():

    #use given list below if you do not want user-input list but comment out try block and except block
    #listNum = [11, 12, 13, 14, 15, 16, 17, 16, 20, 21]
    print("Enter numbers in the list and enter a character or string when finished")

    #try block for exception purposes and will serve as control value for the loop
    try:
        #initialize empty list
        listNum = []

        while True:
            #continuously input numbers from the user until a character or string gets entered
            listNum.append(int(input()))
    except:
        #print the elements in the list again
        print("The List is as follows: ")
        if len(listNum) == 0:
            #print 0 if the list is empty
            print("0 or EMPTY")
        else:
            for y in listNum:
                print(y)

    print("\n")

    #initialize variables for the returning values of functions
    mode = GetMode(listNum)
    median = GetMedian(listNum)
    mean = GetMean(listNum)


    #print the values and convert the returning values to string
    print("The Mode in the list is: " + str(mode))
    print("The Median in the list is: " + str(median))
    print("The Mean in the list is: " + str(mean))


#CALL MAIN TO EXECUTE
main()

#END 04/12/2022

