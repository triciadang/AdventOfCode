import numpy as np
import math
from shapely.geometry import Polygon,Point
import geopandas as gpd
import matplotlib.pyplot as plt

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
        rowLength = len(temp_line)
        if 'S' in temp_line:
            sArrayPos = i
            sInArrayPos = temp_line.index('S')
    
        fullArray.append(temp_line)

    partOfPathArray = np.full(shape=(len(fullArray), len(temp_line)),fill_value="F")

    sFound = False
    startingPoint = sArrayPos
    startingInArrayPoint = sInArrayPos

    prevDir,nextDir = findFirstDir(fullArray,sArrayPos,sInArrayPos,rowLength)
    currentOne = "X"
    count = -1

    polygonArray = []

    while sFound == False: 
        count += 1

        newPoint = []

        if currentOne == "S":
            sFound = True
        else:
            if prevDir == "N":
                startingPoint = startingPoint - 1
                currentOne = fullArray[startingPoint][startingInArrayPoint]
            if prevDir == "E":
                startingInArrayPoint += 1
                currentOne = fullArray[startingPoint][startingInArrayPoint]
            if prevDir == "W":
                startingInArrayPoint -= 1
                currentOne = fullArray[startingPoint][startingInArrayPoint]
            if prevDir == "S":
                startingPoint += 1
                currentOne = fullArray[startingPoint][startingInArrayPoint]
            newPoint += startingPoint,startingInArrayPoint
            polygonArray.append(newPoint)
            partOfPathArray[startingPoint][startingInArrayPoint] = "P"
            nextDir,found = findNextPos(currentOne,prevDir)
            prevDir = nextDir

    print("Maximum Distance:")
    print(count/2)

    poly1 = Polygon(polygonArray)
    myPoly = gpd.GeoSeries([poly1])
    myPoly.plot()
    plt.show()

    numberOfTiles = 0
    for j in range(0,len(partOfPathArray)):
        for k in range(0,rowLength):
            if partOfPathArray[j][k] == "F":
                p1 = Point(j,k)
                if p1.within(poly1):
                    numberOfTiles += 1

    
    # print(rowLength)

    # #do outside
    # for j in range(0, rowLength):
    #     # print(j)
    #     if partOfPathArray[0][j] == "F":
    #         partOfPathArray[0][j] = "N"
    #     if partOfPathArray[-1][j] == "F":
    #         partOfPathArray[-1][j] = "N"
        
    # for i in range(0,len(fullArray)):
    #     # print(i)
    #     if partOfPathArray[i][0] == "F":
    #         partOfPathArray[i][0] = "N"
    #     if partOfPathArray[i][rowLength-1] == "F":
    #         partOfPathArray[i][rowLength-1] = "N"

    # # print(partOfPathArray)

    # k = 1
    # # print(math.ceil(len(fullArray)/2))
    # while k < math.ceil(len(fullArray)/2):
    #     for j in range(0, rowLength):
    #         if partOfPathArray[k][j] == "F":
    #             if checkAround(k,j,partOfPathArray):
    #                 partOfPathArray[k][j] = "N"
    #         if partOfPathArray[-1-k][j] == "F":
    #             if checkAround(-1-k,j,partOfPathArray):
    #                 partOfPathArray[-1-k][j] = "N"
    #     k += 1

    # # print(partOfPathArray)
    # # print()
    # k = 1
    # while k < math.ceil(len(fullArray)/2):
    #     for j in range(rowLength-1, -1,-1):
    #         if partOfPathArray[k][j] == "F":
    #             if checkAround(k,j,partOfPathArray):
    #                 partOfPathArray[k][j] = "N"
    #         if partOfPathArray[-1-k][j] == "F":
    #             if checkAround(-1-k,j,partOfPathArray):
    #                 partOfPathArray[-1-k][j] = "N"
    #     k += 1
            
    # for each_line in partOfPathArray:
    #     for each_row in each_line:
    #         if each_row == "F":
    #             numberOfTiles += 1

    # # print(partOfPathArray)
    print(numberOfTiles)


def checkAround(i,j,partOfPathArray):
    #check above
    temp_i = i
    temp_j = j

    if partOfPathArray[temp_i-1][temp_j] == "N":
        return True

    #check right
    temp_i = i
    temp_j = j

    if partOfPathArray[temp_i][temp_j+1] == "N":
        return True

    #check left
    temp_i = i
    temp_j = j
    if partOfPathArray[temp_i][temp_j-1] == "N":
        return True
            
    #check down
    if partOfPathArray[temp_i+1][temp_j] == "N":
        return True

    return False


def findFirstDir(fullArray,startingPoint,startingInArrayPoint,length):
    length = 20
    prevDir = "X"

    if startingPoint-1 < 0:
        abovePos = None
    else:
        abovePos = fullArray[startingPoint-1][startingInArrayPoint]

    if startingInArrayPoint-1 < 0:
        leftPos = None
    else:
        leftPos = fullArray[startingPoint][startingInArrayPoint-1]

    if startingInArrayPoint+1 >= length:
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
        nextDir,nextPipeFound = findNextPos(abovePos,"N")
        prevDir = "N"
        
    #check left
    if leftPos is not None and leftPos != "." and nextPipeFound == False:
        nextDir,nextPipeFound = findNextPos(leftPos,"W")
        prevDir = "W"

    #check right
    if rightPos is not None and rightPos != "." and nextPipeFound == False:
        nextDir,nextPipeFound = findNextPos(rightPos,"E")
        prevDir = "E"

    #check below
    if belowPos is not None and belowPos != "." and nextPipeFound == False:
        nextDir,nextPipeFound = findNextPos(belowPos,"S")
        prevDir = "S"

    return prevDir, nextDir


def findNextPos(char,direction):
    found = True
    if char == "|" and direction == "S":
        nextDir = "S"
    elif char == "|" and direction == "N":
        nextDir = "N"
    elif char == "-" and direction == "E":
        nextDir = "E"
    elif char == "-" and direction == "W":
        nextDir = "W"
    elif char == "L" and direction == "S":
        nextDir = "E"
    elif char == "L" and direction == "W":
        nextDir = "N"
    elif char == "J" and direction == "S":
        nextDir = "W"
    elif char == "J" and direction == "E":
        nextDir = "N"
    elif char == "7" and direction == "N":
        nextDir = "W"
    elif char == "7" and direction == "E":
        nextDir = "S"
    elif char == "F" and direction == "N":
        nextDir = "E"
    elif char == "F" and direction == "W":
        nextDir = "S"
    else:
        nextDir = "X"
        found = False

    return nextDir,found



day10()