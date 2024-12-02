

def day3():
    # Use a breakpoint in the code line below to debug your script.

    totalSum = 0
    matrix_of_numbers = []
    with open("input3.txt") as f:
        f = f.readlines()


    for each in f:
        matrix_of_numbers +=[each]

    totalSum += check_if_part_number(matrix_of_numbers)
    # print(totalSum)

def check_if_part_number(matrix_numbers):
    length = 10
    total_num = ""
    sum_num = 0

    for i in range(0, len(matrix_numbers)):
        for j in range(0,length):

            if matrix_numbers[i][j].isdigit():
                questionNumber = matrix_numbers[i][j]

                total_num += questionNumber

            #for last column - check if number
            elif total_num != "" and j==0:

                isPartNumber = False
                temp_i = i-1
                temp_j = 10
                if (temp_j-len(total_num)-1) >=0:
                    print("same before")
                    print(temp_j-len(total_num)-1)
                    if matrix_numbers[temp_i][temp_j-len(total_num)-1] != ".":
                        isPartNumber = True

                #check previous row
                if (temp_i-1)>=0:
                    for k in range(0,len(total_num)+2):
                        #row below, column above
                        if (temp_j-k)>=0 and (temp_j-k)<=(length-1):
                            test_number = matrix_numbers[temp_i-1][temp_j-k]
                            print("previous row")
                            print(temp_j-k)
                            print(test_number)
                            if not test_number.isdigit() and test_number != ".":
                                isPartNumber = True

                #check next row
                if (temp_i+1)<len(matrix_numbers):
                    for l in range (1,len(total_num)+2):
                        test_number = matrix_numbers[temp_i+1][temp_j-l]
                        print("next row")
                        print(temp_j - l)
                        print(test_number)
                        if (temp_j-l)>=0 and (temp_j-l)<=(length-1):
                            if not test_number.isdigit() and test_number != ".":
                                isPartNumber = True


                if isPartNumber:
                    print(total_num)
                    sum_num += int(total_num)

                total_num = matrix_numbers[i][j]


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
                    # print(total_num)
                    sum_num += int(total_num)
                total_num = ""

    return sum_num



day3()