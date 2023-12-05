
def parse(data):
    # parse input
    y_max = 0
    y_floor = 0
    blocked = set()
    for line in data:
        coords = [l.split(",") for l in line.strip().split(" -> ")]

        for i in range(len(coords)-1):
            ox, oy, nx, ny = int(coords[i][0]), int(coords[i][1]), int(coords[i+1][0]), int(coords[i+1][1])
            if oy > y_max: y_max = oy
            elif ny > y_max: y_max = ny

            if ox == nx:
                if oy < ny:
                    [blocked.add((ox, y)) for y in range(oy, ny+1)]
                else:
                    [blocked.add((ox, y)) for y in range(ny, oy+1)]
            else:
                if ox < nx:
                    [blocked.add((x, oy)) for x in range(ox, nx+1)]
                else:
                    [blocked.add((x, oy)) for x in range(nx, ox+1)]

    y_floor = y_max + 2
    print("blocked:", blocked)
    print("no of blocks:", len(blocked))
    print("y_max: ", y_max)
    return blocked, y_max, y_floor


def first(blocked, y_max, y_floor):
    # determine lower limit y
    sand_start = (500, 0)
    sand_counter = 0

    # produce sand until it would fall off
    while True:
        x, y = sand_start

        # follow sandpath till its blocked
        while True:
            # update pos till no update possible or
            ox, oy = x, y
            for (nx, ny) in (x, y+1), (x-1, y+1), (x+1, y+1):
                if (nx, ny) in blocked: continue
                x, y = nx, ny
                break
            if (ox, oy) == (x, y) or y == y_max:
                break
        if y == y_max:
            break
        blocked.add((x, y))
        sand_counter += 1

    print("Result Part 1: ", sand_counter)


def second(blocked, y_max, y_floor):
    # determine lower limit y
    sand_start = (500, 0)
    sand_counter = 0

    # produce sand until it would fall off
    while True:
        #print("newsand no", sand_counter)
        x, y = sand_start

        # follow sandpath till its blocked
        while True:
            # update pos till no update possible or
            ox, oy = x, y
            for (nx, ny) in (x, y + 1), (x - 1, y + 1), (x + 1, y + 1):
                if (nx, ny) in blocked or ny == y_floor: continue
                x, y = nx, ny
                break
            #print("new x, y: ", x, y)
            if (ox, oy) == (x, y) or y == y_floor:
                break

        blocked.add((x, y))
        sand_counter += 1
        if y == 0:
            break

    print("Result Part 2: ", sand_counter)


test = False
file = open("test_input" if test else "input").readlines()
first(*parse(file))
second(*parse(file))
