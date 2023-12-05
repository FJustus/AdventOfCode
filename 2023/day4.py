def part1(nums):
    res = 0

    for line in nums:
        points = 0
        win, guess = line[0].split(), line[1].split()

        for g in guess:
            if g in win:
                points = points * 2 if points > 0 else 1
    
        res += points
    return res

#########################################

def part2(nums):
    cardAmount = [1 for s in range(len(nums))]
    for i, line in enumerate(nums, start=1):
        points = 0
        win, guess = line[0].split(), line[1].split()

        for g in guess:
            if g in win:
                points += 1

        for x in range(1,points+1):
            cardAmount[i+x-1] += cardAmount[i-1]

    return sum(cardAmount)

#########################################

def parseInput(input):
    return [i.split(":")[1].split("|") for i in input]

with open('Input/input_4') as input:
    lines = input.read().splitlines()
    print("part 1: ", part1(parseInput(lines)))
    print("part 2: ", part2(parseInput(lines)))