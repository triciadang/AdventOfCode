import numpy as np

def day19():
    f = open("input19.txt","r")
    flines = f.readlines()
    findPaths(flines)

def printArray(array):
    for each in array:
        print(each)

def findPaths(lines):
    total = 0
    inputArray = []

    pathArray = []
    afterNewLine = False
    for i in range(0,len(lines)):
        temp_line = lines[i].strip("\n")
        if lines[i] == "\n":
            afterNewLine = True
        else:
            if afterNewLine == False:
                
                pathArray.append(temp_line)
            else:
                inputArray.append(temp_line)

    print(pathArray)
    print(inputArray)

    for each_line in inputArray:
        print(each_line)
        
        allInputs = each_line[1:-1].split(",")

        xValue = int(allInputs[0][2:])
        mValue = int(allInputs[1][2:])
        aValue = int(allInputs[2][2:])
        sValue = int(allInputs[3][2:])

        pathToFollow = "in"
        
        while pathToFollow != 'A' and pathToFollow != 'R':
            pathToFollow = getNextPath(pathArray,pathToFollow,xValue,mValue,aValue,sValue)
           
        if pathToFollow == 'A':    
            total += xValue + mValue + aValue + sValue
    print(total)


def getNextPath(pathArray,pathToFollow,x,m,a,s):
    i = 0
    letterOfPath = None

    #find correct path
    while letterOfPath != pathToFollow:
        currentcond = pathArray[i]
        index = currentcond.find("{")
        letterOfPath = pathArray[i][0:index]
        i += 1

    #the path is the one pre-increment
    indexOfPathToFollow = i - 1
    # print(pathArray[indexOfPathToFollow])
    
    condToFollow = pathArray[indexOfPathToFollow]
    
    condToFollow = condToFollow[index+1:-1].split(",")
    # conditionals = condToFollow[0]
    # answers = condToFollow[1]

    print(condToFollow)

    # for each_cond in conditionals:
    for i in range(0,len(condToFollow)):
        if "<" in condToFollow[i]:
            inputs = condToFollow[i].split(":")
            firstPart = inputs[0].split("<")
            varToComp = firstPart[0]
            valueToComp = firstPart[1]

            # print(varToComp)
            # print(valueToComp)

            if locals()[varToComp] < int(valueToComp):
                return inputs[1]
            else:
                if isCondition(condToFollow[i+1]) == False:
                    i += 1
                    return condToFollow[i]
                
        if ">" in condToFollow[i]:
            inputs = condToFollow[i].split(":")
            firstPart = inputs[0].split(">")
            varToComp = firstPart[0]
            valueToComp = firstPart[1]

            # print(varToComp)
            # print(valueToComp)

            if locals()[varToComp] > int(valueToComp):
                return inputs[1]
            else:
                if isCondition(condToFollow[i+1]) == False:
                    i += 1
                    return condToFollow[i]
        

def isCondition(entry):
    if "<" in entry or ">" in entry:
        return True
    else:
        return False

day19()