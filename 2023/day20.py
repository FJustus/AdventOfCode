from math import lcm
import time

def part1(lines):

    type = {"%": "flip", "&": "conj", "flip": "%", "conj": "&"}
    broadcast = lines[0].replace(" ", "").split("->")[1].split(",")
    connected = {}
    modules = {}

    for line in lines[1:]:
        start, end = line[1:].replace(" ","").split("->")
        end = end.split(",")
        for e in end:
            if e in connected.keys():
                connected[e].append(start)
            else:
                connected[e] = [start]
        if type[line[0]]=="flip":
            modules[start] = (0, type[line[0]], start, end)
        else:
            modules[start] = ({}, type[line[0]], start, end)

    for m in modules.values():
        if m[1]=="conj":
            modules[m[2]][0].update({c:0 for c in connected[m[2]]})

    modules["rx"] = (0,"rx","rx",0)
    modules["output"] = (0, "out", "out", 0)
    lo = 0
    hi = 0
    # each i a button press
    for i in range(1000):
        Q = []
        # low for button push
        lo += 1
        # low to broadcast
        for b in broadcast:
            Q.append(("B", 0, modules[b]))
        
        while Q:
            sender, signal, (state, type, start, end) = Q.pop(0)
            # for part 2, increase button count to 5k
            if sender=="fn" and signal:
                print(i+1)
            if signal: hi+=1
            else: lo+=1

            if type=="flip" and signal==0:
                state = not state
                signal = state
                
                for e in end:
                    Q.append((start, signal, modules[e]))
                modules[start] = (state, type, start, end)

            elif type=="conj":
                state[sender] = signal
                if all(v==1 for v in state.values()):
                    signal = 0
                else:
                    signal = 1
                for e in end:
                    Q.append((start, signal, modules[e]))

            elif type=="rx" or type=="out":
                continue
    return lo*hi

#########################################

def part2(lines):
    '''
    rx = NAND nc
    nc = lk & fh & hh & fn
    cycles:
    lk: 4003
    fh: 3851
    hh: 4027
    fn: 3847
    LCM: 238815727638557
    '''
    res = lcm(4003,3851,4027,3847)
    return res

#########################################

with open('Input/input_20') as input:
    start = time.time()
    lines = input.read().splitlines()
    print("part 1: ", part1(lines))
    print("part 2: ", part2(lines))
    print("runtime: %ss" % round(time.time() - start, 2))