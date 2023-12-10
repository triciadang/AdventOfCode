
def day4():
    # Use a breakpoint in the code line below to debug your script.

    totalSum = 0

    with open("input4.txt") as f:
        fLines = f.readlines()

        for each_line in fLines:
            totalSum += checkWins(each_line)
    # print(totalSum)

def checkWins(lines):
    splitCard = lines.split("|")
    splitFurther = splitCard[0].split(":")
    winNumbers = splitFurther[1].split(" ")
    ticketNumbers = splitCard[1].split(" ")

    # print(winNumbers)
    # print(ticketNumbers)

    totalScore = 0
    score = 0
    for each_winNum in winNumbers:
        if each_winNum != "":
            for each_ticketEntry in ticketNumbers:
                if each_winNum == each_ticketEntry.strip("\n"):
                    score+= 1
                    # if score == 0:
                    #     score += 1
                    # else:
                    #     score *= 2
    # print(score)
    # totalScore += score

    return score

def day4_5():
    # Use a breakpoint in the code line below to debug your script.

    totalSum = 0

    with open("input4.txt") as f:
        fLines = f.readlines()
        totalSum = getCards(fLines)

    print(totalSum)

def getCards(lines):
    # length = 6
    length = 208
    cardArray = [1] * (length)
    print(cardArray)
    for cardNumber in range(1,(len(lines)+1)):
        numOfMatches = checkWins(lines[cardNumber-1])

        print(numOfMatches)
        for each_match in range(0,numOfMatches):
            cardArray[cardNumber + each_match ] += 1 * cardArray[cardNumber-1]

    print(cardArray)

    sum = 0
    for each in cardArray:
        sum += each

    return sum




# day4()
day4_5()