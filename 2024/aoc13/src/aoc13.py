import re
import numpy as np

def main():

    with open('input.txt') as f:
        lines = f.readlines()

    filtered_list = []
    
    for i in range(0,len(lines)):
        line = lines[i]
        if len(line.strip()) != 0:
            filtered_list.append(line.strip())

    number_of_games = int(len(filtered_list)/3)
    

    for i in range(0,number_of_games):

        a_btn = filtered_list[3*i]
        b_btn = filtered_list[3*i+1]
        prize = filtered_list[3*i+2]

        part1 = find_cost(a_btn,b_btn,prize,False)
        print(f"Total Cost: {part1}")

        # part2 = find_cost(a_btn,b_btn,prize,True)
        # print(f"Total Cost: {part2}")



def find_cost(a_btn, b_btn, prize,part2):
    total_min = 0

    match = re.search(r"Button A: X\+(\d+), Y\+(\d+)",a_btn)
    a_dx = int(match.group(1))
    a_dy = int(match.group(2))

    match = re.search(r"Button B: X\+(\d+), Y\+(\d+)",b_btn)
    b_dx = int(match.group(1))
    b_dy = int(match.group(2))

    match = re.search(r"Prize: X\=(\d+), Y\=(\d+)",prize)
    prize_x = int(match.group(1))
    prize_y = int(match.group(2))
    if part2:
        prize_x += 10000000000000
        prize_y += 10000000000000

    left_side = np.array([[a_dx,a_dy],[b_dx,b_dy]])
    right_side = np.array([prize_x,prize_y])

    # x_difference = a_dx + a_dy
    # y_difference = b_dx + b_dy
    # prize_diff = prize_x + prize_y

    min_price = None
    print(np.linalg.inv(left_side).dot(right_side))

        # num_x = prize_diff / x_difference

    # for a in range(int(num_x)):
        
    #     if (int(prize_diff - (x_difference*a)) % y_difference) == 0:

    #         b = int((prize_diff - (x_difference*a)) // y_difference)

    #         if 0 <= b:
    #             price = a * 3 + b

    #             if (a*a_dx + b*b_dx - prize_x == 0) and (a*a_dy + b*b_dy - prize_y == 0) :

    #                 if min_price is None or 0 <= price <  min_price:
    #                     print(a,b)
    #                     min_price = price

    # if min_price is not None:
    #     total_min += min_price

    return total_min

if __name__ == '__main__':
    main()