import copy


class LList:
    def __init__(self):
        self.first = None
        self.nodes = []


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


if __name__ == "__main__":
    og = list(map(int, open("test_input").readlines()))
    numbers = copy.deepcopy(og)
    #llist = LList()
    #for o in og:
    #    llist.nodes.append(Node())
    l = len(og)
    print(numbers)

    for num in og:
        print("doing", num)

        if num == 0:
            continue

        start_idx = numbers.index(num)
        #print("Start_Idx: ", start_idx)
        #print("Target_Idx: ", target_idx)

        if num < 0:
            for i in range(0, num):
                #print("frontswapperu ", i)
                print("i:", i)
                if start_idx + i >= l:
                    numbers = [numbers[-1]] + numbers[:-1]
                else:
                    numbers[start_idx + i], numbers[start_idx + i + 1] = numbers[start_idx + i + 1], numbers[start_idx + i]
                print(numbers)

        else:
            for i in range(0, abs(num)):
                #print("frontswapperu ", i)
                print("i:", i, ", k")
                if start_idx + i -1 < 0:
                    numbers = numbers[1:-1] + [numbers[0]] + [numbers[-1]]
                else:
                    numbers[start_idx + i], numbers[start_idx + i - 1] = numbers[start_idx + i*k], numbers[start_idx + i]
                print(numbers)

    z_idx = numbers.index(0)
    print("Res Part 1: ", numbers[(z_idx+1000)%l], ",", numbers[(z_idx+2000)%l], ",", numbers[(z_idx+3000)%l],
          "=", numbers[(z_idx+1000)%l] + numbers[(z_idx+2000)%l] + numbers[(z_idx+3000)%l])
