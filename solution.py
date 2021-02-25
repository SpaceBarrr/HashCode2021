# =========================
# FUNCTIONS
# =========================

def change_path(path):
    node_path = []
    for location in path[1:]:
        for intersection in directory:
            if location == intersection[2]:
                node_path.append(int(intersection[1]))
    return node_path

def conflict_finder():
    conflicts = [item for item, count in collections.Counter(current_node).items() if count > 1]
    return conflicts

def conflict_resolution(intersection, incoming_streets):
    street = random.randrange(0,len(incoming_streets)-1)
    return street

def find_incoming_streets(intersection):
    incoming_streets = []
    for i in range(len(directory)):
        if int(directory[i][1]) == intersection:
            incoming_streets.append(int(directory[i][0]))
    return incoming_streets

# =========================
# INIT
# =========================

import collections
import random
from copy import deepcopy

file = 'a.txt'
with open(file, "r+") as f:
    data_set_example = f.read()
    f.close()

data_set_example = data_set_example.split("\n")
length = len(data_set_example)

for i in range(length):
    data_set_example[i] = data_set_example[i].split(" ")

duration = int(data_set_example[0][0])
intersections = int(data_set_example[0][1])
streets = int(data_set_example[0][2])
cars = int(data_set_example[0][3])
score = int(data_set_example[0][4])

directory = []
paths = []

i = 1
while i < length-1:
    if i < 1+streets:
        directory.append(data_set_example[i])
        i += 1
    else:
        paths.append(data_set_example[i])
        i += 1

node_path = []
for path in paths:
    node_path.append(change_path(path))

edge_list = []
for item in directory:
    edge_list.append(list((int(item[0]), int(item[1]), int(item[3]))))

travel = [[0 for i in range(intersections)] for j in range(intersections)]
for i in range(intersections):
    for j in range(intersections):
        if i == j:
            travel[j][i] = 1
for row, col, weight in edge_list:
    travel[row][col] = weight

starting_pos = []
# current position, stop in path, travel tick time
for i in range(cars):
    starting_pos.append(list((int(node_path[i][0]), 0, 0)))

current_pos = deepcopy(starting_pos)
current_node = []

# =========================
# TICK SYSTEM
# =========================

def tick():
    actions = []
    if len(conflict_finder()) == 0:
        for i in range(len(current_pos)):
            if current_pos[i][1] + 1 == len(node_path[i]):
                pass
            elif current_pos[i][2] == 0:
                actions.append(str(paths[i][current_pos[i][1]+1])+' 1')
                current_pos[i][0] = node_path[i][current_pos[i][1]+1]
                current_pos[i][1] += 1
                current_pos[i][2] = travel[node_path[i][current_pos[i][1]]-1][node_path[i][current_pos[i][1]]]
            else:
                current_pos[i][2] -= 1
    if actions:
        print(actions)

running = True
tick_count = 0
while running:
    tick()
    if tick_count == duration:
        running = False
    tick_count += 1
