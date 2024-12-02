from shapely.geometry import LineString

def day24():
    f = open("input24.txt","r")
    flines = f.readlines()
    checkIntersection(flines)


def checkIntersection(lines):
    posArray = []
    velArray = []

    for i in range(0,len(lines)):
        temp_line = lines[i].strip("\n").split("@")

        posArray += [temp_line[0]]
        velArray += [temp_line[1]]

    minX = 200000000000000
    maxX = 400000000000000

    # y = mx + b = slope intercept form
    # y = (1/-2)x + b
    # b = y - (1/-2)x

    total = 0
    for i in range(0,len(posArray)-1):
        
        for j in range(i+1,len(posArray)):
            
            #first line
            position1 = posArray[i].strip(" ").split(",")

            velocity1 = velArray[i].strip(" ").split(",")

            
            y1 = int(position1[1])
            x1 = int(position1[0])

            m1 = (int(velocity1[1])/int(velocity1[0]))

            b1 = y1 - (m1 * x1)
            #x as zero
            minLine1 = m1*minX + b1
            maxLine1 = m1*maxX + b1


            line1 = LineString([(minX,minLine1),(maxX,maxLine1)])

            #second line
            position2 = posArray[j].strip(" ").split(",")

            velocity2 = velArray[j].strip(" ").split(",")

            
            y2 = int(position2[1])
            x2 = int(position2[0])

            m2 = (int(velocity2[1])/int(velocity2[0]))

            b2 = y2 - (m2 * x2)
            #x as zero
            minLine2 = m2*minX + b2
            maxLine2 = m2*maxX + b2

            #print(b)
            line2 = LineString([(minX,minLine2),(maxX,maxLine2)])

            if line1.intersects(line2):
                p = line1.intersection(line2)
                calculateTimeToGetToMinX1 = (p.y-y1)/(int(velocity1[1]))
                calculateTimeToGetToMinX2 = (p.y-y2)/(int(velocity2[1])) 
                if calculateTimeToGetToMinX1 >= 0 and calculateTimeToGetToMinX2 >= 0: 
                    if p.y >= minX and p.y <= maxX:
                        total += 1


    print(total)
    return total





day24()