import time


def part1(fields):
    res = 0

    for field in fields:
        field = field.splitlines()

        res += check(field) * 100

        flipped = [x for x in zip(*field)]
        res += check(flipped)

    return res

def check(field):
    res = 0

    for idx in range(1,len(field)):

        if all(field[idx-i] == field[idx+i-1] for i in range(1, 1+min(idx, len(field)-idx))):
            res+=idx
    return res

#########################################


def check_2(field):
    res = 0

    for idx in range(1,len(field)):
        if sum(diff(field[idx-i], field[idx+i-1]) for i in range(1, 1+min(idx, len(field)-idx))) == 1:
            res+=idx
            break
    return res


def diff(a, b):
    return sum(a[i]!=b[i] for i in range(len(a)))


def part2(fields):
    res = 0

    for field in fields:
        field = field.splitlines()

        res += check_2(field) * 100
        flipped = [x for x in zip(*field)]
        res += check_2(flipped)

    return res

#########################################

with open('Input/input_13') as input:
    start = time.time()
    lines = input.read().split("\n\n")
    print("part 1: ", part1(lines))
    print("part 2: ", part2(lines))
    print("runtime: %ss" % round(time.time() - start, 4))
