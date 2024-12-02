def day14():
    f = open("input14.txt","r")
    flines = f.readlines()
    calculateLoad(flines)


def calculateLoad(lines):
    fullArray = []
    total = 0
    for i in range(0,len(lines)):
        temp_line = lines[i].strip("\n")
        temp_line = list(temp_line)
        lineLength = len(temp_line)
        fullArray += [temp_line]

    # newFullArray = shiftNorth(fullArray,lineLength)
    # total = calculateLoadWeight(newFullArray,lineLength)

    allLoads = {}
    for z in range(0,1000):
        fullArray = doCycle(fullArray,lineLength)
        # printArray(fullArray)
        print(z)
        
        result = calculateLoadWeight(fullArray,lineLength)
        print(result)
        print("===")
        if result not in allLoads:
            allLoads[result] = [z]
        else:
            allLoads[result] += [z]

    for each in allLoads:
        print(each)
        print(allLoads[each])

    return


def printArray(fullArray):
    for each in fullArray:
        print(each)
    return


def doCycle(fullArray,lineLength):
    nCycle = shiftNorth(fullArray,lineLength)
    # printArray(nCycle)

    wCycle = shiftWest(nCycle,lineLength)
    # printArray(wCycle)

    sCycle = shiftSouth(wCycle,lineLength)
    # printArray(sCycle)

    eCycle = shiftEast(sCycle,lineLength)
    # printArray(eCycle)

    return eCycle


def shiftNorth(fullArray,lineLength):
    for i in range(0,len(fullArray)):
        for j in range(0,lineLength):
            if fullArray[i][j] == "O":
                #check if # before
                temp_i = i
                while fullArray[temp_i-1][j] == "." and temp_i >= 1:
                    fullArray[temp_i-1][j] = "O"
                    fullArray[temp_i][j] = "."
                    temp_i -= 1
                    if temp_i == 0:
                        break
    return fullArray


def shiftWest(fullArray,lineLength):
    for i in range(0,len(fullArray)):
        for j in range(0,lineLength):
            if fullArray[i][j] == "O":
                #check if # before
                temp_j = j
                while fullArray[i][temp_j-1] == "." and temp_j >= 1:
                    fullArray[i][temp_j-1] = "O"
                    fullArray[i][temp_j] = "."
                    temp_j -= 1
                    if temp_j == 0:
                        break
    return fullArray

def shiftEast(fullArray,lineLength):
    for i in range(0,len(fullArray)):
        for j in range(lineLength-2,-1,-1):
            if fullArray[i][j] == "O":
                #check if # before
                temp_j = j
                while fullArray[i][temp_j+1] == "." and temp_j <= lineLength-1:
                    fullArray[i][temp_j+1] = "O"
                    fullArray[i][temp_j] = "."
                    temp_j += 1
                    if temp_j == lineLength-1:
                        break
    return fullArray

def shiftSouth(fullArray,lineLength):
    for i in range(len(fullArray)-2,-1,-1):
        for j in range(0,lineLength):
            if fullArray[i][j] == "O":
                #check if # before
                temp_i = i
                while fullArray[temp_i+1][j] == "." and temp_i <= len(fullArray)-1:
                    fullArray[temp_i+1][j] = "O"
                    fullArray[temp_i][j] = "."
                    temp_i += 1
                    if temp_i == len(fullArray)-1:
                        break
    return fullArray

def calculateLoadWeight(fullArray,lineLength):
    rowNumber = len(fullArray)
    total = 0
    for i in range(0,len(fullArray)):
        for j in range(0,lineLength):
            if fullArray[i][j] == "O":
                total += rowNumber
        rowNumber -= 1
    return total

day14()
