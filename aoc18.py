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
    
    for each_instr in fullArray:
        dir = each_instr[0]
        length = each_instr[1]
        print(int(length))
        total_length += int(length)

        if dir == "R":
            startingCoordX += int(length)+1
        elif dir == "L":
            startingCoordX -= int(length)+1
        elif dir == "U":
            startingCoordY += int(length)+1
        elif dir == "D":
            startingCoordY -= int(length)+1

        print(startingCoordX)
        print(startingCoordY)
        coords.append([startingCoordX,startingCoordY])

    newCoords = []
    for each in coords:
        xCoord = each[0] + 1
        yCoord = each[1] + 1
        newCoords.append([xCoord,yCoord])

    print(coords)
    xs, ys = zip(*coords) #create lists of x and y values

    plt.figure()
    plt.plot(xs,ys) 
    plt.show()


    pgon = Polygon(coords) # Assuming the OP's x,y coordinates

    print(pgon.area)
    print(total_length)
            


day18()

# coord = [[1,1], [2,1], [2,2], [1,2], [0.5,1.5]]
# coord.append(coord[0]) #repeat the first point to create a 'closed loop'

# xs, ys = zip(*coord) #create lists of x and y values

# plt.figure()
# plt.plot(xs,ys) 
# plt.show()