import numpy as np
import itertools


def day12():
    f = open("input12.txt","r")
    flines = f.readlines()
    getSprings(flines)

def getSprings(lines):
    springMap = []
    springNumArray = []
    for i in range(0,len(lines)):
        tempArray = lines[i].split(" ")
        springPart = tempArray[0]
        springNum = tempArray[1]
        springMap.append(springPart)
        springNumArray.append(springNum)
        
    print(springMap)
    print(springNumArray)

    for i in range(0,len(springMap)):
        withOutNewLine = springMap[i].strip("\n")
        eachNum = springNumArray[i]
        eachNum = eachNum.strip("\n")
        eachNum = eachNum.split(",")
        print(eachNum)

        hashtagCount = springMap[i].count("#")
        questionCount = springMap[i].count("?")

        totalchar = 0

        eachNum = springNumArray[i]
        eachNum = eachNum.strip("\n")
        eachNum = eachNum.split(",")
        print(eachNum)

        for each in eachNum:
            totalchar += int(each)           
        print(totalchar)

        questionsNeededToBeFilled = totalchar - hashtagCount
        print(questionsNeededToBeFilled)


        questionLocations = []
        # declare for loop
        for itr in range(0,len(springMap[i])):
 
      # check the condition
            if (springMap[i][itr] == "?"):
 
          # print the indices
                questionLocations += [itr]

        print(questionLocations)

        allCombos = itertools.combinations(questionLocations,questionsNeededToBeFilled)
        for each in allCombos:
            print(each)
        print(allCombos)
    #     print(questionsNeededToBeFilled)













# def getSprings(lines):
#     springMap = []
#     springNumArray = []
#     for i in range(0,len(lines)):
#         tempArray = lines[i].split(" ")
#         springPart = tempArray[0]
#         springNum = tempArray[1]
#         springMap.append(springPart)
#         springNumArray.append(springNum)
        
#     print(springMap)
#     print(springNumArray)

#     total = 0

#     for i in range(0,len(springMap)):
#         withOutNewLine = springMap[i].strip("\n")
#         sectionArray = withOutNewLine.split(".")
        
#         hashtagArray = []
#         questionCountArray = []
#         for j in range(0,len(sectionArray)):
#             if sectionArray[j] != "":
#                 hashtagArray += [sectionArray[j].count("#")]
#                 questionCountArray += [sectionArray[j].count("?")]

#         if len(sectionArray) == len(springNumArray):



#         print(hashtagArray)
#         print(questionCountArray)
        
        # for j in range(len(sectionArray)-1,-1,-1):
        #     each_section = sectionArray[j]
        #     questionCount = each_section.count("?")
        #     hashtagCount = each_section.count("#")

        #     if hashtagCount <= 

    # for i in range(0,len(springMap)):
    #     withOutNewLine = springMap[i].strip("\n")

    #     questionCount = springMap[i].count("?")
    #     hashtagCount = springMap[i].count("#")

    #     totalchar = 0
    #     eachNum = springNumArray[i]
    #     eachNum = eachNum.strip("\n")
    #     eachNum = eachNum.split(",")
    #     print(eachNum)
    #     for each in eachNum:
    #         totalchar += int(each)
            
    #     totalchar += len(eachNum)-1

    #     Openings = totalchar - hashtagCount
    #     print(Openings)

            # print(sectionArray[j])



day12()