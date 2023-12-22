import math
import operator
import time
import re

def part1_2(lines):
    rules = {}
    default = {}
    # parse rules
    for idx, line in enumerate(lines):
        if line=="":
            lines = lines[idx+1:]
            break
        name, s = line.split("{")
        rules[name] = []
        s = s.replace("}", "").split(",")
        for rule in s:
            if rule == s[-1]: 
                default[name] = rule
                continue

            start = rule[0]
            op = operator.lt if rule[1] == "<" else operator.gt
            value = int(rule.split(":")[0][2:])
            to = rule.split(":")[1]
            rules[name].append((start, op, value, to))

    # parse input
    Q = []
    for line in lines:
        line = line.replace("{","").replace("}","")
        part = {}
        for pair in line.split(","):
            name, val = pair.split("=")
            part[name] = int(val)
        Q.append((part, "in"))

    # for q in Q: apply rules until A or R
    accepted = []

    while Q:
        part, rule = Q.pop(0)
        if rule=="A":
            accepted.append(part)
            continue
        elif rule=="R":
            continue

        finished = False
        for (sign, op, value, to) in rules[rule]:
            if op(part[sign], value):
                finished = True        
                if to!="R":
                    Q.append((part, to))
                break
        if not finished:
            Q.append((part, default[rule]))

    interval = {'x': (1,4000), 'm': (1,4000), 'a': (1,4000), 's': (1,4000)}
    res2 = find(rules, default, "in", interval)

    return sum(sum(i.values()) for i in accepted), res2

#########################################

def find(rules, default, start, interval):
    res = 0
    Q = [(interval, start)]

    while Q:
        interval, name = Q.pop()
        if name=="A":
            total = 1
            #print("adding", interval)
            for lo, hi in interval.values():
                total *= (hi-lo+1)
            res += total
            continue
        elif name=="R":
            continue
        
        for (start, op, value, to) in rules[name]:
            lo, hi = interval[start]

            # none gets transfered
            if (op==operator.lt and lo>=value) or op==operator.gt and hi<=value:
                continue
            # all gets transfered
            elif (op==operator.lt and hi<value) or (op==operator.gt and lo>value):
                Q.append((interval, to))
                break
            # split
            if op==operator.gt:
                transfer = (value+1, hi)
                cont = (lo, value)
            else:
                transfer = (lo, value-1)
                cont = (value, hi)

            interval[start] = cont
            interval2 = interval.copy()
            interval2[start] = transfer

            Q.append((interval2, to))

        Q.append((interval, default[name]))

    return res

#########################################

with open('Input/input_19') as input:
    start = time.time()
    lines = input.read().splitlines()
    a, b = part1_2(lines)
    print("part 1: ", a, ", part 2: ", b)
    print("runtime: %ss" % round(time.time() - start, 3))