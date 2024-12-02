import numpy as np

def day9():
    f = open("input9.txt", "r")
    flines = f.readlines()

    patternFinder(flines)

def patternFinder(lines):
    sum = 0
    allHistory = []
    patternMap = {}
    for i in range(0,len(lines)):
        if lines[i] != "\n":
            temp_line = lines[i].split()
            bigDiffArray = []
            
            diffArray = []
            for each_int in temp_line:
                diffArray.append(int(each_int))
            print(diffArray)    
            
            bigDiffArray += [diffArray]

            i=0
            while np.any(diffArray):
                diffArray = []
                for j in range(0,len(bigDiffArray[i])-1):
                    x = bigDiffArray[i][j+1]
                    y = bigDiffArray[i][j]

                    diffArray.append(int(x)-int(y))

                bigDiffArray += [diffArray]
                i += 1
            
            difference = 0
            for k in range(len(bigDiffArray)-1,0,-1):
                difference = bigDiffArray[k-1][0]-difference

                #print(difference)

            sum += difference

            print(sum)
            

day9()