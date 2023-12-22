import time

directions = {
    "L": (-1,0),
    "R": (1,0),
    "U": (0,-1),
    "D": (0,1),
    "0": "R",
    "1": "D",
    "2": "L",
    "3": "U"
}

def part1_2(lines, gen):
    points = []
    current = (0,0)
    points.append(current)
    max_x = 0
    min_x = 0
    max_y = 0
    min_y = 0
    circ = 0

    for dir, num in gen(lines):
        newPoint = (current[0]+int(num)*dir[0], current[1]+int(num)*dir[1])
        max_x = max(newPoint[0], max_x)
        max_y = max(newPoint[1], max_y)
        min_x = min(newPoint[0], min_x)
        min_y = min(newPoint[1], min_y)

        circ += abs(newPoint[1]-current[1]) + abs(newPoint[0]-current[0])
        points.append(newPoint)
        current = newPoint
        
        current = newPoint

    '''for y in range(min_y,max_y+1):
        for x in range(min_x,max_x+1):
            if (x,y) in points:
                print("#",end="")
            else:
                print(".",end="")
        print("")'''

    p = points
    A = 0

    for i in range(len(p)-1):
        p1 = p[i]
        p2 = p[i+1]
        A += (p1[1] + p2[1]) * (p1[0] - p2[0])

    return int((0.5 * A) + (circ / 2) + 1)


def gen_p1(m):
    for l in m:
        dir, num, col = l.split()
        yield directions[dir], num

def gen_p2(m):
    for l in m:
        dir, num, col = l.split()
        col = col.replace("(","").replace(")","").replace("#","")
        dir = directions[directions[col[-1]]]
        num = int(col[:-1], 16)
        yield dir, num

#########################################

with open('Input/input_18') as input:
    start = time.time()
    lines = input.read().splitlines()
    print("part 1: ", part1_2(lines, gen_p1))
    print("part 2: ", part1_2(lines, gen_p2))
    print("runtime: %ss" % round(time.time() - start, 2))