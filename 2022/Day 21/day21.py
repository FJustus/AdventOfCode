def first(lines):
    vals = {}
    for line in lines:
        (key, val) = line.replace(" ", "").strip().split(":")
        vals[key] = val

    res = evaluate(vals, "root")
    print("Result Part 1:" , res)


def evaluate(vals, start):
    match = ["+", "-", "*", "/"]

    val = vals[start]
    sign = None
    if "+" in val:
        a, b = val.split("+")
        return evaluate(vals, a) + evaluate(vals, b)
    elif "-" in val:
        a, b = val.split("-")
        return evaluate(vals, a) - evaluate(vals, b)
    elif "*" in val:
        a, b = val.split("*")
        return evaluate(vals, a) * evaluate(vals, b)
    elif "/" in val:
        a, b = val.split("/")
        return evaluate(vals, a) / evaluate(vals, b)
    else:
        return int(val)


file = open("input")
first(file.readlines())
