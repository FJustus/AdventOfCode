def main(data, tail_length):
    hs = [Position(0, 0) for i in range(tail_length)]

    for line in data:
        direction, amount = line.split(" ")
        for i in range(int(amount)):
            # print_state(hs, 26, 26)
            for j in range(len(hs)-1):
                h = hs[j]
                t = hs[j+1]

                if j == 0:
                    hs[j].move(direction)

                x_div = abs(h.x - t.x)
                y_div = abs(h.y - t.y)

                if x_div == 2 and y_div == 2:
                    hs[j+1].move_behind_square(hs[j])
                elif x_div == 2:
                    hs[j + 1].move_behind_x(hs[j])
                elif y_div == 2:
                    hs[j+1].move_behind_y(hs[j])
    print(f"result: {len(set(hs[-1].positions))}")


def print_state(hs, x_max, y_max):
    print("---------------")
    for y in range(0, 5):
        for x in range(0, 6):
            num = "."
            for i in range(len(hs)):
                if (x, y) == hs[i].positions[-1]:
                    num = i
            print(num, end="")
        print("")


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.positions = [(x, y)]

    def move(self, letter):
        (x, y) = letters[letter]
        self.x += x
        self.y += y
        self.positions.append((self.x, self.y))

    def last(self):
        return self.positions[-2]

    def move_behind_x(self, pos):
        (x2_old, _) = pos.positions[-2]
        (_, y2) = pos.positions[-1]
        self.x, self.y = x2_old, y2
        self.positions.append((self.x, self.y))

    def move_behind_y(self, pos):
        (_, y2_old) = pos.last()
        (x2, _) = pos.positions[-1]
        self.x, self.y = x2, y2_old
        self.positions.append((self.x, self.y))

    def move_behind_square(self, pos):
        self.x, self.y = pos.last()
        self.positions.append((self.x, self.y))


letters = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}

file = open("input").readlines()
test = open("test_input").readlines()
test2 = open("test_input2").readlines()
main(file, 2)
main(file, 10)
