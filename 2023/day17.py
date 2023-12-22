from queue import PriorityQueue
import time

def part1(m):
    directions = {
        (1,0),(0,1),(-1,0),(0,-1)
    }

    prev = dict()    

    def dijkstra(start, end):
        queue = PriorityQueue()
        queue.put((int(m[0][0]),start,(),0))
        seen = set()

        
        prev[start] = None


        #for i in range(10):
        while not queue.empty():
            (cost, current, direction, num) = queue.get()
            if (cost, current, direction, num) in seen:
                continue
            seen.add((cost, current, direction, num))
            #print("checking ", current, ", dir: ", direction, ", num: ", num)

            
            for newDir in directions:
                newPos = newDir[0]+current[0], newDir[1]+current[1]
                if not 0<=newPos[1]<len(m) or not 0<=newPos[0]<len(m[0]):
                    continue

                newNum = num
                new_cost = cost + int(m[newPos[1]][newPos[0]])

                if newPos == end:
                    prev[(newPos, newDir, newNum)] = (current, direction, num)
                    return new_cost, (newPos, newDir, newNum)

                if newDir == direction:
                    newNum = num + 1
                    if newNum > 3:
                        continue

                elif direction and newDir == (direction[0]*-1, direction[1]*-1):
                    continue

                else:
                    newNum = 1
               
                priority = new_cost 
                queue.put((priority, newPos, newDir, newNum))
                prev[(newPos, newDir, newNum)] = (current, direction, num)

            
        return None


    res, prevIdx = dijkstra((0,0), (len(m)-1,len(m[0])-1))    
    print(prev)

    end = prevIdx
    path = []
    while end[0]!=(0,0):
        #print("end: ", end)
        path.append(end[0])
        end = prev[end]
    print("path: ", path[::-1])
    return res
#########################################

def part2(lines):
    res = 0
    return res

#########################################

with open('Input/input_test') as input:
    start = time.time()
    lines = input.read().splitlines()
    print("part 1: ", part1(lines))
    print("part 2: ", part2(lines))
    print("runtime: %ss" % round(time.time() - start, 2))