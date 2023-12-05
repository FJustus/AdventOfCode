elfs = open("input").read().strip().split("\n\n")

elfSum = [sum(map(int, elf.splitlines())) for elf in elfs]

elfSum.sort(reverse=True)
print(f"Part 1 res: {elfSum[0]}")

sum3elf = sum(elfSum[:3])

print(f"Part 2 res: {sum3elf}")