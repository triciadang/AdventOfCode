def day10():
    f = open("input10.txt", "r")
    flines = f.readlines()

    pathFinder(flines)

def pathFinder(lines):
    fullArray = []
    sArrayPos = -1
    sInArrayPos = -1
    for i in range(0,len(lines)):
        temp_line = lines[i].strip("\n")
        if 'S' in temp_line:
            sArrayPos = i
            sInArrayPos = temp_line.index('S')
        fullArray.append(temp_line)

    sReached = False
    startingPoint = sArrayPos
    startingInArrayPoint = sInArrayPos
    prevStartingPoint = -1
    prevStartingInArrayPoint = -1
    prevPrevStartingInArrayPoint = -1
    prevPrevStartingPoint = -1
    counter = 0

    while sReached == False:

        if startingPoint-1 < 0:
            abovePos = None
        else:
            abovePos = fullArray[startingPoint-1][startingInArrayPoint]

        if startingInArrayPoint-1 < 0:
            leftPos = None
        else:
            leftPos = fullArray[startingPoint][startingInArrayPoint-1]
        
        if startingInArrayPoint+1 >= len(temp_line):
            rightPos = None
        else:
            rightPos = fullArray[startingPoint][startingInArrayPoint+1]

        if startingPoint+1 >= len(fullArray):
            belowPos = None
        else:
            belowPos = fullArray[startingPoint+1][startingInArrayPoint]
        
        nextPipeFound = False

        #check above
        if abovePos is not None and abovePos != "." and nextPipeFound == False:
            teststartingPoint,teststartingInArrayPoint,nextPipeFound = findNextPos(abovePos,"N",startingPoint,startingInArrayPoint)
            if teststartingPoint == prevPrevStartingPoint and teststartingInArrayPoint == prevPrevStartingInArrayPoint:
                nextPipeFound = False

            print("a")
            
        #check left
        if leftPos is not None and leftPos != "." and nextPipeFound == False:
            teststartingPoint,teststartingInArrayPoint,nextPipeFound = findNextPos(leftPos,"W",startingPoint,startingInArrayPoint)
            if teststartingPoint == prevPrevStartingPoint and teststartingInArrayPoint == prevPrevStartingInArrayPoint:
                nextPipeFound = False
            print("b")

        #check right
        if rightPos is not None and rightPos != "." and nextPipeFound == False:
            teststartingPoint,teststartingInArrayPoint,nextPipeFound = findNextPos(rightPos,"E",startingPoint,startingInArrayPoint)
            if teststartingPoint == prevPrevStartingPoint and teststartingInArrayPoint == prevPrevStartingInArrayPoint:
                nextPipeFound = False
            print("c")

        #check below
        if belowPos is not None and belowPos != "." and nextPipeFound == False:
            teststartingPoint,teststartingInArrayPoint,nextPipeFound = findNextPos(belowPos,"S",startingPoint,startingInArrayPoint)
            if teststartingPoint == prevPrevStartingPoint and teststartingInArrayPoint == prevPrevStartingInArrayPoint:
                nextPipeFound = False
            print("D")

        counter += 1
        print("===")
        prevPrevStartingPoint = prevStartingPoint
        prevPrevStartingInArrayPoint = prevStartingInArrayPoint
        prevStartingPoint = teststartingPoint
        prevStartingInArrayPoint = teststartingInArrayPoint
        startingPoint = teststartingPoint
        startingInArrayPoint = teststartingInArrayPoint
        print(startingPoint)
        print(startingInArrayPoint)
        
        currentChar = fullArray[startingPoint][startingInArrayPoint]
        if currentChar == "S":
            print(counter)
            sReached =True





