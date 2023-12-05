def main(data):
    total_overlap = 0
    partial_overlap = 0
    for pair in data:
        a1, a2, b1, b2 = map(int, pair.strip().replace("-", ",").split(","))
        total_overlap += 1 if (a1<=b1 and a2>=b2) or (b1<=a1 and b2>=a2) else 0
        partial_overlap += 1 if not(a2<b1 or a1>b2) else 0

    print(f"Part 1 total: {total_overlap}")
    print(f"Part 2 total: {partial_overlap}")


sample ="2-4,6-8\n2-3,4-5\n5-7,7-9\n2-8,3-7\n6-6,4-6\n2-6,4-8".split("\n")
data = open("Day 04/input").readlines()
    
main(data)