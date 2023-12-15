def day15():
    f = open("input15.txt","r")
    fline = f.readline()
    total = 0
    new_array = fline.split(",")
    for each in new_array:
        total += getHash(each)
        print(total)

def day15_2():
    f = open("input15.txt","r")
    fline = f.readline()
    new_array = fline.split(",")

    boxDict = {}

    for each_number in range(0,256):
        boxDict[each_number] = []

    for each_instruction in new_array:
        # print(each_instruction)
        if "-" in each_instruction:
            lensDetails = each_instruction.split("-")
            name = lensDetails[0]
            boxNumber = getHash(name)
            currentBoxContents = boxDict[boxNumber]

            if name in currentBoxContents:
                boxIndex = currentBoxContents.index(name)

                currentBoxContents.pop(boxIndex+1)
                currentBoxContents.pop(boxIndex)

                boxDict[boxNumber] = currentBoxContents

        if "=" in each_instruction:
            lensDetails = each_instruction.split("=")
            name = lensDetails[0]
            boxNumber = getHash(name)
            currentBoxContents = boxDict[boxNumber]

            if name in currentBoxContents:
                boxIndex = currentBoxContents.index(name)

                boxDict[boxNumber][boxIndex+1] = lensDetails[1]
            else:
                boxDict[boxNumber] += lensDetails

    print(boxDict)

    total = 0
    for each_key in range(0,256):
        n = 1
        for each_entry in range(1,len(boxDict[each_key]),2):
            total += (each_key+1) * n * int(boxDict[each_key][each_entry])
            # print(total)
            n += 1
    print(total)

def getHash(line):
    charArray = list(line)

    total = 0
    for currentChar in list(line):
        asciiEquiv = ord(currentChar)
        total += asciiEquiv
        total = (total * 17)%256

    return total



# day15()
day15_2()