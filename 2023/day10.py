import math

loop_parts = {}
def part1(m):
    res = 0

    types = {
        (0,-1):"|F7",
        (0,1):"|JL",
        (1,0):"-7J",
        (-1,0):"-FL"
    }
    ways = {
        "|": [(0,1),(0,-1)],
        "F": [(0,1),(1,0)],
        "7": [(-1,0),(0,1)],
        "J": [(0,-1),(-1,0)],
        "L": [(0,-1),(1,0)],
        "-": [(1,0),(-1,0)],
        "S": [(0,1),(0,-1),(1,0),(-1,0)]
    }

    prev = (-1,-1)
    current = ()
    start = ()

    for y, row in enumerate(m):
        for x, p in enumerate(row):
            if p=="S":
                start = (int(x),int(y))
                loop_parts[start] = 0
                current = start

    while 1:
        for d in ways[m[current[1]][current[0]]]:
            test = (current[0]+d[0], current[1]+d[1])
            if test == prev:
                continue
            elif m[test[1]][test[0]] == "S":
                return int((res+1)/2)

            if m[test[1]][test[0]] in types[d]:
                res+=1
                prev = current
                current = test
                loop_parts[current] = res
                break
#########################################

def part2(lines):
            
    res = 0
    for y, row in enumerate(lines):
        is_enclosed = False

        for x, part in enumerate(row):
            if (x,y) in loop_parts:
                if part not in "S-JL":
                    is_enclosed = not is_enclosed

            elif is_enclosed:
                res+=1
    return res

#########################################

with open('Input/input_10') as input:
    lines = input.read().splitlines()
    print("part 1: ", part1(lines))
    print("part 2: ", part2(lines))

# part2
# transform into ...
# go line by line
# if crossed loop tiles number uneven -> inside