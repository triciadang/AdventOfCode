import re

def main():
    with open("input.txt") as f:
        lines = f.readlines()

    result = []
    for line in lines:
        result+=(re.findall(r'\d+', line))
    print(result)

    global A
    global B
    global C
    global outputs
    
    A = int(result.pop(0))
    B = int(result.pop(0))
    C = int(result.pop(0))
    outputs = []

    instruction = result
    instruction_map = {}
    

    for i in range(len(instruction)//2):
        instruction_map[i] = (instruction[i*2],instruction[i*2+1])

    first_value = 8**15
    first_value = 37383403556864

    #Tried each range with varying powers of 8 until there was blocks/patterns of correct entries
    #Kept decreasing the range until I could go by 1 efficiently
    
    #First iteration: 8**15, 8**16, 7
    # 36283883716608, 39032662786048, 10
    # 37220186587136, 37222334070784, 6
    # 37221334220800, 37221334974464, 0

    # Answer: 37221334433268

    pow_of_8 = 0
    for i in range(37221334220800,37221334974464,8**pow_of_8):
        print(i)
        A = i

        outputs = []
        find_A(instruction_map)
        if outputs == instruction:
            print(i)
            break

    # tried finding it through each digit
    # match_back_char_index = len(instruction)-1
    # i = match_back_char_index-1
    # starting_value = 8**(len(instruction))
    # reset_value = starting_value
    # A = starting_value
    # outputs = []
    # find_A(instruction_map)

    # while outputs != instruction and i >=0:
    #     print(starting_value)
    #     print(f"match {match_back_char_index}")
    #     print(outputs)

    #     if outputs[match_back_char_index] != instruction[match_back_char_index] or len(outputs)!=len(instruction):
    #         starting_value -= 8**i
    #         A = starting_value

    #     else:
    #         if i == 0:
    #             i = 0
    #         else:
    #             i-=1
    #         print(f"start {starting_value}")
    #         reset_value = starting_value
    #         A = reset_value
    #         match_back_char_index -= 1
    #         if match_back_char_index < 0:
    #             break
            
    #     # if starting_value < 34634616274944:
    #     if starting_value < 0:
    #         print("too low reset")
    #         A = reset_value
    #         print(reset_value)
    #         break
    #         if i == 0:
    #             i = 0
    #         else:
    #             i-= 1
            
    #     outputs = []
    #     find_A(instruction_map)

    # while outputs == instruction:
    #     A=starting_value
    #     outputs = []
    #     find_A(instruction_map)

    #     starting_value -= 1

    # print(starting_value)


def find_A(instruction_map):
    global outputs
    ip = 0

    while ip < len(instruction_map):
        
        opcode,operand = instruction_map[ip]

        match opcode:
            case "0":
                function_0(operand)
            case "1":
                function_1(operand)
            case "2":
                function_2(operand)
            case "3":
                new_ip = function_3(operand)
                if new_ip != -1:
                    ip = new_ip - 1
            case "4":
                function_4(operand)
            case "5":
                function_5(operand)
            case "6":
                function_6(operand)
            case "7":
                function_7(operand)

        ip += 1

    #part 1  
    print(','.join(outputs))
    return
        
def combo_op(operand):
    global A
    global B
    global C

    operand = int(operand)

    if operand == 4:
        operand = A
    elif operand == 5:
        operand = B
    elif operand == 6:
        operand = C


    return operand 

def function_0(operand):
    global A

    operand = combo_op(int(operand))
    denominator = 2**operand
    A = int(A/denominator)
    return 

def function_1(operand):
    global B

    operand = int(operand)
    B = int(B)^operand
    return 

def function_2(operand):
    global B

    operand = combo_op(int(operand))
    B = operand%8
    return 

def function_3(operand):
    global A

    if A == 0:
        return -1
    else:
        return int(operand)

def function_4(operand):
    global B
    global C

    B = B^C
    return

def function_5(operand):
    global outputs

    operand = combo_op(int(operand))
    outputs.append(str(operand%8))
    return

def function_6(operand):
    global A
    global B

    operand = combo_op(int(operand))
    denominator = 2**operand
    B = int(A/denominator)
    return

def function_7(operand):
    global C
    operand = combo_op(int(operand))
    denominator = 2**operand
    C = int(A/denominator)
    return 

if __name__ == '__main__':
    main()