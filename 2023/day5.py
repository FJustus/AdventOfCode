def part1(lines):
    res = []
    seeds = list(map(int, lines[0].split(":")[1].split()))
    lines = lines[3:]
    transformer = []
    filler = []
    
    for line in lines:
        if line == "":
            continue
        if ":" in line:
            transformer.append(filler)
            filler = []
        else:
            filler.append(list(map(int, line.split())))
    transformer.append(filler)

    for seed in seeds:
        for trafo in transformer:
            for end, start, r in trafo:
                if seed >= start and seed <= start + r:
                    seed = end + seed - start
                    break
        res.append(seed)

    return min(res)

#########################################

def part2(lines):
    seeds = []
    seed_vals = lines[0].split(":")[1].split()
    for i in range(0,len(seed_vals),2):
        seeds.append([int(seed_vals[i]), int(seed_vals[i+1])])

    lines = lines[3:]
    transformer = []
    filler = []
    for line in lines:
        if line == "":
            continue
        if ":" in line:
            transformer.append(filler)
            filler = []
        else:
            filler.append(list(map(int, line.split())))
    transformer.append(filler)

    location = 0
    delta = 100000
    while check_location(location, transformer, seeds) < 0:
        location+=delta

    location -= delta
    while check_location(location, transformer, seeds) < 0:
        location+=1
    return location
    

def in_seeds(x, seed_pairs):
    for pair in seed_pairs:
        if x >= pair[0] and x <= pair[0]+pair[1]:
            return True
    return False


def check_location(location, transformer, seeds):
    tmp = location
    for trafo in transformer[::-1]:
        for end, start, r in trafo:
            if tmp >= end and tmp < end + r:
                tmp = start + tmp - end
                break
    return tmp if in_seeds(tmp, seeds) else -1



#########################################

with open('Input/input_5') as input:
    lines = input.read().splitlines()
    print("part 1: ", part1(lines))
    print("part 2: ", part2(lines))