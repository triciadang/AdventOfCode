import numpy as np

def day16():
    f = open("input16.txt","r")
    flines = f.readlines()
    calculateTiles(flines)


def calculateTiles(lines):
    fullArray = []

    for i in range(0,len(lines)):
        temp_line = lines[i].strip("\n")
        temp_line = list(temp_line)
        lineLength = len(temp_line)
        fullArray += [temp_line]

    print(fullArray)

    highestCount = -1

    # i = 0
    # j = 0
    # dir = "E"

    for i in range(0,len(fullArray)):
        #if 0,0 corner
        if i == 0:
            dir = "S"
            energizedArray = np.full((len(fullArray),lineLength),"")
            energizedArray = followPath(fullArray,i,0,dir,lineLength,energizedArray)

            count = getCount(energizedArray)
            if count > highestCount:
                highestCount = count

            dir = "E"
            energizedArray = np.full((len(fullArray),lineLength),"")
            energizedArray = followPath(fullArray,i,0,dir,lineLength,energizedArray)

            count = getCount(energizedArray)
            if count > highestCount:
                highestCount = count

            #if 0,end corner
            dir = "W"
            energizedArray = np.full((len(fullArray),lineLength),"")
            energizedArray = followPath(fullArray,i,lineLength-1,dir,lineLength,energizedArray)
            count = getCount(energizedArray)
            if count > highestCount:
                highestCount = count

            dir = "S"
            energizedArray = np.full((len(fullArray),lineLength),"")
            energizedArray = followPath(fullArray,i,lineLength-1,dir,lineLength,energizedArray)
            count = getCount(energizedArray)
            if count > highestCount:
                highestCount = count

            
        #if bottom corners
        if i == len(fullArray)-1:

            #bottom left
            dir = "N"
            energizedArray = np.full((len(fullArray),lineLength),"")
            energizedArray = followPath(fullArray,i,0,dir,lineLength,energizedArray)
            count = getCount(energizedArray)
            if count > highestCount:
                highestCount = count

            dir = "E"
            energizedArray = np.full((len(fullArray),lineLength),"")
            energizedArray = followPath(fullArray,i,0,dir,lineLength,energizedArray)
            count = getCount(energizedArray)
            if count > highestCount:
                highestCount = count

            #bottom right
            dir = "W"
            energizedArray = np.full((len(fullArray),lineLength),"")
            energizedArray = followPath(fullArray,i,lineLength-1,dir,lineLength,energizedArray)
            count = getCount(energizedArray)
            if count > highestCount:
                highestCount = count

            dir = "N"
            energizedArray = np.full((len(fullArray),lineLength),"")
            energizedArray = followPath(fullArray,i,lineLength-1,dir,lineLength,energizedArray)
            count = getCount(energizedArray)
            if count > highestCount:
                highestCount = count
            
        else:
            #left side
            dir = "E"
            energizedArray = np.full((len(fullArray),lineLength),"")
            energizedArray = followPath(fullArray,i,0,dir,lineLength,energizedArray)
            count = getCount(energizedArray)
            if count > highestCount:
                highestCount = count

            #right side
            dir = "W"
            energizedArray = np.full((len(fullArray),lineLength),"")
            energizedArray = followPath(fullArray,i,lineLength-1,dir,lineLength,energizedArray)
            count = getCount(energizedArray)
            if count > highestCount:
                highestCount = count

        
    for j in range(1,lineLength-1):
        dir = "S"
        energizedArray = np.full((len(fullArray),lineLength),"")
        energizedArray = followPath(fullArray,0,j,dir,lineLength,energizedArray)
        count = getCount(energizedArray)
        if count > highestCount:
            highestCount = count

        dir = "N"
        energizedArray = np.full((len(fullArray),lineLength),"")
        energizedArray = followPath(fullArray,len(fullArray)-1,j,dir,lineLength,energizedArray)
        count = getCount(energizedArray)
        if count > highestCount:
            highestCount = count


    print(highestCount)

def getCount(energizedArray):
    count = 0
    for each_row in energizedArray:
        for each_col in each_row:
            if each_col != "":
                count += 1
    return count

def printArray(array):
    for each in array:
        print(each)


def followPath(fullArray,i,j,dir,lineLength,energizedArray):
    
    while i >= 0 and i < len(fullArray) and j >=0 and j<lineLength:
        currentChar = fullArray[i][j]
        #we already traced this
        if dir in energizedArray[i][j]:
            return energizedArray
        else:
            energizedArray[i][j] += dir
            # printArray(energizedArray)
            # print("====")

        if currentChar == ".":
            if dir == "E":
                j += 1
            elif dir == "N":
                i -= 1
            elif dir == "S":
                i += 1
            elif dir == "W":
                j -= 1
        elif currentChar == "/":
            if dir == "E":
                i -= 1
                dir = "N"
            elif dir == "N":
                j += 1
                dir = "E"
            elif dir == "S":
                j -= 1
                dir = "W"
            elif dir == "W":
                i += 1
                dir = "S"
        elif currentChar == "\\":
            if dir == "E":
                i += 1
                dir = "S"
            elif dir == "N":
                j -= 1
                dir = "W"
            elif dir == "S":
                j += 1
                dir = "E"
            elif dir == "W":
                i -= 1
                dir = "N"
        elif currentChar == "|":
            if dir == "E":
                energizedArray = followPath(fullArray,i-1,j,"N",lineLength,energizedArray)
                # energizedArray = followPath(fullArray,i+1,j,"S",lineLength,energizedArray)
                i += 1
                dir = "S"
            elif dir == "W":
                energizedArray = followPath(fullArray,i-1,j,"N",lineLength,energizedArray)
                # energizedArray = followPath(fullArray,i+1,j,"S",lineLength,energizedArray)
                i += 1
                dir = "S"
            elif dir == "N":
                i -= 1
            elif dir == "S":
                i += 1
        elif currentChar == "-":
            if dir == "E":
                j += 1
            elif dir == "W":
                j -= 1
            elif dir == "N":
                energizedArray = followPath(fullArray,i,j-1,"W",lineLength,energizedArray)
                # energizedArray = followPath(fullArray,i,j+1,"E",lineLength,energizedArray)
                j += 1
                dir = "E"
            elif dir == "S":
                energizedArray = followPath(fullArray,i,j-1,"W",lineLength,energizedArray)
                # energizedArray = followPath(fullArray,i,j+1,"E",lineLength,energizedArray)
                j += 1
                dir = "E"

    return energizedArray


day16()
