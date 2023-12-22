from functools import cache
import itertools
import time


def part1(lines):
    # disgusting bruteforce
    res = 0

    for idx, line in enumerate(lines):
        if idx % 100 == 0:
            print("line ", idx)

        Q = []
        field, nums = line.split()
        nums = list(map(int,nums.split(",")))    

        Q = add_permutations(field, nums)
        val = sum(check(*q) for q in Q)
        res += val
    return res

def add_permutations(field, nums):
    n = field.count("?")
    iters = list(itertools.product([True, False], repeat=n))

    perms = []
    for x in range(len(iters)):
        new_field = ""
        q_count = 0
        for i in range(len(field)):
            if field[i]=="?":
                new_field += "." if iters[x][q_count] else "#"
                q_count += 1
            else:
                new_field += field[i]
        perms.append((new_field, tuple(nums)))
    return tuple(perms)


def check(field, nums):
    field = [x for x in field.split(".") if x]
    if len(field) != len(nums):
        return 0
    elif _check(tuple(field), tuple(nums)):
        return 1
    else:
        return 0

def _check(f, n):
    if all(len(f[i])==n[i] for i in range(len(n))):
        return 1

#########################################

def part2(lines):
    vals = []
    for line in lines:
        field, nums = line.split()
        nums = list(map(int,nums.split(",")))
        vals.append(("?".join([field]*5), tuple(nums*5)))
            
    return sum(recurse(f, n) for (f,n) in vals)


@cache
def recurse(field, nums):
    # check basic cases
    if not nums:
        return True if not "#" in field else False

    if not field:
        return False    

    next_sign = field[0]
    next_num = nums[0]
     

    def raute():
        # block doesn't fit
        if len(field) < next_num:
            return False
        
        # . would be in block
        if "." in field[:next_num]:
            return False

        # correct length and last one
        if len(field) == next_num:
            return True if len(nums) == 1 else False

        if field[next_num] != "#":
            return recurse(field[next_num+1:], nums[1:])

        return False
    
    def punkt():
        return recurse(field[1:], nums)


    if next_sign == ".":
        return punkt()
    elif next_sign == "#":
        return raute()
    elif next_sign == "?":
        return raute() + punkt()
    else:
        raise RuntimeError



#########################################

with open('Input/input_12') as input:
    start = time.time()
    lines = input.read().splitlines()
    #print("part 1: ", part1(lines))
    print("part 2: ", part2(lines))
    print("runtime: %ss" % round(time.time() - start, 2))