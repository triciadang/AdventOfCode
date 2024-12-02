def day7():
    # Use a breakpoint in the code line below to debug your script.

    with open("input7.txt") as f:
        fLines = f.readlines()

        checkHandDos(fLines)

def checkHand(lines):
    print(lines)
    i = 0
    high_card = []
    one_pair = []
    two_pair = []
    three = []
    full_house = []
    four_kind = []
    five_kind = []


    while i != len(lines):
        sorted = False
        hand = lines[i].split()[0]

        for k in range(0,len(hand)):
            if sorted == False:
                count = hand.count(hand[k])
                if count == 5:
                    five_kind += [lines[i]]
                    sorted = True

                elif count == 4:
                    four_kind += [lines[i]]
                    sorted = True

                elif count == 3:
                    fullHouseCount = 0
                    for j in range(1,len(hand)):
                        if hand[k] != hand[j] and sorted == False:
                            fullHouseCount = hand.count(hand[j])
                            if fullHouseCount == 2:
                                full_house += [lines[i]]
                                sorted = True
                    if sorted == False:
                        three += [lines[i]]
                        sorted = True

                elif count == 2:
                    for j in range(1,len(hand)):
                        if hand[k] != hand[j] and sorted == False:
                            pairCount = hand.count(hand[j])
                            if pairCount == 2:
                                two_pair += [lines[i]]
                                sorted = True
                            if pairCount ==3:
                                full_house += [lines[i]]
                                sorted = True

                    if sorted == False:
                        one_pair += [lines[i]]
                        sorted = True

        if sorted == False:
            high_card += [lines[i]]

        i += 1

    print(high_card)
    print(one_pair)
    print(two_pair)
    print(three)
    print(full_house)
    print(four_kind)
    print(five_kind)



    total_winnings = 0
    rank = 1
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    # ranks = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}


    convertedHighCard = convert(high_card)
    print(convertedHighCard)
    convertedHighCard.sort()
    if high_card is not None:
        for each in convertedHighCard:
            print(rank)
            print(each)
            bid = each.split()[1]
            total_winnings += int(bid) * rank
            rank += 1

    convertedOne = convert(one_pair)
    print(convertedOne)
    convertedOne.sort()
    if one_pair is not None:
        for each in convertedOne:
            print(rank)
            print(each)
            bid = each.split()[1]
            total_winnings += int(bid) * rank
            rank += 1

    convertedTwo = convert(two_pair)
    print(convertedTwo)
    convertedTwo.sort()
    if two_pair is not None:
        for each in convertedTwo:
            print(rank)
            print(each)
            bid = each.split()[1]
            total_winnings += int(bid) * rank
            rank += 1

    convertedThree = convert(three)
    print(convertedThree)
    convertedThree.sort()
    if three is not None:
        for each in convertedThree:
            print(rank)
            print(each)
            bid = each.split()[1]
            total_winnings += int(bid) * rank
            rank += 1

    convertedFullHouse = convert(full_house)
    print(convertedFullHouse)
    convertedFullHouse.sort()
    if full_house is not None:
        for each in convertedFullHouse:
            print(rank)
            print(each)
            bid = each.split()[1]
            total_winnings += int(bid) * rank
            rank += 1

    convertedFour = convert(four_kind)
    print(convertedFour)
    convertedFour.sort()
    if four_kind is not None:
        for each in convertedFour:
            print(rank)
            print(each)
            bid = each.split()[1]
            total_winnings += int(bid) * rank
            rank += 1

    convertedFive = convert(five_kind)
    print(convertedFive)
    convertedFive.sort()
    if five_kind is not None:
        for each in convertedFive:
            print(rank)
            print(each)
            bid = each.split()[1]
            total_winnings += int(bid) * rank
            rank += 1

    print(total_winnings)

