def part1and2(m, to_add):
    m = [list(s) for s in m]
    res = 0
    empty_row = []
    empty_col = []
    galaxies = []

    flipped = [list(a) for a in zip(*m)]
    [empty_col.append(idx) for idx, r in enumerate(flipped) if all(i=="." for i in r)]

    # find galaxy locations
    count = 0
    for y, r in enumerate(m):
        empty = True
        for x, c in enumerate(r):
            if c=="#":
                galaxies.append((x,y))
                m[y][x] = count
                count+=1
                empty = False
        if empty:
            empty_row.append(y)

    def x_dist(x1, x2):
        return sum(to_add for x in empty_col if x < max(x1,x2) and x > min(x1, x2)) + abs(x1-x2)
    def y_dist(y1, y2):
        return sum(to_add for x in empty_row if x < max(y1,y2) and x > min(y1, y2)) + abs(y1-y2)

    # find distances
    for galaxy_num, galaxy in enumerate(galaxies):
        for i in range(galaxy_num+1, len(galaxies)):
            other_galaxy = galaxies[i]
            res += x_dist(galaxy[0], other_galaxy[0]) + y_dist(galaxy[1], other_galaxy[1])

    return res

#########################################

def part2(lines):
    res = 0
    return res

#########################################

with open('Input/input_11') as input:
    lines = input.read().splitlines()
    print("part 1: ", part1and2(lines, 1))
    print("part 2: ", part1and2(lines, 999999))