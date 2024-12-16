class Robot:
    def __init__(self, xpos, ypos):
        self.xpos = xpos  # Instance attribute
        self.ypos = ypos  # Instance attribute


def main():
    with open("input.txt") as f:
        lines = f.readlines()

    new_line = lines.index("\n")
    map = []
    directions = []

    for i in range(new_line):
        map.append(list(lines[i].strip()))

    for j in range(new_line+1,len(lines)):
        directions += lines[j]

    # print(part1(lines,map,directions))
    
    new_map = double_map(map)
    part2(new_map,directions)

def part2(new_map,directions):
    print_map(new_map)
    for i in range(0,len(new_map)):
        current_line = new_map[i]
        try:
            index = current_line.index("@")
        except ValueError:
            index = -1

        if index != -1:
            robot = Robot(index,i)
            break
    
    for each_direction in directions:
        print(each_direction)
        new_xpos = robot.xpos
        new_ypos = robot.ypos
        print(new_ypos)

        match each_direction:
            case "<":
                new_xpos -= 1
            case ">":
                new_xpos += 1
            case "^":
                new_ypos -= 1
            case "v":
                new_ypos += 1

        if new_map[new_ypos][new_xpos] == ".":
            new_map[new_ypos][new_xpos] = "@"
            new_map[robot.ypos][robot.xpos] = "."
            robot.ypos = new_ypos
            robot.xpos = new_xpos

        elif new_map[new_ypos][new_xpos] == "[" or new_map[new_ypos][new_xpos] == "]":
            (new_map,robot) = update_map2(new_map,new_ypos,new_xpos,each_direction,robot)

        print_map(new_map)
        
        #else if hit wall, do nothing

    return (calculate_sum(new_map))

def update_map2(map,new_ypos,new_xpos,each_direction,robot):
    box = ["[","]"]
    horiz_dir = [">","<"]
    current_xpos = new_xpos
    current_ypos = new_ypos

    if each_direction in horiz_dir:
        while map[new_ypos][new_xpos] in box:
            match each_direction:
                case "<":
                    diff = -1
                    new_xpos -= 1
                case ">":
                    diff = 1
                    new_xpos += 1

            if map[new_ypos][new_xpos] == "#":
                return (map,robot)
            
            #there is an opening
            if map[new_ypos][new_xpos] == ".":
                while new_xpos != robot.xpos:
                    map[new_ypos][new_xpos] = map[new_ypos][new_xpos - diff]
                    map[new_ypos][new_xpos - diff] = "."
                    new_xpos = new_xpos - diff

        map[current_ypos][current_xpos] = "@"
        robot.ypos = current_ypos
        robot.xpos = current_xpos

    else:
        while map[new_ypos][new_xpos] in box:
            match each_direction:
                case "^":
                    diff = -1
                    new_ypos -= 1
                case "v":
                    diff = 1
                    new_ypos += 1

            if map[new_ypos][new_xpos] == "#":
                return (map,robot)
            
            #there is an opening
            if map[new_ypos][new_xpos] == ".":
                print("plop")
                while new_ypos != robot.ypos:
                    next_char = map[new_ypos-diff][new_xpos]
                    if next_char == "]":
                        map[new_ypos][new_xpos] = map[new_ypos-diff][new_xpos]
                        map[new_ypos][new_xpos-1] = map[new_ypos-diff][new_xpos-1]
                    elif next_char == "[":
                        print("here")
                        map[new_ypos][new_xpos] = map[new_ypos-diff][new_xpos]
                        map[new_ypos][new_xpos+1] = map[new_ypos-diff][new_xpos+1]

                        print_map(map)


        map[current_ypos][current_xpos] = "@"
        robot.ypos = current_ypos
        robot.xpos = current_xpos
        
        

    return (map,robot)


def double_map(map):
    new_map = []
    for each_line in map:
        new_line = []
        for each_entry in each_line:
            match each_entry:
                case "#":
                    new_line += "#"
                    new_line += "#"
                case "O":
                    new_line += "["
                    new_line += "]"
                case ".":
                    new_line += "."
                    new_line += "."
                case "@":
                    new_line += "@"
                    new_line += "."

        new_map.append(new_line)
    return new_map


def part1(lines,map,directions):
    for i in range(0,len(map)):
        current_line = lines[i]
        if current_line.find("@") != -1:
            robot = Robot(i,lines[i].find("@"))
            break

    for each_direction in directions:
        new_xpos = robot.xpos
        new_ypos = robot.ypos

        match each_direction:
            case "<":
                new_xpos -= 1
            case ">":
                new_xpos += 1
            case "^":
                new_ypos -= 1
            case "v":
                new_ypos += 1

        if map[new_ypos][new_xpos] == ".":
            map[new_ypos][new_xpos] = "@"
            map[robot.ypos][robot.xpos] = "."
            robot.ypos = new_ypos
            robot.xpos = new_xpos

        elif map[new_ypos][new_xpos] == "O":
            (map,robot) = update_map(map,new_ypos,new_xpos,each_direction,robot)
        
        #else if hit wall, do nothing

    return (calculate_sum(map))

def calculate_sum(map):
    total = 0
    possible = ["O","[","]"]
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] in possible:
                total += 100*i + j
    return total

def print_map(map):
    for each_line in map:
        print(each_line)
    print("======")
    return
                    
def update_map(map,new_ypos,new_xpos,each_direction,robot):
    current_xpos = new_xpos
    current_ypos = new_ypos

    while map[new_ypos][new_xpos] == "O":
        
        match each_direction:
            case "<":
                new_xpos -= 1
            case ">":
                new_xpos += 1
            case "^":
                new_ypos -= 1
            case "v":
                new_ypos += 1

        if map[new_ypos][new_xpos] == "#":
            return (map,robot)
        
    if map[new_ypos][new_xpos] == ".":
        map[new_ypos][new_xpos] = "O"
        map[current_ypos][current_xpos] = "@"
        map[robot.ypos][robot.xpos] = "."
        robot.ypos = current_ypos
        robot.xpos = current_xpos
        

    return (map,robot)
    

if __name__ == '__main__':
    main()