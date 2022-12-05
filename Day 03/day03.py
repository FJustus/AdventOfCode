def first():
 
    res_duplicates = []
    content = open("Day 03/input")
    for line in content.read().split("\n"):

        first = line[:len(line)//2]
        second = line[len(line)//2:]

        duplicates = find_duplicates(first, second)

        res_duplicates = res_duplicates + duplicates

    res = sum(map(val, res_duplicates))
    print(f"first: {res}")


def second(n):
    total = 0
    content = open("Day 03/input")

    while True:
        strs = []
        for i in range(n):
            line = content.readline().strip()
            strs.append(line)
        
        if "" in strs:
            break

        duplicate = find_duplicates(strs[0], strs[1])
        for i in strs[1:]:
            duplicate = find_duplicates(duplicate, i)

        total += sum(map(val, duplicate))

    print(f"second: {total}")

def find_duplicates(first, second):
    duplicates = []

    for i in first:
        if i in second and not i in duplicates:
            duplicates.append(i)

    return duplicates

def val(letter):
    return ord(letter) - 38 if letter.isupper() else ord(letter) - 96
            
# first
first()
second(3)