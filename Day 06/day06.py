def main(data, n):
    for i in range(len(data)):
        if len(set(data[i:i+n])) == n:
            print(f"Solution: {i+n}")
            break

file = open("Day 06/input").read()
#test = "bvwbjplbgvbhsrlpgdmjqwftvncz"

main(file, 4)
main(file, 14)