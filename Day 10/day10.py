def main(data):
    def print_cycle(j, num):
        if j in print_counts:
            xs.append(num)

    lines = data.readlines()
    print_counts = [20, 60, 100, 140, 180, 220]

    x = 1
    xs = []
    cycle = 1
    crt = [[] for _ in range(6)]
    row = 0

    for i in range(len(lines)):
        line = lines[i].strip().split(" ")

        if row == 6:
            break
        print_cycle(cycle, x)
        cycle, crt, row = do_cycle(cycle, x, crt, row)

        if "add" in line[0]:
            print_cycle(cycle, x)
            cycle, crt, row = do_cycle(cycle, x, crt, row)
            x += int(line[1])

    res = sum(map(lambda a: a[0]*a[1], zip(print_counts, xs)))
    print(f"Result Part 1: {res}")
    print(f"Result Part 2:")
    [print(k) for k in crt]


def do_cycle(cycle, x, crt, row):
    crt[row].append("#" if x <= cycle % 40 <= x+2 else ".")
    cycle += 1
    row += 1 if cycle % 40 == 1 else 0
    return cycle, crt, row


file = open("input")
main(file)
