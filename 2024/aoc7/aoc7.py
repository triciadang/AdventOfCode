from itertools import product


def main():
    with open("input.txt") as f:
        lines = f.readlines()

    working = 0

    for each_line in lines:
        print(each_line)
        result = each_line.split(":")

        answer_req = (int)(result[0])
        numbers = result[1]
        num_array = numbers.split()
        num_array = [item.strip() for item in num_array]

        if test_number(num_array.copy(),answer_req):
            working += answer_req

        else:
            if test_number_w_concat(num_array.copy(),answer_req):
                working += answer_req

    print(working)



def test_number_w_concat(num_array,answer_req):
    combs = build_possibilities_arrays(len(num_array))
    
    for each_possibility in combs:

        current = num_array[0]
        for i in range(1,len(num_array)):
            each_entry = each_possibility[i-1]
            if each_entry == "*":
                current = int(current) * int(num_array[i])
            elif each_entry == "+":
                current = int(current) + int(num_array[i])
            elif each_entry == "||":
                current = str(current) + str(num_array[i])

            current = int(current)
            
        if current == answer_req:
            return True

    return False

def build_possibilities_arrays(length_of_array):
    possibilities = ["*","+","||"]
    perms = []

    perms = list(product(possibilities,repeat=(length_of_array-1)))

    return perms


  

def test_number(num_array,answer_req):
    if len(num_array) == 0:
        return False

    last_element = (int)(num_array.pop())
        
    if answer_req%last_element == 0:
        new_answer_req = answer_req/last_element
        if new_answer_req == 1 and len(num_array) == 0:
            return True
        elif test_number(num_array[:],new_answer_req):
            return True


    new_answer_req =  answer_req-last_element
    if new_answer_req == 0 and len(num_array) == 0:
        return True
    elif test_number(num_array[:],new_answer_req):
        return True
    
    return False
        
    

        
main()