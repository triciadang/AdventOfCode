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
        lineLength = len(temp_line)
        fullArray += [temp_line]

    print(fullArray)

    drawDiagram(fullArray)

def drawDiagram(fullArray):
    startingCoordX = 0
    startingCoordY = 0
    coords = []
    total_length = 0
    coords.append([startingCoordX,startingCoordY])
    startingCoordX = 1
    startingCoordY = 0
    coords.append([startingCoordX,startingCoordY])
    
    for i in range(len(fullArray)-1,-1,-1):
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

    newCoords = []
    for each in coords:
        xCoord = each[0] + 1
        yCoord = each[1] + 1
        newCoords.append([xCoord,yCoord])

    xs, ys = zip(*coords) #create lists of x and y values

    plt.figure()
    plt.plot(xs,ys) 
    plt.show()


    pgon = Polygon(coords) # Assuming the OP's x,y coordinates

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

# coord = [[1,1], [2,1], [2,2], [1,2], [0.5,1.5]]
# coord.append(coord[0]) #repeat the first point to create a 'closed loop'

# xs, ys = zip(*coord) #create lists of x and y values

# plt.figure()
# plt.plot(xs,ys) 
# plt.show()