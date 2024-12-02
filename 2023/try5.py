
def day5():
    # Use a breakpoint in the code line below to debug your script.

    totalSum = 0

    with open("input5.txt") as f:
        fLines = f.readlines()

        lowestNumber = seedMap(fLines)
    # print(totalSum)

def seedMap(lines):
    # print(lines)

    i = 0
    seedSoil = []
    soilFertilizer = []
    fertilizerWater = []
    waterLight = []
    lightTemp = []
    tempHumidity = []
    humidityLocation = []
    while i != len(lines):
        if "seeds" in lines[i]:
            seeds_entry = lines[i].split()
            i += 1
            # print(seeds_entry)
        elif "seed-to-soil" in lines[i]:

            while "soil-to-fertilizer" not in lines[i]:
                seedSoil += [lines[i]]
                i+=1
            # print(seedSoil)
        elif "soil-to-fertilizer" in lines[i]:

            while "fertilizer-to-water" not in lines[i]:
                soilFertilizer += [lines[i]]
                i+=1
            # print(soilFertilizer)
        elif "fertilizer-to-water" in lines[i]:

            while "water-to-light" not in lines[i]:
                fertilizerWater += [lines[i]]
                i+=1
            # print(fertilizerWater)
        elif "water-to-light" in lines[i]:

            while "light-to-temperature" not in lines[i]:
                waterLight += [lines[i]]
                i+=1
            # print(waterLight)
        elif "light-to-temperature" in lines[i]:

            while "temperature-to-humidity" not in lines[i]:
                lightTemp += [lines[i]]
                i+=1
            # print(lightTemp)
        elif "temperature-to-humidity" in lines[i]:

            while "humidity-to-location" not in lines[i]:
                tempHumidity += [lines[i]]
                i+=1
            # print(tempHumidity)
        elif "humidity-to-location" in lines[i]:

            while i < len(lines):
                humidityLocation += [lines[i]]
                i+=1
            # print(humidityLocation)
        else:
            i+=1

    seedSoilDict = buildDict(seedSoil)
    soilFertilizeDict = buildDict(soilFertilizer)
    fertilizerWaterDict = buildDict(fertilizerWater)
    waterLightDict = buildDict(waterLight)
    lightTempDict = buildDict(lightTemp)
    tempHumidityDict = buildDict(tempHumidity)
    humidityLocationDict = buildDict(humidityLocation)

    leastNumber = 999999999999
    for k in range(1,len(seeds_entry)):
        seed = int(seeds_entry[k])

        if seed in seedSoilDict:
            soil = seedSoilDict[seed]
        else:
            soil = seed

        if soil in soilFertilizeDict:
            fertilizer = soilFertilizeDict[soil]
        else:
            fertilizer = soil

        if fertilizer in fertilizerWaterDict:
            water = fertilizerWaterDict[fertilizer]
        else:
            water = fertilizer


        if water in waterLightDict:
            light = waterLightDict[water]
        else:
            light = water


        if light in lightTempDict:
            temp = lightTempDict[light]
        else:
            temp = light


        if temp in tempHumidityDict:
            humidity = tempHumidityDict[temp]
        else:
            humidity = temp


        if humidity in humidityLocationDict:
            location = humidityLocationDict[humidity]
        else:
            location = humidity

        if location < leastNumber:
            leastNumber = location


    print(leastNumber)

def buildDict(mapArray):
    # print(mapArray)
    mapDict = {}
    for i in range(1,len(mapArray)):
        if mapArray[i] != "\n":
            entry = mapArray[i]
            eachEntry = entry.split()
            # print(eachEntry)

            dstRange = int(eachEntry[0].strip())
            srcRange = int(eachEntry[1].strip())
            rangeLen = int(eachEntry[2].strip())

            for j in range(rangeLen):
                mapDict[srcRange+j] = dstRange+j

    # print(mapDict)
    return mapDict


day5()