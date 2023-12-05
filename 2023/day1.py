
def part1(input):
    return sum(intOnly(i) for i in lines)

#######################################################################

def part2(lines):
    sum = 0
    for line in lines:
        val = intOnly(parseLine(line))
        print("added: ", val)
        sum += val
    return sum

#######################################################################

def intOnly(s):
    res = ""
    for c in s:
        res += c if c.isdigit() else ""
    return int(res[::len(res)-1]) if len(res)>1 else int(res + res)


def parseLine(line):
    replacer = {"one": "o1e",
                "two": "t2o",
                "three": "t3e",
                "four": "f4r",
                "five": "f5e",
                "six": "s6x",
                "seven": "s7n",
                "eight": "e8t",
                "nine": "n9e" }

    for i in replacer:
        line = line.replace(i, replacer[i])
    return line

with open('Input/input_1') as input:
    lines = input.readlines()
    print(part1(lines))
    print(part2(lines))