def findNextPos(char,direction,startingPoint,InArrayPos):
    found = True
    if char == "|" and direction == "S":
        startingPoint = startingPoint - 1
        InArrayPos = InArrayPos
    elif char == "|" and direction == "N":
        startingPoint = startingPoint + 1
        InArrayPos = InArrayPos
    elif char == "-" and direction == "E":
        startingPoint = startingPoint
        InArrayPos = InArrayPos + 1
    elif char == "-" and direction == "W":
        startingPoint = startingPoint
        InArrayPos = InArrayPos - 1
    elif char == "L" and direction == "S":
        startingPoint = startingPoint + 1
        InArrayPos = InArrayPos + 1
    elif char == "L" and direction == "W":
        startingPoint = startingPoint - 1
        InArrayPos = InArrayPos - 1
    elif char == "J" and direction == "S":
        startingPoint = startingPoint + 1
        InArrayPos = InArrayPos - 1
    elif char == "J" and direction == "E":
        startingPoint = startingPoint - 1
        InArrayPos = InArrayPos + 1
    elif char == "7" and direction == "N":
        startingPoint = startingPoint-1
        InArrayPos = InArrayPos - 1
    elif char == "7" and direction == "E":
        startingPoint = startingPoint + 1
        InArrayPos = InArrayPos + 1
    elif char == "F" and direction == "N":
        startingPoint = startingPoint - 1
        InArrayPos = InArrayPos + 1
    elif char == "F" and direction == "W":
        startingPoint = startingPoint + 1
        InArrayPos = InArrayPos - 1
    else:
        found = False

    return startingPoint, InArrayPos, found



day10()






def checkAround(i,j,partOfPathArray,fullArray,rowLength):
    isSurroundedByLoop = True
    #check above
    temp_i = i
    temp_j = j
    while temp_i >= 0:
        if partOfPathArray[temp_i-1][temp_j] == True:
            break
        else:
            if fullArray[temp_i-1][temp_j] == ".":
                temp_i = temp_i - 1

            else:
                isSurroundedByLoop = False
                break

    
    #check right
    temp_i = i
    temp_j = j
    while temp_j < rowLength-1 and isSurroundedByLoop == True:
        if partOfPathArray[temp_i][temp_j+1] == True:
            break
        else:
            if fullArray[temp_i][temp_j+1] == ".":
                temp_j = temp_j + 1

            else:
                isSurroundedByLoop = False
                break

    
    #check left
    temp_i = i
    temp_j = j
    while temp_j >= 0 and isSurroundedByLoop == True:
        if partOfPathArray[temp_i][temp_j-1] == True:
            break
        else:
            if fullArray[temp_i][temp_j-1] == ".":
                temp_j = temp_j - 1

            else:
                isSurroundedByLoop = False
                break

    
    #check down
    temp_i = i
    temp_j = j
    while temp_i < len(fullArray)-1 and isSurroundedByLoop == True:
        if partOfPathArray[temp_i+1][temp_j] == True:
            break
        else:
            if fullArray[temp_i+1][temp_j] == ".":
                temp_i = temp_i + 1

            else:
                isSurroundedByLoop = False
                break

    return isSurroundedByLoop


def checkAround(i,j,partOfPathArray,fullArray,rowLength):
    isSurroundedByLoop = True
    #check above
    temp_i = i
    temp_j = j

    if partOfPathArray[temp_i-1][temp_j] != True:
        if fullArray[temp_i-1][temp_j] == "." and temp_i >= 0:
            temp_i = temp_i - 1
        else:
            isSurroundedByLoop = False

    #check right
    temp_i = i
    temp_j = j

    if partOfPathArray[temp_i][temp_j+1] != True:
        if fullArray[temp_i][temp_j+1] == "." and temp_j < rowLength-1 and isSurroundedByLoop == True:
            temp_j = temp_j + 1
        else:
            isSurroundedByLoop = False

    #check left
    temp_i = i
    temp_j = j
    if partOfPathArray[temp_i][temp_j-1] != True:
        if fullArray[temp_i][temp_j-1] == "." and temp_j >= 0 and isSurroundedByLoop == True:
            temp_j = temp_j - 1
        else:
            isSurroundedByLoop = False
            
    #check down
    temp_i = i
    temp_j = j
    if partOfPathArray[temp_i+1][temp_j] != True:
        if fullArray[temp_i+1][temp_j] == "." and temp_i < len(fullArray)-1 and isSurroundedByLoop == True:
            temp_i = temp_i + 1
        else:
            isSurroundedByLoop = False

    return isSurroundedByLoop



def checkUp(i,j,partOfPathArray,fullArray,rowLength):
    isSurroundedByLoop = True
    #check above
    temp_i = i
    temp_j = j

    if partOfPathArray[temp_i-1][temp_j] != True:
        if fullArray[temp_i-1][temp_j] == "." and temp_i >= 0:
            temp_i = temp_i - 1
        else:
            isSurroundedByLoop = False

    return temp_i,temp_j,isSurroundedByLoop

