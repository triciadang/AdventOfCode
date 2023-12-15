import numpy as np
import pandas as pd


def day13():
    f = open("input13.txt","r")
    flines = f.readlines()
    isSymmetric(flines)


def isSymmetric(lines):
    fullArray = []
    total = 0
    for i in range(0,len(lines)):
        temp_line = lines[i].strip("\n")
        if temp_line == "" or i == len(lines)-1:
            total += getSymmetry(fullArray,rowLength)
            fullArray = []
        else:
            rowLength = len(temp_line)
            temp_line = list(temp_line)
            fullArray.append(temp_line)
    print(total)


def getSymmetry(fullArray,rowLength):
    total = 0
    dataframe = pd.DataFrame(fullArray)
    symmetric = False
    print(dataframe)
    # print(dataframe[0])
    #check column
    for i in range(0,rowLength-1):
        if dataframe[i].equals(dataframe[i+1]):
            print(i)
            temp_i = i
            temp_j = temp_i+1
            check = True
            while check== True and temp_i >=0 and temp_j < rowLength:
                if dataframe[temp_i].equals(dataframe[temp_j]):
                    temp_i -= 1
                    temp_j += 1
                else:
                    check = False
            if check == True:
                print("here")
                total += i+1


    #check row
    for j in range(0,len(fullArray)-1):
        if fullArray[j] == fullArray[j+1]:
            temp_i = j
            temp_j = j+1
            check = True
            while check== True and temp_i >=0 and temp_j < len(fullArray):
                if fullArray[temp_i]==(fullArray[temp_j]):
                    temp_i -= 1
                    temp_j += 1
                else:
                    check = False
            if check == True:
                total += 100 * (j+1)
                
    return (total)
#=================PART 2=====================
def day13_5():
    f = open("input13.txt","r")
    flines = f.readlines()
    isSymmetricDos(flines)

def isSymmetricDos(lines):
    fullArray = []
    total = 0
    for i in range(0,len(lines)):
        temp_line = lines[i].strip("\n")

        #separate problems
        if temp_line == "" or i == len(lines)-1:
            actualCol,actualRow = getColRowSymmetry(fullArray)
            total += getNewReflection(fullArray,actualCol,actualRow)
            print(total)
            fullArray = []

        #build problem
        else:
            temp_line = list(temp_line)
            fullArray.append(temp_line)


def getColRowSymmetry(fullArray):
    rowLength = len(fullArray[0])
    dataframe = pd.DataFrame(fullArray)
    print(dataframe)
    actualCol = None
    actualRow = None


    #check column
    for i in range(0,rowLength-1):
        #check if column matches next one
        if dataframe[i].equals(dataframe[i+1]):
            temp_i = i
            temp_j = temp_i+1
            check=True
            while check== True and temp_i >=0 and temp_j < rowLength:
                if dataframe[temp_i].equals(dataframe[temp_j]):
                    #check every other column
                    temp_i -= 1
                    temp_j += 1
                else:
                    check = False
                    
            if check == True:
                actualCol = i


    #check row
    for j in range(0,len(fullArray)-1):
        if fullArray[j] == fullArray[j+1]:
            temp_i = j
            temp_j = j+1
            check = True
            while check== True and temp_i >=0 and temp_j < len(fullArray):
                if fullArray[temp_i]==(fullArray[temp_j]):
                    #check other rows
                    temp_i -= 1
                    temp_j += 1
                else:
                    check = False
            if check == True:
                actualRow = j

    #return where real line of symmetry is   
    return actualCol,actualRow

def checkIfOneApartCol(fullArray,col1,col2):
    differences = 0

    for each_i in range(0,len(fullArray)):
        if fullArray[each_i][col1] != fullArray[each_i][col2]:
            differences += 1

    if differences == 1:
        return True
    else:
        return False
    
def checkIfOneApartRow(fullArray,rowLength,row1,row2):
    differences = 0

    for each_i in range(0,rowLength):
        if fullArray[row1][each_i] != fullArray[row2][each_i]:
            differences += 1

    if differences == 1:
        return True
    else:
        return False

def getNewReflection(fullArray,actualCol,actualRow):
    rowLength = len(fullArray[0])
    dataframe = pd.DataFrame(fullArray)

    #check column
    for i in range(0,rowLength-1):
        #check if column matches actual symmetry
        if actualCol is None or i != actualCol:
            temp_i = i
            temp_j = temp_i+1

            #check if there is a column with one apart
            if dataframe[i].equals(dataframe[i+1]):
                
                check=True
                alreadyChangedOne = False
                while check== True and temp_i >=0 and temp_j < rowLength:
                    if dataframe[temp_i].equals(dataframe[temp_j]):
                        #check every other column
                        temp_i -= 1
                        temp_j += 1
                    else:
                        if alreadyChangedOne == False:
                            isColApart = checkIfOneApartCol(fullArray,temp_i,temp_j)
                            #if it is one column apart
                            if isColApart == True:
                                alreadyChangedOne = True
                                temp_i -= 1
                                temp_j +=1
                            else:
                                check = False
                        else:
                            check = False
                if check == True:
                    return (i+1)

            #check if a column next to another column is off by one
            else:
                isColApart = checkIfOneApartCol(fullArray,temp_i,temp_j)

                #if it is one col apart, you have to make sure the rest have symmetry
                if isColApart == True:
                    temp_i -= 1
                    temp_j += 1
                    check = True
                    while check== True and temp_i >=0 and temp_j < rowLength:
                        #if all of them have symmetry
                        if dataframe[temp_i].equals(dataframe[temp_j]):
                            #check every other column
                            temp_i -= 1
                            temp_j += 1
                        else:
                            check = False
                    if check == True:
                        return (i+1)


    #check row
    for j in range(0,len(fullArray)-1):
        #check if row matches actual symmetry
        if actualRow is None or j != actualRow:
            temp_i = j
            temp_j = j+1
            #check if there is one row apart when row matches next row
            if fullArray[j] == fullArray[j+1]:
                
                check = True
                alreadyChangedOneRow = False
                while check== True and temp_i >=0 and temp_j < len(fullArray):
                    if fullArray[temp_i]==(fullArray[temp_j]):
                        #check other rows
                        temp_i -= 1
                        temp_j += 1
                    else:
                        if alreadyChangedOneRow == False:
                            isRowApart = checkIfOneApartRow(fullArray,rowLength,temp_i,temp_j)
                            #if it is one col apart
                            if isRowApart == True:
                                alreadyChangedOneRow = True
                                temp_i -= 1
                                temp_j +=1
                            else:
                                check = False
                        else:
                            check = False
                if check == True:
                    return (j+1)*100
                
            #check if row next to another row is off by one
            else:
                isRowApart = checkIfOneApartRow(fullArray,rowLength,temp_i,temp_j)

                #if it is one row apart, you have to make sure the rest have symmetry
                if isRowApart == True:
                    check = True
                    temp_i -= 1
                    temp_j += 1
                    print("i")
                    print(temp_i)
                    print("J")
                    print(temp_j)
                    while check== True and temp_i >=0 and temp_j < len(fullArray):
                        #if all of them have symmetry
                        if fullArray[temp_i]==(fullArray[temp_j]):
                            #check every other column
                            temp_i -= 1
                            temp_j += 1
                        else:
                            check = False
                    if check == True:
                        return (j+1)*100

day13_5()