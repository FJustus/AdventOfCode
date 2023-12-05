from dataclasses import dataclass
import re

def first():
    stacks = []
    moves = []

    # parse move commands
    moves = parse_moves()
    # parse stack states
    stacks = parse_stacks()

    # apply moves to stacks
    for m in moves:
        for i in range(m.amount):
            cargo = stacks[m.from_stack].pop()
            stacks[m.to_stack].append(cargo)
    print_stacks(stacks)   

    print_solution(stacks) 

def second():
    stacks = []
    moves = []

    # parse stack states
    stacks = parse_stacks()
    # parse move commands
    moves = parse_moves()

    # apply moves to stacks
    for m in moves:
        changes = []
        for i in range(m.amount):
            changes.append(stacks[m.from_stack].pop())
        for j in reversed(changes):
            stacks[m.to_stack].append(j)

    print_stacks(stacks)   

    print_solution(stacks) 

def print_solution(stacks):
    res = ""
    for s in stacks:
        res = res + s[-1]
    print(f"solution: {res}")

def print_stacks(stacks):
    for i,s in enumerate(stacks):
        print(f"Stack {i}: {s}")
    print("----------------")

def parse_moves():
    moves = []
    for line in file[10:]:
        m,f,t = re.findall(r'\d+', line.strip())
        moves.append(Move(m, f, t))
    return moves

def parse_stacks():
    stacks = [[],[],[],[],[],[],[],[],[]]

    for line in reversed(file[:8]):
        for id in range(0, len(line), 4):
            s = line[id:id+4]
            val = re.search(r'\w', s)
            if val:
                val = val.group(0)
                stacks[id//4].append(val)
        
    print_stacks(stacks)
    return stacks

@dataclass
class Move:
    amount: int
    from_stack: int
    to_stack: int

    def __init__(self, amount, from_stack, to_stack):
        self.amount = int(amount)
        # -1 because array index
        self.from_stack = int(from_stack)-1
        self.to_stack = int(to_stack)-1

file = open("Day 05/input").readlines()
first()
second()