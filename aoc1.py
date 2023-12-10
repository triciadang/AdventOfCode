
def day1():
    # Use a breakpoint in the code line below to debug your script.
    total_sum = 0
    with open("input.txt") as f:
        f = f.readlines()
        print(f)
    for each in f:

        total_sum += int(addLines(each))


def addLine(line):

    first_number = -1
    second_number= -1

    #find first
    for each_letter in line:
        if each_letter.isdigit():
            first_number = each_letter
            break

    #find last
    for each_letter in reversed(line):

        if each_letter.isdigit():
            second_number = each_letter
            break

    return first_number + second_number



def addLines(line):


    first_number = -1
    second_number= -1

    isInt = False

    #find first
    for each_letter in line:
        try:
            int(each_letter)
            isInt = True

        except ValueError:
            continue


        if isInt:
            first_number = each_letter
            break


    isInt = False
    #find last
    for each_letter in reversed(line):

        try:
            int(each_letter)
            isInt = True

        except ValueError:
            continue


        if isInt:
            second_number = each_letter
            break


    return first_number + second_number

def addLines_2(line):

    first_number = -1
    second_number= -1

    num_array = []

    #find first
    word = ""
    for each_letter in line:
        if each_letter.isdigit():
            if word != "":
                num_array += [word]
                word = ""
            num_array += each_letter
        else:
            word += each_letter
    if word != "":
        num_array += [word]


    print(num_array)
    for each_entry in num_array:
        if each_entry.isdigit():
            if first_number == -1:
                first_number = int(each_entry)
            second_number = int(each_entry)
        else:
            first_num, last_num = num_to_int(each_entry)
            if first_num != -5:
                if first_number == -1:
                    first_number = first_num
                second_number = last_num

    total = int(str(first_number) + str(second_number))



    return(total)

def num_to_int(word_string):
    first_num = -5
    first_position = 100
    last_num = -5
    last_position = -1

    if "one" in word_string:
        if word_string.find("one") < first_position:
            first_num = 1
            first_position = word_string.find("one")
        if word_string.rindex("one") >= last_position:
            last_num  = 1
            last_position = word_string.rindex("one")

    if "two" in word_string:
        if word_string.find("two") < first_position:
            first_num = 2
            first_position = word_string.find("two")
        if word_string.rindex("two") >= last_position:
            last_num  = 2
            last_position = word_string.rindex("two")

    if "three" in word_string:
        if word_string.find("three") < first_position:
            first_num = 3
            first_position = word_string.find("three")
        if word_string.rindex("three") >= last_position:
            last_num  = 3
            last_position = word_string.rindex("three")

    if "four" in word_string:
        if word_string.find("four") < first_position:
            first_num = 4
            first_position = word_string.find("four")
        if word_string.rindex("four") >= last_position:
            last_num  = 4
            last_position = word_string.rindex("four")

    if "five" in word_string:
        if word_string.find("five") < first_position:
            first_num = 5
            first_position = word_string.find("five")
        if word_string.rindex("five") >= last_position:
            last_num  = 5
            last_position = word_string.rindex("five")

    if "six" in word_string:
        if word_string.find("six") < first_position:
            first_num = 6
            first_position = word_string.find("six")
        if word_string.rindex("six") >= last_position:
            last_num  = 6
            last_position = word_string.rindex("six")

    if "seven" in word_string:
        if word_string.find("seven") < first_position:
            first_num = 7
            first_position = word_string.find("seven")
        if word_string.rindex("seven") >= last_position:
            last_num  = 7
            last_position = word_string.rindex("seven")

    if "eight" in word_string:
        if word_string.find("eight") < first_position:
            first_num = 8
            first_position = word_string.find("eight")
        if word_string.rindex("eight") >= last_position:
            last_num  = 8
            last_position = word_string.rindex("eight")

    if "nine" in word_string:
        if word_string.find("nine") < first_position:
            first_num = 9
        if word_string.rindex("nine") >= last_position:
            last_num  = 9


    # print(first_num)
    # print(last_num)

    return first_num, last_num



def day1_5():
    # Use a breakpoint in the code line below to debug your script.
    total_sum = 0
    with open("input.txt") as f:
        f = f.readlines()
        print(f)
    for each in f:
        print(addLines_2((each)))
        total_sum += addLines_2(each)
    print(total_sum)

#day1()
day1_5()


