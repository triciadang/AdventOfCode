import re
from sympy import symbols, Eq, solve, core

def main():

    with open('input.txt') as f:
        lines = f.readlines()

    filtered_list = []
    
    for i in range(0,len(lines)):
        line = lines[i]
        if len(line.strip()) != 0:
            filtered_list.append(line.strip())

    number_of_games = int(len(filtered_list)/3)
    
    part1 = 0
    part2 = 0
    for i in range(0,number_of_games):

        a_btn = filtered_list[3*i]
        b_btn = filtered_list[3*i+1]
        prize = filtered_list[3*i+2]

        part1 += find_cost(a_btn,b_btn,prize,False)
        

        part2 += find_cost(a_btn,b_btn,prize,True)
        

    print(f"Total Part1 Cost: {part1}")
    print(f"Total Part2 Cost: {part2}")


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

    a,b = symbols('a,b')

    eq1 = Eq((a_dx * a + b_dx * b), prize_x)
    eq2 = Eq((a_dy * a + b_dy * b), prize_y)
             
    result = solve((eq1,eq2),(a,b))

    a = (result[a])
    b = (result[b])

    if isinstance(a,core.numbers.Integer) and isinstance(b,core.numbers.Integer):
        total_min += a * 3 + b

    return total_min

if __name__ == '__main__':
    main()