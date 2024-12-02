
def day6():
    # Use a breakpoint in the code line below to debug your script.

    with open("input6.txt") as f:
        fLines = f.readlines()

        beatRecords(fLines)

def day6_5():
    # Use a breakpoint in the code line below to debug your script.

    with open("input6.txt") as f:
        fLines = f.readlines()

        beatRecordsDos(fLines)

def beatRecordsDos(lines):
    time = lines[0].split()
    actualTime = ""
    for i in range(1,len(time)):
        actualTime += time[i]
    print(actualTime)
    actualTimeInt = int(actualTime)

    distance = lines[1].split()
    actualDistance = ""
    for j in range(1,len(distance)):
        actualDistance += distance[j]
    print(actualDistance)
    actualDistanceInt = int(actualDistance)


    waysToWin = 0
    for each_time in range (0,actualTimeInt):
        distanceTraveled = (actualTimeInt - each_time) * each_time
        if distanceTraveled > int(actualDistanceInt):
            waysToWin += 1

    print(waysToWin)

def beatRecords(lines):
    time = lines[0].split()
    print(time)
    distance = lines[1].split()
    print(distance)
    productWins = 1
    for i in range(1,len(time)):
        waysToWin = 0
        timeEntry = int(time[i])
        for each_time in range (0,timeEntry):
            distanceTraveled = (timeEntry - each_time) * each_time
            if distanceTraveled > int(distance[i]):
                waysToWin += 1

        productWins = productWins * waysToWin

    print(productWins)

# day6()
day6_5()