def checkHandDos(lines):
    # print(lines)
    i = 0
    high_card = []
    one_pair = []
    two_pair = []
    three = []
    full_house = []
    four_kind = []
    five_kind = []


    while i != len(lines):
        hand = lines[i].split()[0]
        high_card_bool = True
        one_pair_bool = False
        two_pair_bool = False
        three_bool = False
        full_house_bool = False
        four_kind_bool = False
        five_kind_bool = False

        for k in range(0,len(hand)):
            jCount = hand.count("J")
            if hand[k] != "J" or jCount == 5:
                count = hand.count(hand[k]) + jCount

                if jCount == 5:
                    count = 5

                if count == 5:
                    five_kind_bool = True

                elif count == 4:
                    four_kind_bool = True

                elif count == 3:
                    for j in range(1,len(hand)):
                        if hand[k] != hand[j] and hand[j]!="J":
                            fullHouseCount = hand.count(hand[j])
                            if fullHouseCount == 2:
                                full_house_bool = True
                    three_bool = True

                elif count == 2:
                    for j in range(1,len(hand)):
                        if hand[k] != hand[j] and hand[j]!="J":
                            pairCount = hand.count(hand[j])
                            if pairCount == 2:
                                two_pair_bool = True
                            if pairCount ==3:
                                full_house_bool = True

                    one_pair_bool = True

        if five_kind_bool:
            five_kind += [lines[i]]
        elif four_kind_bool:
            four_kind += [lines[i]]
        elif full_house_bool:
            full_house += [lines[i]]
        elif three_bool:
            three += [lines[i]]
        elif two_pair_bool:
            two_pair += [lines[i]]
        elif one_pair_bool:
            one_pair += [lines[i]]
        elif high_card_bool:
            high_card += [lines[i]]


        i += 1


    print(high_card)
    print(one_pair)
    print(two_pair)
    print(three)
    print(full_house)
    print(four_kind)
    print(five_kind)



    total_winnings = 0
    rank = 1
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    # ranks = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}


    convertedHighCard = convert(high_card)
    print(convertedHighCard)
    convertedHighCard.sort()
    if high_card is not None:
        for each in convertedHighCard:
            print(rank)
            print(each)
            bid = each.split()[1]
            total_winnings += int(bid) * rank
            rank += 1

    convertedOne = convert(one_pair)
    print(convertedOne)
    convertedOne.sort()
    if one_pair is not None:
        for each in convertedOne:
            print(rank)
            print(each)
            bid = each.split()[1]
            total_winnings += int(bid) * rank
            rank += 1

    convertedTwo = convert(two_pair)
    print(convertedTwo)
    convertedTwo.sort()
    if two_pair is not None:
        for each in convertedTwo:
            print(rank)
            print(each)
            bid = each.split()[1]
            total_winnings += int(bid) * rank
            rank += 1

    convertedThree = convert(three)
    print(convertedThree)
    convertedThree.sort()
    if three is not None:
        for each in convertedThree:
            print(rank)
            print(each)
            bid = each.split()[1]
            total_winnings += int(bid) * rank
            rank += 1

    convertedFullHouse = convert(full_house)
    print(convertedFullHouse)
    convertedFullHouse.sort()
    if full_house is not None:
        for each in convertedFullHouse:
            print(rank)
            print(each)
            bid = each.split()[1]
            total_winnings += int(bid) * rank
            rank += 1

    convertedFour = convert(four_kind)
    print(convertedFour)
    convertedFour.sort()
    if four_kind is not None:
        for each in convertedFour:
            print(rank)
            print(each)
            bid = each.split()[1]
            total_winnings += int(bid) * rank
            rank += 1

    convertedFive = convert(five_kind)
    print(convertedFive)
    convertedFive.sort()
    if five_kind is not None:
        for each in convertedFive:
            print(rank)
            print(each)
            bid = each.split()[1]
            total_winnings += int(bid) * rank
            rank += 1

    print(total_winnings)

def convert(tryArray):
    new_array = []
    ranks = {'J':'A', '2':'B', '3':'C', '4':'D', '5':'E', '6':'F', '7':'G', '8':'H', '9':'I', 'T':'J', 'Q':'L', 'K':'M', 'A':'N'}

    for each_entry in tryArray:
        new_entry = each_entry.split()
        newString = ""
        for each_letter in new_entry[0]:
            newString += ranks[each_letter]

        newString = newString + " " + new_entry[1]
        new_array += [newString]

    return new_array


day7()