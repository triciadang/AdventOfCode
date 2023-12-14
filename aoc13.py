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
#=============================================================PART 2=====================
def day13_5():
    f = open("input13.txt","r")
    flines = f.readlines()
    isSymmetricDos(flines)

def isSymmetricDos(lines):
    fullArray = []
    total = 0
    for i in range(0,len(lines)):
        temp_line = lines[i].strip("\n")
        if temp_line == "" or i == len(lines)-1:
            col,row = getSymmetryDos(fullArray,rowLength)
            total += getNewReflection(fullArray,rowLength,col,row)
            fullArray = []
        else:
            rowLength = len(temp_line)
            temp_line = list(temp_line)
            fullArray.append(temp_line)
    print(total)

def getNewReflection(fullArray,rowLength,col,row):
    actualCol = col
    actualRow = row

    total = 0
    dataframe = pd.DataFrame(fullArray)
    
    #check column
    for i in range(0,rowLength-1):
        if i != actualCol:
            temp_i = i
            temp_j = temp_i+1
            checkCol = True

            while checkCol== True and temp_i >=0 and temp_j < rowLength:
                if dataframe[temp_i].equals(dataframe[temp_j]):
                    temp_i -= 1
                    temp_j += 1
                else:
                    oneApartBool,entry = checkIfOneApartRow(fullArray,rowLength,temp_i,temp_j)
                    if oneApartBool == True:
                        answer = changeOneColApart(fullArray,rowLength,entry,temp_i,temp_j)
                        temp_i -= 1
                        temp_j += 1
                        break
                    else:
                        checkRow = False
            if checkCol == True:
                # print("here")
                total += i+1

    #check row
    for j in range(0,len(fullArray)-1):
        checkRow = True
        # if fullArray[j] == fullArray[j+1]:
        temp_i = j
        temp_j = j+1

        while checkRow== True and temp_i >=0 and temp_j < len(fullArray):
            if fullArray[temp_i]==(fullArray[temp_j]):
                temp_i -= 1
                temp_j += 1
            else:
                oneApartBool,entry = checkIfOneApartRow(fullArray,rowLength,temp_i,temp_j)
                if oneApartBool == True:
                    answer = changeOneRowApart(fullArray,rowLength,entry,temp_i,temp_j)
                    temp_i -= 1
                    temp_j += 1
                    break
                else:
                    checkRow = False

        if checkRow == True:
            print(total)
            total += 100 * (j+1)    
            break

    # print(dataframe)
    return total

def checkIfOneApartCol(fullArray,rowLength,col1,col2):
    differences = 0
    entry = None

    for each_i in range(0,rowLength):
        if fullArray[each_i][col1] != fullArray[each_i][col2]:
            differences += 1
            entry = each_i

    if differences == 1:
        return True,entry
    else:
        return False,entry
    

def checkIfOneApartRow(fullArray,rowLength,row1,row2):
    differences = 0
    entry = None

    for each_i in range(0,rowLength):
        if fullArray[row1][each_i] != fullArray[row2][each_i]:
            differences += 1
            entry = each_i

    if differences == 1:
        return True,entry
    else:
        return False,entry


def changeOneColApart(fullArray,rowLength,i,temp_i,temp_j):
    dataframe = pd.DataFrame(fullArray)
    print(dataframe)

    tempArray = fullArray
    if tempArray[i][temp_i] == "#":
        tempArray[i][temp_i] = "."
    elif tempArray[i][temp_i] == ".":
        tempArray[i][temp_i] = "#"

    total = getTotal(tempArray,rowLength)

    if total == 0:
        tempArray = fullArray
        if tempArray[i][temp_j] == "#":
            tempArray[i][temp_j] = "."
        elif tempArray[i][temp_j] == ".":
            tempArray[i][temp_j] = "#"
    
    return total

def changeOneRowApart(fullArray,rowLength,i,temp_i,temp_j):
    dataframe = pd.DataFrame(fullArray)
    print(dataframe)

    tempArray = fullArray
    if tempArray[temp_i][i] == "#":
        tempArray[temp_i][i] = "."
    elif tempArray[temp_i][i] == ".":
        tempArray[temp_i][i] = "#"

    total = getTotal(tempArray,rowLength)

    if total == 0:
        tempArray = fullArray
        if tempArray[temp_j][i] == "#":
            tempArray[temp_j][i] = "."
        elif tempArray[temp_j][i] == ".":
            tempArray[temp_j][i] = "#"
    
    return total

def getTotal(fullArray,rowLength):
    total = 0
    dataframe = pd.DataFrame(fullArray)
    print(dataframe)

    for i in range(0,rowLength-1):
        if dataframe[i].equals(dataframe[i+1]):
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
                
    return total

def getSymmetryDos(fullArray,rowLength):
    total = 0
    dataframe = pd.DataFrame(fullArray)
    symmetric = False
    print(dataframe)
    actualCol = None
    actualRow = None

    #check column
    for i in range(0,rowLength-1):
        if dataframe[i].equals(dataframe[i+1]):
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
                actualCol = i


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
                actualRow = j
                
    return actualCol,actualRow

day13_5()