from time import perf_counter

def first(data):
    res = [line.split("\n") for line in data.split("\n\n")]
    res = [evaluate_order(pair, i+1) for i, pair in enumerate(res)]

    #print(f"res: {res}")
    print(f"Result Part 1: {sum([r for r in res if r])}")


def second(data):
    lines = list(filter(None, (line.strip() for line in data)))
    lines = [eval(line) for line in lines]
    lines.append([[2]])
    lines.append([[6]])

    # BubbleSort
    n = len(lines)
    swapped = False
    for i in range(n-1):
        for j in range(n-i-1):
            if not compare_order(lines[j], lines[j+1]):
                swapped = True
                lines[j], lines[j+1] = lines[j+1], lines[j]

        if not swapped:
            break

    #[print(line) for line in lines]
    f = lines.index([[2]]) + 1
    s = lines.index([[6]]) + 1
    #print("f:", f, ", s:", s)
    print("Result Part2: ", s*f)

def evaluate_order(pair, num):
    c1, c2 = eval(pair[0]), eval(pair[1])

    if compare_order(c1, c2):
        #print(f"{num} was legit")
        return num
    #print(f"{num} was not legit")

def compare_order(l: list, r: list, first=False):

    #print(f"compare {l} and {r}")
    # if identical
    if l == r:
        return None
    elif l is None: return True
    elif r is None: return False
    # if both list
    elif isinstance(l, list) and isinstance(r, list):
        i = 0
        res = None
        while res is None:
            if i >= len(l):
                return None if i >= len(r) else True
            elif i >= len(r): return False
            res = compare_order(l[i], r[i])
            i += 1
        return res
    # if list and int
    elif isinstance(l, list) and isinstance(r, int):
        return compare_order(l, [r])
    # if int and list
    elif isinstance(l, int) and isinstance(r, list):
        return compare_order([l], r)
    #if int and int
    elif isinstance(l, int) and isinstance(r, int):
        if r < l: return False
        elif l < r: return True
        else:
            #print("None")
            return None

    return True


use_test = False
with open("test_input" if use_test else "input") as file:
    # first(file)
    start_time_two = perf_counter()
    second(file)
    print(round((perf_counter() - start_time_two)*1e3, 2), "ms")
