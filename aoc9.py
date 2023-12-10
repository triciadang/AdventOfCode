def day9():
    f = open("input9.txt", "r")
    flines = f.readlines()

    patternFinder(flines)

def patternFinder(lines):
    allHistory = []
    patternMap = {}
    for i in range(0,len(lines)):
        if lines[i] != "\n":
            temp_line = lines[i].split()
            print(temp_line)
            



day9()