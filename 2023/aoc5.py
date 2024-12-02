
def day5():
    # Use a breakpoint in the code line below to debug your script.

    totalSum = 0

    with open("input5.txt") as f:
        fLines = f.readlines()

        seedMap(fLines)

def day5_5():
    # Use a breakpoint in the code line below to debug your script.

    totalSum = 0

    with open("input5.txt") as f:
        fLines = f.readlines()

        seedDos(fLines)
        # seedTres(fLines)

def seedTres(lines):
    # print(lines)
    print("here")

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

    lowestNumber = 2561416828
    # highestNumber = 125742457

    soil = getNext(lowestNumber, seedSoil)
    fertilizer = getNext(soil, soilFertilizer)
    water = getNext(fertilizer, fertilizerWater)
    light = getNext(water, waterLight)
    temp = getNext(light, lightTemp)
    humidity = getNext(temp, tempHumidity)
    location = getNext(humidity, humidityLocation)
    print(location)


def seedDos(lines):
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


    seedExists = False
    # location = 62000000
    location = 125742456

    while seedExists != True :
        print("===========")
        print(location)
        humidity = getPrev(location,humidityLocation)
        print(humidity)
        temp = getPrev(humidity,tempHumidity)
        print(temp)
        light = getPrev(temp,lightTemp)
        print(light)
        water = getPrev(light,waterLight)
        print(water)
        fertilizer = getPrev(water,fertilizerWater)
        print(fertilizer)
        soil = getPrev(fertilizer,soilFertilizer)
        print(soil)
        seed = getPrev(soil,seedSoil)
        print(seed)

        i = 1
        while i < len(seeds_entry):
            lower_limit = int(seeds_entry[i])
            upper_limit = (int(seeds_entry[i]) + int(seeds_entry[i+1]))


            if seed >= lower_limit and seed <= upper_limit:
                seedExists = True
                print("here")
                print(location)
                print(seed)
                break

            i += 2
        location += 1

    print(location-1)

def getPrev(base,convArray):
    for i in range(1, len(convArray)):
        foundFinal = False
        if convArray[i] != "\n":
            entry = convArray[i]
            # print(entry)
            eachEntry = entry.split()

            dstRange = int(eachEntry[0].strip())
            srcRange = int(eachEntry[1].strip())
            rangeLen = int(eachEntry[2].strip())

            if base >= dstRange and base <= (dstRange + rangeLen):
                final = srcRange + (base - dstRange)
                foundFinal = True
                break

    if foundFinal == False:
        final = base

    return final

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

    leastLocation = 99999999999999
    for k in range(1,len(seeds_entry)):

        seed = int(seeds_entry[k])

        soil = getNext(seed,seedSoil)
        fertilizer = getNext(soil,soilFertilizer)
        water = getNext(fertilizer,fertilizerWater)
        light = getNext(water,waterLight)
        temp = getNext(light,lightTemp)
        humidity = getNext(temp,tempHumidity)
        location = getNext(humidity,humidityLocation)

        if location < leastLocation:
            leastLocation = location
    print(leastLocation)


def getNext(base,convArray):
    for i in range(1, len(convArray)):
        foundFinal = False
        if convArray[i] != "\n":
            entry = convArray[i]
            # print(entry)
            eachEntry = entry.split()

            dstRange = int(eachEntry[0].strip())
            srcRange = int(eachEntry[1].strip())
            rangeLen = int(eachEntry[2].strip())

            if base >= srcRange and base <= (srcRange + rangeLen):
                final = dstRange + (base - srcRange)
                foundFinal = True
                break

    if foundFinal == False:
        final = base

    return final

day5_5()