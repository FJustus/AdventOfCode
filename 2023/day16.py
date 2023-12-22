from functools import cache
import sys
import time

directions = {
    "L": (-1,0),
    "R": (1,0),
    "U": (0,-1),
    "D": (0,1)
}
# /
turnTilde = {
    (-1,0): "D",
    (0,1): "L",
    (1,0): "U",
    (0,-1): "R",
}
# \
turnBackslash = {
    (-1,0): "U",
    (0,1): "R",
    (1,0): "D",
    (0,-1): "L",
}

def part1(m, start, direction):
    #energized = set()

    sys.setrecursionlimit(5000)
    
    seen = follow_beam(tuple(m), start, direction, {})

    '''for y in range(max_y):
        for x in range(max_x):
            if (x,y) in seen:
                print("#",end="")
            else:
                print(".", end="")
        print("") '''

    return len(seen)


def follow_beam(m, s, d, seen):
    pos = (s[0]+d[0], s[1]+d[1])
    max_x = len(m[0])
    max_y = len(m)
    #print("seen: ", seen)
    if pos[0]<0 or pos[0]>=max_x or pos[1]<0 or pos[1]>=max_y:
        return seen
    if pos in seen and d in seen[pos]:
        return seen

    if pos in seen:
        seen[pos].append(d)
    else:
        seen[pos] = [d]
    char = m[pos[1]][pos[0]]

    #print(char)

    if char == "|" and (d==directions["L"] or d==directions["R"]):
        return (follow_beam(m, pos, directions["U"], seen) | follow_beam(m, pos, directions["D"], seen))
    elif char == "-" and (d==directions["U"] or d==directions["D"]):
        return (follow_beam(m, pos, directions["L"], seen) | follow_beam(m, pos, directions["R"], seen))
    elif char == "\\":
        return follow_beam(m, pos, directions[turnBackslash[d]], seen)
    elif char == "/":
        return follow_beam(m, pos, directions[turnTilde[d]], seen)
    elif char == "." or (char=="-" and d[1]==0) or (char=="|" and d[0]==0):
        return follow_beam(m, pos, d, seen)

#########################################

def part2(m):
    res = []

    for y in range(len(m)):
        start = (-1,y)
        direction = (1,0)
        res.append(len(follow_beam(tuple(m), start, direction, {})))
        start = (len(m),y)
        direction = (-1,0)
        res.append(len(follow_beam(tuple(m), start, direction, {})))


    for x in range(len(m[0])):
        start = (x,-1)
        direction = (0,1)
        res.append(len(follow_beam(tuple(m), start, direction, {})))
        start = (x, len(m))
        direction = (0,-1)
        res.append(len(follow_beam(tuple(m), start, direction, {})))
    
    return max(res)

#########################################

with open('Input/input_16') as input:
    start = time.time()
    lines = input.read().splitlines()
    print("part 1: ", part1(lines, (-1,0), (1,0)))
    print("part 2: ", part2(lines))
    print("runtime: %ss" % round(time.time() - start, 2))