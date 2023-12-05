def part1(lines):
    res = 0
    ID = 1

    for line in lines:
        line = line.strip().split(":")[1].replace(",", ";").split(";")
        
        max_r, max_g, max_b = 12, 13, 14
        r, g, b = 0, 0, 0

        for x in line:
            match x.split():
                case[num, "blue"]:
                    b = int(num) if int(num) > b else b
                case[num, "red"]:
                    r = int(num) if int(num) > r else r
                case[num, "green"]:
                    g = int(num) if int(num) > g else g
                case _:
                    print("error")

        if r <= max_r and b <= max_b and g <= max_g:
            res += ID

        ID += 1
    return res

#########################################

def part2(lines):
    res = 0
    ID = 1

    for line in lines:
        line = line.strip().split(":")[1].replace(",", ";").split(";")
        
        max_r, max_g, max_b = 0, 0, 0
        r, g, b = 0, 0, 0

        for x in line:
            match x.split():
                case[num, "blue"]:
                    b = int(num) if int(num) > b else b
                case[num, "red"]:
                    r = int(num) if int(num) > r else r
                case[num, "green"]:
                    g = int(num) if int(num) > g else g
                case _:
                    print("error")

        if r > max_r:
            max_r = r
        if g > max_g:
            max_g = g
        if b > max_b:
            max_b = b

        ID += 1
        res += max_r * max_g * max_b

    return res

#########################################

with open('Input/input_2') as input:
    lines = input.readlines()
    print("part 1: ", part1(lines))
    print("part 2: ", part2(lines))