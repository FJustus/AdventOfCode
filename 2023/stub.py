import time

def part1(lines):
    res = 0
    return res

#########################################

def part2(lines):
    res = 0
    return res

#########################################

with open('Input/input_test') as input:
    start = time.time()
    lines = input.read().splitlines()
    print("part 1: ", part1(lines))
    print("part 2: ", part2(lines))
    print("runtime: %ss" % round(time.time() - start, 2))