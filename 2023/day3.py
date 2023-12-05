def part1(m):
    res = 0
    marked = set()
    vals = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]

    for y in range(len(m)):
        for x in range(len(m[0])):
            if not m[y][x].isdigit() and m[y][x] != ".":
                [marked.add((x+i, y+j)) for i,j in vals]

    for y in range(len(m)):
        num = ""
        isMarked = False
        for x in range(len(m[0])):
            if m[y][x].isdigit():
                isMarked = (x,y) in marked or isMarked
                num += m[y][x]
            if not m[y][x].isdigit() or x == len(m[0])-1:
                if not num == "":
                    if isMarked:
                        res += int(num)
                    num = ""
                    isMarked = False
    return res

#########################################

def part2(m):
    res = 0
    gear = 1
    gears = {}
    vals = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]

    for y in range(len(m)):
        for x in range(len(m[0])):
            if m[y][x] == "*":
                for i,j in vals:
                    gears[(x+i, y+j)] = gear
                gear += 1


    gearVals = {}
    for y in range(len(m)):
        num = ""
        isGear = False
        for x in range(len(m[0])):
            if m[y][x].isdigit():
                isGear = (x,y) in gears or isGear
                if (x,y) in gears.keys():
                    gear = gears[(x,y)]
                num += m[y][x]
            if not m[y][x].isdigit() or x == len(m[0])-1:
                if not num == "":
                    if isGear:
                        if gear in gearVals.keys():
                            res += gearVals[gear] * int(num)
                        else:
                            gearVals[gear] = int(num)
                    num = ""
                    isGear = False
    return res

#########################################

with open('Input/input_3') as input:
    lines = input.read().splitlines()
    print("part 1: ", part1(lines))
    print("part 2: ", part2(lines))