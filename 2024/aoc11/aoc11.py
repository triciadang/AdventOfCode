

def main():
    number_of_blinks = 0

    with open("input.txt") as f:
        line = f.read()

    initial_array = line.split()
    stone_dict = {}

    for each in initial_array:
        stone_dict[each] = 1

    print(stone_dict)

    number_of_blinks = 75

    while number_of_blinks > 0:
        new_array = {}

        for each_entry_key in stone_dict.keys():
            count = stone_dict[each_entry_key]

            #engraved with 1
            if each_entry_key == "0":
                new_key = "1"

            #even digits
            elif len(each_entry_key) %2 == 0:
                halfway = int(len(each_entry_key)/2)

                new_key = (str(int(each_entry_key[:halfway])))

                if new_key in new_array:
                    new_array[new_key] += count

                else:
                    new_array[new_key] = count

                new_key = (str(int(each_entry_key[halfway:])))

            # multipled by 2024
            else:
                new_key = str(int(each_entry_key) * 2024)


            if new_key in new_array:
                new_array[new_key] += count

            else:
                new_array[new_key] = count

        stone_dict = new_array

        print(stone_dict)

        number_of_blinks -= 1



    total = 0
    for every_value in stone_dict.values():
        total += every_value

    print(total)




if __name__ == '__main__':
    main()