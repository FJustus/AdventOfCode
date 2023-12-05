import re
from functools import reduce
from math import isqrt
from sys import set_int_max_str_digits


class Day11:
    def __init__(self, data):
        self.monkeys = []
        self.parse_monkeys(data)

        divisers = [m.test_num for m in self.monkeys]
        limiter = reduce(lambda a,b: a*b, divisers)
        [m.set_limiter(limiter) for m in self.monkeys]

        res = [m.save() for m in self.monkeys]
        print(f"starting: {res}")

        for r in range(1, 10001):
            for i in range(len(self.monkeys)):
                ret = self.monkeys[i].inspect()
                for to, val in ret:
                    self.monkeys[int(to)].catch(val)

            # save after round values
            if r % 100 == 0 or r in [1, 20, 100]:
                print(f"===ROUND {r}===")
                res = []
                count = []
                for m in self.monkeys:
                    res.append(m.save())
                    count.append(m.inspect_counter)

                #print(f"res: {res}")
                print(f"count: {count}")
                count.sort()
                print(f"Result Part 1/2: {count[-1]*count[-2]}")

    def parse_monkeys(self, data):
        monkeys = data.split("\n\n")
        i = 0
        for m in monkeys:
            m = m.split("\n")
            items = re.findall(r"\d+", m[1])
            op = m[2].split("=")[1]
            test = re.search(r"\d+", m[3])[0]
            true = re.search(r"\d+", m[4])[0]
            false = re.search(r"\d+", m[5])[0]
            self.monkeys.append(Monkey(i, items, op, test, true, false))
            i += 1


class Monkey:
    def __init__(self, ID, start_items, operation, test_num, true_num, false_num):
        self.ID = ID
        self.inspect_counter = 0
        self.items = list(map(int, start_items))
        self.operation = operation
        self.test_num = int(test_num)
        self.true_num = int(true_num)
        self.false_num = int(false_num)

    def set_limiter(self, l):
        self.limiter = l

    def inspect(self):
        ret = []
        for old in self.items:
            self.inspect_counter += 1
            # print(f"monkey {self.ID} inspecting {old}")
            new = eval(self.operation) % self.limiter

            # new = new * 3
            if new % self.test_num == 0:
                throw_to = self.true_num
            else:
                throw_to = self.false_num
            ret.append((throw_to, new))
        self.items = []
        return ret

    def catch(self, val):
        self.items.append(val)

    def save(self):
        return self.items


file = open("input").read()
Day11(file)
