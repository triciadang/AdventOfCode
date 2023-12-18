import numpy as np
def day11():
    f = open("input11.txt","r")
    flines = f.readlines()
    galaxyDistance(flines)
    
def galaxyDistance(lines):
    galaxyMap = []
    for i in range(0,len(lines)):
        mapArray = lines[i].strip("\n")
        mapArray = list(mapArray)
        lineLength = len(mapArray)
        galaxyMap.append(mapArray)
    expandedGalaxyMap = galaxyMap

    #check each row for all row
    arrayOfEmptyRows = []
    for k in range(0,len(galaxyMap)):
        eachRow = False
        for i in range(0,lineLength):
            if galaxyMap[k][i] != ".":
                eachRow = True
        if eachRow == False:
            arrayOfEmptyRows += [k]
    print(arrayOfEmptyRows)

    #check each column for empty column
    arrayOfEmptyColumns = []
    for i in range (0,lineLength):
        eachColumn = False
        for k in range(0,len(galaxyMap)):
            if galaxyMap[k][i] != ".":
                eachColumn = True
        if eachColumn == False:
            arrayOfEmptyColumns += [i]
    print(arrayOfEmptyColumns)

    # #add in rows to expanded galaxy map
    # emptyRow = []
    # for each in range(0,lineLength):
    #     emptyRow.append(".")
    # for i in range(0,len(arrayOfEmptyRows)):
    #     expandedGalaxyMap.insert(arrayOfEmptyRows[i]+i,emptyRow)

    # #add in columns to expanded galaxy map
    # for i in range(0,len(arrayOfEmptyColumns)):
    #     for j in range(0,len(expandedGalaxyMap)):
    #         expandedGalaxyMap[j].insert(arrayOfEmptyColumns[i]+i,".")

    #put all points into dictionary
    newLineLength = len(expandedGalaxyMap[0])
    pointDict = {}
    k = 0
    for i in range(0,len(expandedGalaxyMap)):
        for j in range(0,newLineLength):
            if expandedGalaxyMap[i][j] == "#":
                print(i,j)
                new_i = i
                new_j = j

                for each_value in arrayOfEmptyRows:
                    if i > each_value:
                        new_i += 999999

                for each_yValue in arrayOfEmptyColumns:
                    if j > each_yValue:
                        new_j += 999999

                print(new_i,new_j)
                pointDict[k] = new_i,new_j
                k += 1
                
    #calculate the shortest path between two points
    print(pointDict)
    distance = 0
    for i in range(0,len(pointDict)):
        for j in range(i+1,len(pointDict)):
            firstx,firsty = pointDict[i]
            secondx,secondy = pointDict[j]
            pointDist = (abs((secondx - firstx)) + abs((secondy - firsty)))
            distance += pointDist
    print(distance)

day11()