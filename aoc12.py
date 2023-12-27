import numpy as np
import itertools
from functools import cache


def day12():
    f = open("input12.txt","r")
    flines = f.readlines()
    getSprings(flines)

def getSprings(lines):
    springMap = []
    springNumArray = []
    total = 0
    for i in range(0,len(lines)):
        tempArray = lines[i].split(" ")
        springPart = tempArray[0]
        springNum = tempArray[1]
        springMap.append(springPart)
        springNumArray.append(springNum)
        
    for i in range(0,len(springMap)):
        print(i)
    # for i in range(0,1):
        sprintAlrInArray = springMap[i].count("#")

        springNumArr = springNumArray[i].strip("\n")
        springNumArr = springNumArr.split(",")

        totalSprings = 0
        for each_spring in springNumArr:
            totalSprings += int(each_spring)

        springsNeeded = totalSprings - sprintAlrInArray

        questionMarkCount = springMap[i].count("?")

        newList = range(questionMarkCount)

        unique_combos = (itertools.combinations(newList,springsNeeded))
        combo_list = [list(t) for t in unique_combos]

        current_work = list(springMap[i])
        
        for j in range(0,len(combo_list)):
            tempWork = np.copy(current_work)
            questionCount = 0
            i = 0
            k = 0
            numChanged = 0
            while numChanged < len(combo_list[j]):
                if tempWork[i] == "?":
                    if questionCount == combo_list[j][k]:
                        tempWork[i] = "#"
                        k += 1
                        numChanged += 1
                    questionCount += 1
                i += 1

            if checkIfWorks(tempWork,springNumArr) == True:
                total += 1

    print(total)



def checkIfWorks(tempWork,givenSpringMap):
    j = 0
    springCount = 0
    # tempWork = ['?', '#', '#', '#', '?', '?', '?', '?', '?', '#', '#', '#']
    

    for i in range(0,len(tempWork)):
        if j < len(givenSpringMap):
            if tempWork[i] == "#":
                springCount += 1
            elif springCount != 0:
                if springCount ==int(givenSpringMap[j]):
                    j += 1
                    springCount = 0
                else:
                    return False
                
    #make sure you went through the whole thing
    if springCount != 0:
        if springCount ==int(givenSpringMap[j]):
            j += 1
            springCount = 0
        else:
            return False

    if j == len(givenSpringMap):
        return True
    else:
        return False


day12()