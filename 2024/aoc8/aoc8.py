
def main():
    with open("input.txt") as f:
        lines = f.readlines()

    all_unique_locs_to_chars = get_all_locations(lines)
    antinode_locs = []

    #remove new line
    line_length = len(lines[0]) - 1


    for each_char in all_unique_locs_to_chars.keys():

        all_values = all_unique_locs_to_chars[each_char]
        for i in range(0,len(all_values)):
            for j in range(i+1,len(all_values)):


                #line value
                line_diff = all_values[i][0] - all_values[j][0]
                index_diff = all_values[i][1] - all_values[j][1]

                new_line1 = all_values[i][0] + line_diff
                new_index1 = all_values[i][1] + index_diff

                while inbounds_check(new_line1,new_index1,len(lines),line_length):

                    if check_location(new_line1,new_index1,antinode_locs):
                        antinode_locs += [(new_line1,new_index1)]

                    new_line1 = new_line1 + line_diff
                    new_index1 = new_index1 + index_diff

                new_line1 = new_line1 - line_diff
                new_index1 = new_index1 - index_diff

                while inbounds_check(new_line1,new_index1,len(lines),line_length):

                    if check_location(new_line1,new_index1,antinode_locs):
                        antinode_locs += [(new_line1,new_index1)]

                    new_line1 = new_line1 - line_diff
                    new_index1 = new_index1 - index_diff

                new_line2 = all_values[j][0] - line_diff
                new_index2 = all_values[j][1] - index_diff

                while inbounds_check(new_line2,new_index2,len(lines),line_length):

                    if check_location(new_line2,new_index2,antinode_locs):
                        antinode_locs += [(new_line2,new_index2)]

                    new_line2 = new_line2 - line_diff
                    new_index2 = new_index2 - index_diff

                new_line2 = all_values[j][0] + line_diff
                new_index2 = all_values[j][1] + index_diff

                while inbounds_check(new_line2,new_index2,len(lines),line_length):

                    if check_location(new_line2,new_index2,antinode_locs):
                        antinode_locs += [(new_line2,new_index2)]

                    new_line2 = new_line2 + line_diff
                    new_index2 = new_index2 + index_diff

    print(antinode_locs)
    print(len(antinode_locs))


def inbounds_check(line,index,num_of_lines,line_length):
    if line >= 0 and line < num_of_lines and index >= 0 and index < line_length:
        return True
    else:
        return False


def check_location(line,index,antinode_locs):
    valid_location = (line,index)
            
    if valid_location not in antinode_locs:
        return True
        
    else:   
        return False
    

def get_all_locations(lines):
    all_unique_chars_and_locations = {}
    for i in range(0,len(lines)):
        for j in range(0,len(lines[i])):
            each_entry = lines[i][j]
            if each_entry != "\n" and each_entry.strip() != ".":
                if each_entry in all_unique_chars_and_locations.keys():
                    all_unique_chars_and_locations[each_entry] += [(i,j)]

                else: 
                    all_unique_chars_and_locations[each_entry] = [(i,j)]

    print(all_unique_chars_and_locations)
    return all_unique_chars_and_locations
    

if __name__ == '__main__':       
    main()