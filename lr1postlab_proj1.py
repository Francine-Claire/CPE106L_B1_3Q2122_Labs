def GetMode(listNum):
    if len(listNum) == 0:
        return 0
    else:
        freqNum = {}
        for num in listNum:
            hold = freqNum.get(num, None)
            if hold == None:
                freqNum[num] = 1
            else:
                freqNum[num] = hold + 1
        highestFreq = max(freqNum.values())
        for highFreqNum in freqNum:
            if freqNum[highFreqNum] == highestFreq:
                return highFreqNum

def GetMedian(listNum):
    if len(listNum) == 0:
        return 0
    else:
        listNum.sort()
        midpoint = len(listNum) // 2
        if len(listNum) % 2 == 1:
            return listNum[midpoint]
        else:
            return (listNum[midpoint] + listNum[midpoint-1]) / 2

def GetMean(listNum):
    if len(listNum) == 0:
        return 0
    else:
        sum = 0
        for i in listNum:
            sum += i
        return sum/len(listNum)

def main():
    print("Enter numbers in the list and enter a character or string when finished")
    try:
        listNum = []
        while True:
            listNum.append(int(input()))
    except:
        print("The List is as follows: ")
        if len(listNum) == 0:
            print("0 or EMPTY")
        else:
            for y in listNum:
                print(y)
    print("\n")

    mode = GetMode(listNum)
    median = GetMedian(listNum)
    mean = GetMean(listNum)
    
    print("The Mode in the list is: " + str(mode))
    print("The Median in the list is: " + str(median))
    print("The Mean in the list is: " + str(mean))
main()