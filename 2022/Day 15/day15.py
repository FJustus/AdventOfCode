import re
from time import process_time
from multiprocessing import Pool


def first_better(res_row):
    cantbe = set()
    # print("starting calc...")
    for s in sensors:
        x, y, dist = s

        diff = abs(res_row - y)

        if dist < diff:
            continue
        rest_diff = dist - diff

        for i in range(0, rest_diff+1):
            if x+i <= 4_000_000:
                cantbe.add(x+i)
            if x-i >= 0:
                cantbe.add(x-i)

    # add this for part 1 to be correct
    """for b in beacons:
        if b[0] in cantbe and b[1] == res_row:
            cantbe.remove(b[0])
    for s in sensors:
        if s[0] in cantbe and s[1] == res_row:
            cantbe.remove(s[0])"""

    return cantbe

    # print res
    """for x in range(-4, 27):
        if x in cantbe:
            print("#", end="")
        else:
            print(".", end="")"""


def second(beacons, sensors):
    x_min, x_max = 0, 4_000_000
    y_min, y_max = 0, 4_000_000
    with Pool(4) as pool:
        b = beacons
        s = sensors
        for y in range(y_min, y_max+1):
            pool.apply(calc, args=[y])

    """y_min, y_max = 0, 0
    with Pool(4) as pool:
        l = [y for y in range(y_min, 2)]
        pool.apply(calc, args=(beacons, sensors, l))
        #pool.map(calc, l)"""


def calc(y):
    mult = 4000000
    x_min, x_max = 0, 4_000_000
    print("asdasd")
    cant_be = first_better(y)
    print(f"row:{y}")
    # print(cant_be)
    if len(cant_be) >= x_max - x_min + 1:
        # print("skipping")
        return
    for x in range(x_min, x_max + 1):
        if x not in cant_be:
            print("Result Part 2: x=", x, ", y=", y, "freq:", (x * mult) + y)
            break

def parse(data):
    beacons = set()
    sensors = set()
    for line in data:
        # line = data[0]
        sx, sy, bx, by = re.findall(r"-?\d+", line)
        sx, sy, bx, by = int(sx), int(sy), int(bx), int(by)
        dist = abs(sy - by) + abs(sx - bx)
        # print(f"for sensor {sx}, {sy} with beacon {bx}, {by}, dist: {dist}")

        sensors.add((sx, sy, dist))
        beacons.add((bx, by))
    return beacons, sensors


if __name__ == '__main__':
    test = False
    file = open("test_input" if test else "input").readlines()
    start = process_time()
    beacons, sensors = parse(file)
    second(beacons, sensors)
    print("time: ", process_time() - start)
    # second(file)
