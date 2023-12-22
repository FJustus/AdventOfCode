from functools import cache
import time


def part1(lines):
    #print("vorher: ")
    #print(*lines, sep="\n")
    field = tilt_north(lines)
    #print("nacher: ")
    #print(*field, sep="\n")
    res = calc_load(field)
    return res


def tilt_east(field):
    new_field = []
    for row in field:
        O_num = 0
        new_line = ""
        for c in row:
            if c == ".":
                new_line += "."
            elif c == "O":
                O_num += 1
            elif c == "#":
                new_line += "O" * O_num
                new_line += "#"
                O_num = 0
        new_line += "O" * O_num
        new_field.append(new_line)
    return new_field


def tilt_north(field):
    flipped = list(zip(*field))
    flipped = [reversed(l) for l in flipped]
    flipped = tilt_east(tuple(flipped))
    flipped = [reversed(l) for l in flipped]
    field = list(zip(*flipped))
    return field


def tilt_south(field):
    flipped = list(zip(*field))
    flipped = tilt_east(tuple(flipped))
    field = list(zip(*flipped))
    return field


def tilt_west(field):
    rev = [reversed(l) for l in field]
    rev = tilt_east(tuple(rev))
    return [reversed(l) for l in rev]


def calc_load(field):
    return sum(sum(len(f)-idx for c in f if c=="O") for idx, f in enumerate(field))

#########################################

def part2(lines):
    res = []
    c = 1_000_000_000

    for i in range(c):
        lines = tilt_north(lines)
        lines = tilt_west(lines)
        lines = tilt_south(lines)
        lines = tilt_east(lines)
        
        if lines in res:
            cycle_start = res.index(lines)
            cycle_length = i - cycle_start
            offset = (c-1 - i) % cycle_length + cycle_start
            return calc_load(res[offset])
        else:
            res.append(lines)

#########################################

with open('Input/input_14') as input:
    start = time.time()
    lines = input.read().splitlines()
    print("part 1: ", part1(lines))
    print("part 2: ", part2(lines))
    print("runtime: %ss" % round(time.time() - start, 2))