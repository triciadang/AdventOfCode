import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from shapely.geometry import Polygon

def day18():
    f = open("input18.txt","r")
    flines = f.readlines()
    calculateLava(flines)


def calculateLava(lines):
    fullArray = []

    for i in range(0,len(lines)):
        temp_line = lines[i].strip("\n")
        temp_line = temp_line.split()
        fullArray += [temp_line]

    # drawDiagram(fullArray)
    drawDiagram2(fullArray)

def drawDiagram2(fullArray):
    startingCoordX = 0
    startingCoordY = 0
    coords = []
    total_length = 0
    coords.append([startingCoordX,startingCoordY])
    
    for i in range(0,len(fullArray)):

        lengthPart = fullArray[i][2][2:7]
        length = int(lengthPart,16)
        total_length += int(length)
        dir = fullArray[i][2][-2]
        if dir == "0":
            startingCoordX += length
        elif dir == "2":
            startingCoordX -= length
        elif dir == "3":
            startingCoordY += length
        elif dir == "1":
            startingCoordY -= length

        coords.append([startingCoordX,startingCoordY])

    print(coords)
    pgon = Polygon(coords) # Assuming the OP's x,y coordinates

    print(pgon.area)
    print(total_length)

    insideArea = pickTheorem(pgon.area,total_length)
    print(insideArea)

    totalArea = total_length+insideArea
    print(totalArea)


def drawDiagram(fullArray):
    startingCoordX = 0
    startingCoordY = 0
    coords = []
    total_length = 0
    coords.append([startingCoordX,startingCoordY])
    
    for i in range(0,len(fullArray)):
        dir = fullArray[i][0]
        length = fullArray[i][1]
        total_length += int(length)

        if dir == "R":
            startingCoordX += int(length)
        elif dir == "L":
            startingCoordX -= int(length)
        elif dir == "U":
            startingCoordY += int(length)
        elif dir == "D":
            startingCoordY -= int(length)

        coords.append([startingCoordX,startingCoordY])

    xs, ys = zip(*coords)

    plt.figure()
    plt.plot(xs,ys) 
    plt.show()


    pgon = Polygon(coords)

    print(pgon.area)
    print(total_length)

    insideArea = pickTheorem(pgon.area,total_length)
    print(insideArea)

    totalArea = total_length+insideArea
    print(totalArea)



def pickTheorem(area,boundary):
    insidePoints = area - (.5*boundary) +1
    return insidePoints

            


day18()