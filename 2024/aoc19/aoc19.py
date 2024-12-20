import functools
from itertools import permutations


def main():
    with open("input.txt") as f:
        all_chunks, phrases = f.read().split("\n\n")

    global chunk_list
    chunk_list = all_chunks.split(", ")
    phrase_list = phrases.split("\n")

    global max_length
    max_length = 0
    for each in chunk_list:
        if len(each) > max_length:
            max_length = len(each)

    phrase_count = 0

    for each_phrase in phrase_list:
        print(each_phrase)
        if check_function(each_phrase):
             phrase_count += 1

            
    print(phrase_count)

@functools.cache
def check_function(entry):
    queue = [entry]
    while len(queue) != 0:
        entry = queue.pop()
        for i in range(max_length,0,-1):
            if entry[0:i] in chunk_list:
                if entry[i:] == '':
                    chunk_list.append(entry[0:i])
                    queue = []
                    return True
                else:
                    queue.append(entry[i:])

    return False

    print(phrase_count)
if __name__ == '__main__':
    main()
