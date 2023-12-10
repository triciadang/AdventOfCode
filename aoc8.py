import numpy as np


def day8():
    f = open("input8.txt", "r")
    flines = f.readlines()

    zFinder(flines)


def zFinder(lines):
    path = lines[0]
    pathMap = {}
    for i in range(2, len(lines)):
        mapArray = lines[i].split()

        firstEntry = mapArray[2].replace("(", "")
        firstEntry = firstEntry.replace(",", "")
        print(firstEntry)
        secondEntry = mapArray[3].strip()
        secondEntry = secondEntry.replace(")", "")
        print(secondEntry)

        pathMap[mapArray[0]] = [firstEntry, secondEntry]

    zzzFound = False
    newEntry = "AAA"
    count = 0
    while zzzFound == False:
        for i in range(0, len(path)):
            each_letter = path[i]
            if each_letter == "L":
                newEntry = pathMap[newEntry][0]
                count += 1
            elif each_letter == "R":
                newEntry = pathMap[newEntry][1]
                count += 1

            if newEntry == "ZZZ":
                zzzFound = True
                print(count)
                break

            if i == len(path):
                i = 0
            else:
                i += 1


# second problem


def day8_5():
    f = open("input8.txt", "r")
    flines = f.readlines()

    zFinderDos(flines)


def findAllAs(pathMapDict):
    aArray = []
    for each in pathMapDict.keys():
        if each[-1] == "A":
            aArray += [each]

    return aArray


def zFinderDos(lines):
    path = lines[0].strip()

    pathMap = {}
    for i in range(2, len(lines)):
        mapArray = lines[i].split()

        firstEntry = mapArray[2].replace("(", "")
        firstEntry = firstEntry.replace(",", "")
        secondEntry = mapArray[3].strip()
        secondEntry = secondEntry.replace(")", "")

        pathMap[mapArray[0]] = [firstEntry, secondEntry]

    aArray = findAllAs(pathMap)
    aNewEntry = {}
    lcmArray = []

    for eachAEntry in aArray:
        aNewEntry[eachAEntry] = eachAEntry

    count = 0

    zzzFound = False

    for eachA in aArray:
        zzzFound = False
        count = 0
        while zzzFound == False:
            for i in range(0, len(path)):

                count += 1
                each_letter = path[i]

                aNewEntry[eachA] = findNext(aNewEntry[eachA],pathMap,each_letter)

                if aNewEntry[eachA][-1] == "Z":
                    lcmArray += [count]
                    print(count)
                    # zzzFound = True

                if i == len(path):
                    i = 0
                # print(count)

    print(count)
    print(lcmArray)


    x = np.lcm.reduce(lcmArray,dtype=object)
    x = np.longdouble(x)




def findNext(newEntry, pathMap, each_letter):
    # print(pathMap)

    lookUpArray = pathMap[newEntry]

    if each_letter == "L":
        newEntry = lookUpArray[0]

    elif each_letter == "R":
        newEntry = lookUpArray[1]

    return newEntry


# day8()
day8_5()