import time

def part1(line):
    line = line.replace("\n","")
    res = 0
    for s in line.split(","):
        res += do_hash(s)
    return res


def do_hash(string):
    res = 0
    for s in string:
        res += ord(s)
        res *= 17
        res = res % 256
    return res

#########################################

def part2(line):
    line = line.replace("\n","")
    hashmap = {}

    for s in line.split(","):
        if s[-1]=="-":
            lens = s[:-1]
            label = do_hash(lens)

            if label in hashmap.keys():
                box = hashmap[label]
                for b in box:
                    if lens in b:
                        box.remove(b)
        else: 
            lens, focal = s.split("=")
            label = do_hash(lens)
            value = (lens, focal)

            if label in hashmap.keys():
                box = hashmap[label]
                found = False
                for i,b in enumerate(box):
                    if lens == b[0]:
                        box[i] = value
                        found = True

                if not found:
                    box.append(value)  
            else:
                hashmap[label] = [value]

        '''print("After ", s)
        for keys,values in hashmap.items():
            print(keys)
            print(values)
        print("-"*10)'''

    return calc_score(hashmap)


def calc_score(hashmap):
    res = 0
    for box in hashmap:
        for j, (_, focal) in enumerate(hashmap[box]):
            val = (box+1) * (j+1) * int(focal)
            res += val
    return res

#########################################

with open('Input/input_15') as input:
    start = time.time()
    lines = input.read()
    print("part 1: ", part1(lines))
    print("part 2: ", part2(lines))
    print("runtime: %ss" % round(time.time() - start, 2))