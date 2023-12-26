import numpy as np
import threading

def day23():
    f = open("input23.txt","r")
    flines = f.readlines()
    findPaths(flines)

def printArray(array):
    for each in array:
        print(each)

def findPaths(lines):
    fullArray = []

    for i in range(0,len(lines)):
        temp_line = list(lines[i].strip("\n"))

        fullArray.append(temp_line)

    startPosX = 0
    startPosY = 1
    currentDist = 0
    currentDir = "S"
    maxDistance = -1
    energizedArray = np.copy(fullArray)
    multiplePaths = [[currentDist,startPosX,startPosY,currentDir,energizedArray]]

    while len(multiplePaths) != 0:

        currentDist = multiplePaths[0][0]
        startPosX = multiplePaths[0][1]
        startPosY = multiplePaths[0][2]
        currentDir = multiplePaths[0][3]
        energizedArray = multiplePaths[0][4]

        if startPosX != len(fullArray)-1 or startPosY != len(fullArray[0])-2:
            multiplePaths.pop(0)
            # multiplePaths += doPathFinding(fullArray,startPosX,startPosY,currentDist,currentDir)
            multiplePaths += doPathFindingDos(startPosX,startPosY,currentDist,currentDir,energizedArray)
        else:
            multiplePaths.pop(0)
            print(currentDist)
            if currentDist > maxDistance:
                maxDistance = currentDist
    print(maxDistance)


def doPathFindingDos(startPosX,startPosY,currentDist,currentDir,energizedArray):
    
    multiplePaths = []
    newX,newY = 0,0
    newDir = None
    #check north
    if startPosX - 1 > 0:
        currentChar = energizedArray[startPosX-1][startPosY]
        if currentChar != "#" and currentDir != "S" and currentChar != "O":
            newX,newY,newDir = getNextPositionDos(currentChar,startPosX,startPosY,"N")
            tempEnergizedArray1 = np.copy(energizedArray)
            tempEnergizedArray1[newX][newY] = "O"
            multiplePaths.append([currentDist+1,newX,newY,newDir,tempEnergizedArray1])
    
    #check south
    if startPosX + 1 < len(energizedArray):
        currentChar = energizedArray[startPosX+1][startPosY]
        if currentChar != "#" and currentDir != "N" and currentChar != "O":
            newX,newY,newDir = getNextPositionDos(currentChar,startPosX,startPosY,"S")
            tempEnergizedArray2 = np.copy(energizedArray)
            tempEnergizedArray2[newX][newY] = "O"
            multiplePaths.append([currentDist+1,newX,newY,newDir,tempEnergizedArray2])

    #check west
    if startPosY - 1 > 0:
        currentChar = energizedArray[startPosX][startPosY-1]
        if currentChar != "#" and currentDir != "E" and currentChar != "O":
            newX,newY,newDir = getNextPositionDos(currentChar,startPosX,startPosY,"W")
            tempEnergizedArray3 = np.copy(energizedArray)
            tempEnergizedArray3[newX][newY] = "O"
            multiplePaths.append([currentDist+1,newX,newY,newDir,tempEnergizedArray3])
    
    #check east
    if startPosX - 1 < len(energizedArray[0]):
        currentChar = energizedArray[startPosX][startPosY+1]
        if currentChar != "#" and currentDir != "W" and currentChar != "O":
            newX,newY,newDir = getNextPositionDos(currentChar,startPosX,startPosY,"E")
            tempEnergizedArray4 = np.copy(energizedArray)
            tempEnergizedArray4[newX][newY] = "O"
            multiplePaths.append([currentDist+1,newX,newY,newDir,tempEnergizedArray4])

    
    return multiplePaths
         

def getNextPositionDos(currentChar,startPosX,startPosY,currentDir):
    if currentDir == "N":
        startPosX -= 1
    elif currentDir == "S":
        startPosX += 1
    elif currentDir == "W":
        startPosY -= 1
    elif currentDir == "E":
        startPosY += 1
    return startPosX,startPosY,currentDir


def doPathFinding(fullArray,startPosX,startPosY,currentDist,currentDir):
    multiplePaths = []
    newX,newY = 0,0
    newDir = None
    #check north
    if startPosX - 1 > 0:
        currentChar = fullArray[startPosX-1][startPosY]
        if currentChar != "#" and currentChar != "v" and currentDir != "S":
            newX,newY,newDir = getNextPosition(currentChar,startPosX,startPosY,"N")

            multiplePaths.append([currentDist+1,newX,newY,newDir])
    
    #check south
    if startPosX + 1 < len(fullArray):
        currentChar = fullArray[startPosX+1][startPosY]
        if currentChar != "#" and currentChar != "^" and currentDir != "N":
            newX,newY,newDir = getNextPosition(currentChar,startPosX,startPosY,"S")

            multiplePaths.append([currentDist+1,newX,newY,newDir])

    #check west
    if startPosY - 1 > 0:
        currentChar = fullArray[startPosX][startPosY-1]
        if currentChar != "#" and currentChar != ">" and currentDir != "E":
            newX,newY,newDir = getNextPosition(currentChar,startPosX,startPosY,"W")

            multiplePaths.append([currentDist+1,newX,newY,newDir])
    
    #check east
    if startPosX - 1 < len(fullArray[0]):
        currentChar = fullArray[startPosX][startPosY+1]
        if currentChar != "#" and currentChar != "<" and currentDir != "W":
            newX,newY,newDir = getNextPosition(currentChar,startPosX,startPosY,"E")

            multiplePaths.append([currentDist+1,newX,newY,newDir])

    
    return multiplePaths
         

def getNextPosition(currentChar,startPosX,startPosY,currentDir):
    if currentChar == ">":
        startPosY += 1
        currentDir = "E"
    elif currentChar == "<":
        startPosY -= 1
        currentDir = "W"
    elif currentChar == "^":
        startPosX -= 1
        currentDir = "N"
    elif currentChar == "v":
        startPosX += 1
        currentDir = "S"
    elif currentDir == "N":
        startPosX -= 1
    elif currentDir == "S":
        startPosX += 1
    elif currentDir == "W":
        startPosY -= 1
    elif currentDir == "E":
        startPosY += 1
    return startPosX,startPosY,currentDir

day23()