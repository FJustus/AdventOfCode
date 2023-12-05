def first():
 
    res_duplicates = []
    content = open("Day 03/input")
    for l in content.read().split("\n"):

        first, second = set(l[:len(l)//2]), set(l[len(l)//2:])
        duplicates = (first & second).pop()
        res_duplicates = res_duplicates + list(duplicates)

    res = sum(map(val, res_duplicates))
    print(f"first: {res}")


def second(n):
    total = 0
    content = open("Day 03/input").readlines()

    for i in range(0, len(content), n):
        #assume 3 lines here
        l1, l2, l3 = content[i:i+n]

        same = (set(l1.strip()) & set(l2.strip()) & set(l3.strip())).pop()
        total += sum(map(val, list(same)))

    print(f"second: {total}")

def val(letters):
    return sum([ord(i) - 38 if i.isupper() else ord(i) - 96 for i in letters])

first()
second(3)