import functools
import operator

def part1(lines):
    res = 0

    for line in lines:
        values = [list(map(int, line.split()))]

        new = [1]
        count = 0

        while sum(new)!=0:
            new = [y-x for x,y in zip(values[count], values[count][1:])]
            if new:
                values.append(new)
            else:
                values.append([0])
            count+=1

        res += sum(val[-1] for val in values)
        
    return res

#########################################

def part2(lines):
    res = 0

    for line in lines:
        values = [list(map(int, line.split()))]

        new = [1]
        count = 0

        while any(n!=0 for n in new):
            new = [y-x for x,y in zip(values[count], values[count][1:])]
            if new:
                values.append(new)
            else:
                values.append([0])
            count+=1
        
        numbers = [value[0] for value in values]

        #foldr = lambda func, acc, xs: functools.reduce(lambda x, y: func(y, x), xs[::-1], acc)
        def foldr(nums):
            if len(nums)==2:
                return nums[0] - nums[1]
            return nums[0] - foldr(nums[1:])
        
        val = foldr(numbers)
        res += val
   
    return res

   
#########################################

with open('Input/input_9') as input:
    lines = input.read().splitlines()
    print("part 1: ", part1(lines))
    print("part 2: ", part2(lines))