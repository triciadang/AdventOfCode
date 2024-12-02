

def day2():
    # Use a breakpoint in the code line below to debug your script.

    totalSum = 0
    with open("input2.txt") as f:
        f = f.readlines()

    for each in f:
        game_number, is_possible = isPossible(each)
        if is_possible:
            totalSum += int(game_number)
        print(totalSum)

def day2_5():

    totalSum = 0

    with open("input2.txt") as f:
        f = f.readlines()


    for each in f:
        game_number, power = getPowers(each)
        print(power)
        totalSum += power
    print(totalSum)


def getPowers(each_line):

    game_split = each_line.split(":")

    game_number = game_split[0].split(" ")[1]

    #get numbers for each color
    maxRed = -1
    maxGreen = -1
    maxBlue = -1

    each_color = game_split[1].split(" ")
    print(each_color)

    index = -1
    while each_color[index] != '':

        if "green" in each_color[index]:
            index -= 1
            if int(each_color[index]) > maxGreen:
                maxGreen = int(each_color[index])

        elif "blue" in each_color[index]:
            index -= 1
            if int(each_color[index]) > maxBlue:
                maxBlue = int(each_color[index])

        elif "red" in each_color[index]:
            index -= 1
            if int(each_color[index]) > maxRed:
                maxRed = int(each_color[index])

        index -= 1

    return game_number,maxGreen * maxBlue * maxRed


def isPossible(each_line):

    game_split = each_line.split(":")

    game_number = game_split[0].split(" ")[1]

    #get numbers for each color
    redBalls = 12
    greenBalls = 13
    blueBalls = 14

    is_possible = True
    each_color = game_split[1].split(" ")
    print(each_color)

    index = -1
    while each_color[index] != '':

        if "green" in each_color[index]:
            index -= 1
            if int(each_color[index]) > greenBalls:
                is_possible = False

        elif "blue" in each_color[index]:
            index -= 1
            if int(each_color[index]) > blueBalls:
                is_possible = False

        elif "red" in each_color[index]:
            index -= 1
            if int(each_color[index]) > redBalls:
                is_possible = False

        index -= 1

    return game_number,is_possible

day2_5()