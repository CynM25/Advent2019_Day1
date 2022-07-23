'''
--- Day 3: Crossed Wires ---
The gravity assist was successful, and you're well on your way to the Venus refuelling station. During the rush back on Earth, the fuel management system wasn't completely installed, so that's next on the priority list.

Opening the front panel reveals a jumble of wires. Specifically, two wires are connected to a central port and extend outward on a grid. You trace the path each wire takes as it leaves the central port, one wire per line of text (your puzzle input).

The wires twist and turn, but the two wires occasionally cross paths. To fix the circuit, you need to find the intersection point closest to the central port. Because the wires are on a grid, use the Manhattan distance for this measurement. While the wires do technically cross right at the central port where they both start, this point does not count, nor does a wire count as crossing with itself.

For example, if the first wire's path is R8,U5,L5,D3, then starting from the central port (o), it goes right 8, up 5, left 5, and finally down 3:

What is the Manhattan distance from the central port to the closest intersection?

Your puzzle answer was 1983.

--- Part Two ---
It turns out that this circuit is very timing-sensitive; you actually need to minimize the signal delay.

To do this, calculate the number of steps each wire takes to reach each intersection; choose the intersection where the sum of both wires' steps is lowest. If a wire visits a position on the grid multiple times, use the steps value from the first time it visits that position when calculating the total value of a specific intersection.

The number of steps a wire takes is the total number of grid squares the wire has entered to get to that location, including the intersection being considered. Again consider the example from above:

What is the fewest combined steps the wires must take to reach an intersection?

Your puzzle answer was 107754.
'''
print("------------------------------------------------------")
with open("Day3_Input.txt") as f:
    wire_path1 = f.readline()
    wire_path2 = f.readline()

for i in wire_path1:
    s = wire_path1.split(",")
for j in wire_path2:
    s2 = wire_path2.split(",")

DX = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
DY = {'L': 0, 'R': 0, 'U': 1, 'D': -1}

def get_points(s):
    x = 0
    y = 0
    result = set()                                      #needed for Part 1  ()
    #length = 0                                         #needed for Part 2
    #result = {}                                        #needed for Part 2 (empty dictionary)
    for cmd in s:                                       #cmd is 'command "L", "R", "U", "D" '
        direction = cmd[0]
        steps = int(cmd[1:])
        assert direction in ["L", "R", "U", "D"]
        for n in range(steps):
            x += DX[direction]
            y += DY[direction]
            result.add((x,y))                           #needed for Part 1
            #length += 1                                #needed for Part 2
            #if (x,y) not in result:                    #needed for Part 2
            #   result[(x,y)] = length                  #needed for Part 2
    return result

path1 = get_points(s)
path2 = get_points(s2)
both = path1 & path2                                    #needed for Part 1
result = min([abs(x) + abs(y) for (x,y) in both])       #needed for Part 1
#both = set(path1.keys()) & set(path2.keys())           #needed for Part 2
#result = min([path1[p] + path2[p] for p in both])      #needed for Part 2
print(result)


#Part 1: Your puzzle answer was 1983.
#Part 2: Your puzzle answer was 107754.