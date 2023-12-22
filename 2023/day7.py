from functools import cmp_to_key
from collections import Counter

def part1(lines):
    res = 0
    pair5, pair4, fullhouse, pair3, pair2, pair1, highcard = [], [], [], [], [], [], []
   
    for line in lines:
        hand, bid = line.split()[0], int(line.split()[1])

        type = set(hand)

        if len(type) == 5:
            highcard.append((hand, bid))
        elif len(type) == 1:
            pair5.append((hand, bid))
        elif len(type) == 4:
            pair1.append((hand, bid))

        elif len(type) == 2:
            x = list(hand)
            x.sort()
            if x[0]==x[3] or x[1]==x[4]:
                pair4.append((hand, bid))
            else:
                fullhouse.append((hand, bid))

        elif len(type) == 3:
            x = list(hand)
            x.sort()

            if x[0]==x[2] or x[2]==x[4] or x[1]==x[3]:
                pair3.append((hand, bid))
            else:
                pair2.append((hand, bid))

    rank = 1

    reslist = sorted(highcard, key=cmp_to_key(compare_1))
    reslist.extend(sorted(pair1, key=cmp_to_key(compare_1)))
    reslist.extend(sorted(pair2, key=cmp_to_key(compare_1)))
    reslist.extend(sorted(pair3, key=cmp_to_key(compare_1)))
    reslist.extend(sorted(fullhouse, key=cmp_to_key(compare_1)))
    reslist.extend(sorted(pair4, key=cmp_to_key(compare_1)))
    reslist.extend(sorted(pair5, key=cmp_to_key(compare_1)))

    for (_, bid) in reslist:
        res+=rank*bid
        rank+=1

    return res

##########################################################

def compare_1(item1, item2):
    values = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10, "J":11, "Q":12, "K":13, "A":14}
    return _compare(item1, item2, values)

def compare_2(item1, item2):
    values = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10, "J":1, "Q":12, "K":13, "A":14}
    return _compare(item1, item2, values)

def _compare(item1, item2, values):
    
    for i in range(5):
        x, y = values[item1[0][i]], values[item2[0][i]]
        if x < y:
            return -1
        elif x > y:
            return 1
    return 0

#########################################

def part2(lines):
    res = 0
    pair5, pair4, fullhouse, pair3, pair2, pair1, highcard = [], [], [], [], [], [], []
   
    for line in lines:
        hand, bid = line.split()[0], int(line.split()[1])

        type = set(hand)

        data = Counter(hand)
        mf = data.most_common(2)
        values = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10, "J":1, "Q":12, "K":13, "A":14}

        if mf[0][0]=="J":
            mf = mf[1:]

        if not mf:
            most_frequent = "J"
        else:
            if len(mf)==1:
                most_frequent = mf[0][0]

            elif len(mf)==2:
                if mf[0][0]==mf[1][0]:
                    most_frequent = max(mf[0][0], mf[1][0], key=lambda p: values[p])
                else:
                    most_frequent = mf[0][0]

        joker_hand = hand.replace("J", most_frequent)

        type = set(joker_hand)
        unique = len(type)

        # high card
        if unique == 5:
            highcard.append((hand, bid))
        # 5 pair
        elif unique == 1:
            pair5.append((hand, bid))
        # pair
        elif unique == 4:
            pair1.append((hand, bid))

        # 4 pair or full house
        elif unique == 2:
            x = list(joker_hand)
            x.sort()
            if x[0]==x[3] or x[1]==x[4]:
                pair4.append((hand, bid))
            else:
                fullhouse.append((hand, bid))

        # 2 pair or 3 pair
        elif unique == 3:
            x = list(joker_hand)
            x.sort()

            if x[0]==x[2] or x[2]==x[4] or x[1]==x[3]:
                pair3.append((hand, bid))
            else:
                pair2.append((hand, bid))

    reslist = sorted(highcard, key=cmp_to_key(compare_2))
    reslist.extend(sorted(pair1, key=cmp_to_key(compare_2)))
    reslist.extend(sorted(pair2, key=cmp_to_key(compare_2)))
    reslist.extend(sorted(pair3, key=cmp_to_key(compare_2)))
    reslist.extend(sorted(fullhouse, key=cmp_to_key(compare_2)))
    reslist.extend(sorted(pair4, key=cmp_to_key(compare_2)))
    reslist.extend(sorted(pair5, key=cmp_to_key(compare_2)))
    
    rank = 1
    for (_, bid) in reslist:
        res+=rank*bid
        rank+=1

    return res

#########################################

with open('Input/input_7') as input:
    lines = input.read().splitlines()
    print("part 1: ", part1(lines))
    print("part 2: ", part2(lines))
