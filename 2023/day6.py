import math

def part1(lines):
    res = 0
    timedist = list(zip(map(int, lines[0].split()[1:]), map(int, lines[1].split()[1:])))

    for time, dist in timedist:
        count = 0
        for i in range(1,time):
            charge, race = i, time - i
            if race * charge > dist:
                count += 1

        res = res*count if res > 0 else count
    return res

#########################################

def part2(lines):
    time = int(lines[0].split(":")[1].replace(" ", ""))
    dist = int(lines[1].split(":")[1].replace(" ", ""))

    for i in range(0,time+1):
        charge, race = i, time - i

        if race * charge > dist:
            return time+1 - (2*i)        

    return 0


def part2_alt(lines):
    t = int(lines[0].split(":")[1].replace(" ", ""))
    m = int(lines[1].split(":")[1].replace(" ", ""))

    dist_1 = math.ceil((-t+math.sqrt(t**2-4*m))/-2)
    dist_2 = math.ceil((-t-math.sqrt(t**2-4*m))/-2)

    return abs(dist_2-dist_1)

#########################################

def parse_input(lines):
    return lines

with open('Input/input_6') as input:
    lines = input.read().splitlines()
    #print("part 1: ", part1(parse_input(lines)))
    #print("part 2: ", part2(parse_input(lines)))
    print("part 2: ", part2_alt(parse_input(lines)))