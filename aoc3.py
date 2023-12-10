

def day3():
    # Use a breakpoint in the code line below to debug your script.

    totalSum = 0
    matrix_of_numbers = []
    with open("input3.txt") as f:
        f = f.readlines()


    for each in f:
        matrix_of_numbers +=[each]

    totalSum += check_if_part_number(matrix_of_numbers)
    print(totalSum)

def check_if_part_number(matrix_numbers):
    length = 140
    total_num = ""
    sum_num = 0

    for i in range(0, len(matrix_numbers)):
        for j in range(0,length):

            if matrix_numbers[i][j].isdigit() and j != (length-1):
                questionNumber = matrix_numbers[i][j]

                total_num += questionNumber

            #for last column - check if number
            elif matrix_numbers[i][j].isdigit() and total_num != "" and j==(length-1):

                # print(i)
                # print(j)

                total_num += matrix_numbers[i][j]

                # print(total_num)

                isPartNumber = False

                temp_j = length
                if (temp_j-len(total_num)-1) >=0:
                    # print("same before")
                    # print(temp_j-len(total_num)-1)
                    # print(matrix_numbers[i][temp_j-len(total_num)-1])
                    if matrix_numbers[i][temp_j-len(total_num)-1] != ".":
                        isPartNumber = True

                #check previous row
                if (i-1)>=0:
                    for k in range(0,len(total_num)+2):
                        #row below, column above
                        if (temp_j-k)>=0 and (temp_j-k)<=(length-1):
                            test_number = matrix_numbers[i-1][temp_j-k]
                            # print("previous row")
                            # print(temp_j-k)
                            # print(test_number)
                            if not test_number.isdigit() and test_number != ".":
                                isPartNumber = True

                #check next row
                if (i+1)<len(matrix_numbers):
                    for l in range (1,len(total_num)+2):
                        test_number = matrix_numbers[i+1][temp_j-l]
                        # print("next row")
                        # print(temp_j-1)
                        # print(test_number)
                        if (temp_j-l)>=0 and (temp_j-l)<=(length-1):
                            if not test_number.isdigit() and test_number != ".":
                                isPartNumber = True


                if isPartNumber:
                    print(total_num)
                    sum_num += int(total_num)

                total_num = ""


            elif total_num != "":

                #need to check
                isPartNumber = False


                #check same row
                # print("same after")
                # print(j)
                if matrix_numbers[i][j] != "." and matrix_numbers[i][j] != "\n":
                    isPartNumber = True

                if (j-len(total_num)-1) >=0:
                    # print("same before")
                    # print(j-len(total_num)-1)
                    if matrix_numbers[i][j-len(total_num)-1] != "." and matrix_numbers[i][j] != "\n":
                        isPartNumber = True

                #check previous row
                if (i-1)>=0:
                    for k in range(0,len(total_num)+2):
                        #row below, column above
                        if (j-k)>=0 and (j-k)<=(length-1):
                            # print("previous row")
                            # print(j-k)
                            test_number = matrix_numbers[i-1][j-k]
                            if not test_number.isdigit() and test_number != "." and test_number != "\n":
                                isPartNumber = True

                #check next row
                if (i+1)<len(matrix_numbers):
                    for l in range (0,len(total_num)+2):
                        test_number = matrix_numbers[i+1][j-l]
                        # print("next row")
                        # print(j - l)
                        if (j-l)>=0 and (j-l)<=(length-1):
                            if not test_number.isdigit() and test_number != "." and test_number != "\n":
                                isPartNumber = True


                if isPartNumber:
                    print(total_num)
                    sum_num += int(total_num)
                total_num = ""

    return sum_num



def day3_5():
    # Use a breakpoint in the code line below to debug your script.

    totalSum = 0
    matrix_of_numbers = []
    with open("input3.txt") as f:
        f = f.readlines()


    for each in f:
        matrix_of_numbers += [each]

    totalSum = check_if_gear_number(matrix_of_numbers)
    print(totalSum)

def check_if_gear_number(matrix_numbers):
    length = 140
    sum_num = 0

    for row in range(0, len(matrix_numbers)):
        for column in range(0,length):

            if matrix_numbers[row][column] == "*":

                gear_number = []
                whole_number = ""
                #check previous row for numbers
                # check previous column

                i = row
                j = column

                #if number keeps going
                if matrix_numbers[i-1][j-1].isdigit():
                    while matrix_numbers[i-1][j-1].isdigit():
                        whole_number = matrix_numbers[i-1][j-1] + whole_number
                        j -= 1

                i = row
                j = column
                #check directly above column
                if matrix_numbers[i-1][j].isdigit():
                    whole_number += matrix_numbers[i-1][j]
                else:
                    #reset
                    if whole_number != "":
                        gear_number += [whole_number]
                        whole_number = ""

                i = row
                j = column
                #check next to column
                if matrix_numbers[i-1][j+1].isdigit():
                    while matrix_numbers[i-1][j+1].isdigit():
                        whole_number = whole_number + matrix_numbers[i-1][j+1]
                        j += 1

                if whole_number != "":
                    gear_number += [whole_number]

                #================================================


                #check same row for numbers
                #check same row
                i = row
                j = column
                whole_number = ""

                if matrix_numbers[i][j-1].isdigit():
                    while matrix_numbers[i][j-1].isdigit():
                        whole_number = matrix_numbers[i][j-1] + whole_number
                        j -= 1

                if whole_number != "":
                    gear_number += [whole_number]


                i = row
                j = column
                whole_number = ""
                #check next to column
                if matrix_numbers[i][j+1].isdigit():
                    while matrix_numbers[i][j+1].isdigit():
                        whole_number = whole_number + matrix_numbers[i][j+1]
                        j += 1

                if whole_number != "":
                    gear_number += [whole_number]

                #======================================

                whole_number = ""
                #check next row for numbers
                # check previous column

                i = row
                j = column

                if matrix_numbers[i+1][j-1].isdigit():
                    while matrix_numbers[i+1][j-1].isdigit():
                        whole_number = matrix_numbers[i+1][j-1] + whole_number
                        j -= 1

                i = row
                j = column

                #check directly above column
                if matrix_numbers[i+1][j].isdigit():
                    whole_number += matrix_numbers[i+1][j]
                else:
                    if whole_number!= "":
                        gear_number += [whole_number]
                        whole_number = ""

                i = row
                j = column



                #check next to column
                if matrix_numbers[i+1][j+1].isdigit():
                    while matrix_numbers[i+1][j+1].isdigit():
                        whole_number = whole_number + matrix_numbers[i+1][j+1]
                        j += 1

                if whole_number != "":
                    gear_number += [whole_number]

                print(gear_number)

                if len(gear_number) == 2:
                    gear_ratio = int(gear_number[0]) * int(gear_number[1])
                    print(gear_ratio)
                    sum_num += gear_ratio

    return sum_num

# day3()
day3_5()