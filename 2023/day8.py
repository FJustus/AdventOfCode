from functools import reduce
import math

def part1(lines):
    directions = [int(x) for x in list(lines[0].replace("L", "0").replace("R", "1"))]
    lines = lines[2:]
    nodes = {}

    for line in lines:
        a = "".join(c for c in line if c.isalnum())
        nodes[a[:3]] = [a[3:6], a[6:]]

    current_node_id = "AAA"
    next_node_id = ""
    end_node_id = "ZZZ"
    steps = 0

    while 1:
        for lr in directions:
            next_node_id = nodes[current_node_id][lr]

            if current_node_id == end_node_id:
                return steps
            
            current_node_id = next_node_id
            steps+=1
    return -1

#########################################

def part2(lines):
    directions = [int(x) for x in list(lines[0].replace("L", "0").replace("R", "1"))]
    lines = lines[2:]
    nodes = {}

    for line in lines:
        a = "".join(c for c in line if c.isalnum())
        nodes[a[:3]] = [a[3:6], a[6:]]

    start_node_ids = [i for i in list(nodes.keys()) if i[2]=="A"]
    steps = []

    for _, start_node_id in enumerate(start_node_ids):
        node_id = start_node_id
        count = 0
        while node_id[2] != "Z":
            node_id = nodes[node_id][directions[count % len(directions)]]
            count+=1

        steps.append(count)

    return math.lcm(*steps)

#########################################

with open('Input/input_8') as input:
    lines = input.read().splitlines()
    print("part 1: ", part1(lines))
    print("part 2: ", part2(lines))