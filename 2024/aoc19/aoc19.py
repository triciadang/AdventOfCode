import functools

def main():
    with open("input.txt") as f:
        all_chunks, phrases = f.read().split("\n\n")

    global chunk_list
    chunk_list = all_chunks.split(", ")
    phrase_list = phrases.split("\n")

    overall_count = 0
    phrase_count = 0

    for each_phrase in phrase_list:
        if check_function(each_phrase):
            phrase_count += 1
            overall_count += (part_2(each_phrase))
            
    print(phrase_count)
    print(overall_count)

@functools.cache
def check_function(entry):
    global chunk_list
    if len(entry)==0:
        return True
    else:
        for each_chunk in chunk_list:
            if entry.startswith(each_chunk):
                if check_function(entry.removeprefix(each_chunk)):

                    return True
                    
    return False

@functools.cache
def part_2(entry):
    global chunk_list
    if len(entry)==0:
        return 1
    else:
        count = 0
        for each_chunk in chunk_list:
            if entry.startswith(each_chunk):
                count += part_2(entry.removeprefix(each_chunk))
                    
    return count

if __name__ == '__main__':
    main()
