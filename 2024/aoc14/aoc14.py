import re
import matplotlib.pyplot as plt
import numpy as np
import time

def main():

    with open("input.txt") as f:
        lines = f.readlines()

    print(part1(lines))

    tiles_wide = 101
    tiles_tall = 103

    christmas_tree(lines)

def christmas_tree(lines):
    time = 100
    tiles_wide = 101
    tiles_tall = 103
    

    # horiz: 122, 225, 328
    # vert: 70, 171, 272, 373

    for i in range(7241,100000000,101):
        xpoints = np.array([])
        ypoints = np.array([])
        print(i)
        for each_line in lines:
            
            time = i
            match = re.search(r"p\=(-?\d+),(-?\d+) v\=(-?\d+),(-?\d+)",each_line)
            x_pos = int(match.group(1))
            y_pos = int(match.group(2))
            dx = int(match.group(3))
            dy = int(match.group(4))

            new_x = (x_pos + dx * time) % tiles_wide
            new_y = (y_pos + dy * time) % tiles_tall
            # if new_x in xpoints and new_y in ypoints:
            #     print(i)
            #     break

            # else:
            xpoints = np.append(xpoints,(x_pos + dx * time) % tiles_wide)
            ypoints = np.append(ypoints,(y_pos + dy * time) % tiles_tall)

        plt.plot(xpoints, ypoints, 'o')
        plt.show()

    return 


def part1(lines):
    time = 100
    tiles_wide = 101
    tiles_tall = 103
    quad1 = 0
    quad2 = 0
    quad3 = 0
    quad4 = 0
    for each_line in lines:
        match = re.search(r"p\=(-?\d+),(-?\d+) v\=(-?\d+),(-?\d+)",each_line)
        x_pos = int(match.group(1))
        y_pos = int(match.group(2))
        dx = int(match.group(3))
        dy = int(match.group(4))

        new_xpos = (x_pos + dx * time) % tiles_wide
        new_ypos = (y_pos + dy * time) % tiles_tall

        halfway_x = ((tiles_wide + 1)/2)-1
        halfway_y = ((tiles_tall + 1)/2)-1

        if new_xpos > halfway_x:
            if new_ypos < halfway_y:
                quad2 += 1
            elif new_ypos > halfway_y:
                quad4 += 1
        if new_xpos < halfway_x:
            if new_ypos > halfway_y:
                quad3 += 1
            elif new_ypos < halfway_y:
                quad1 += 1

    return(quad1 * quad2 * quad3 * quad4)

if __name__ == '__main__':
    main()