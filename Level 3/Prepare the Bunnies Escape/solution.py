import time
from collections import deque

class Node:
    def __init__(self, x, y, walls, station_map):
        self.x = x
        self.y = y
        self.walls = walls
        self.station_map = station_map

    def __hash__(self):
        return self.x ^ self.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.walls == other.walls

    def get_neighbours(self):
        x = self.x
        y = self.y
        walls = self.walls
        station_map = self.station_map
        
        height = len(station_map)
        width = len(station_map[0])
        
        neighbours = []

        if x > 0:
            n = station_map[y][x-1] == 1
            if n:
                if walls > 0: 
                    neighbours.append(Node(x-1, y, walls-1, station_map))
            else: 
                neighbours.append(Node(x-1, y, walls, station_map))

        if x < width-1:
            n = station_map[y][x+1] == 1
            if n:
                if walls > 0: 
                    neighbours.append(Node(x+1, y, walls-1, station_map))
            else: 
                neighbours.append(Node(x+1, y, walls, station_map))

        if y > 0:
            n = station_map[y-1][x] == 1
            if n:
                if walls > 0: 
                    neighbours.append(Node(x, y-1, walls-1, station_map))
            else: 
                neighbours.append(Node(x, y-1, walls, station_map))

        if y < height-1:
            n = station_map[y+1][x] == 1
            if n:
                if walls > 0: 
                    neighbours.append(Node(x, y+1, walls-1, station_map))
            else: 
                neighbours.append(Node(x, y+1, walls, station_map))

        return neighbours

class Station:
    def __init__(self, station_map, walls):
        self.station_map = station_map
        self.height = len(station_map)
        self.width = len(station_map[0])
        self.walls = walls

    def get_shortest_escape_path(self):
        source = Node(0, 0, self.walls, self.station_map)
        queue = deque([source])
        cost = {source: 1}

        while queue:
            node = queue.popleft()

            # Solution found
            if node.y == self.height-1 and node.x == self.width-1: return cost[node]

            # Iterate through all neighbours
            for neighbour in node.get_neighbours():
                # Add neighbour to the queue if its cost wasn't calculated before
                if neighbour not in cost.keys():      
                    cost[neighbour] = cost[node] + 1   
                    queue.append(neighbour)   

        return -1 

def solution(map):
    station = Station(map, 1)
    return station.get_shortest_escape_path()

# Test solution:
test_cases = [
    ([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]], 7),
    ([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]], 11),
    ([[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], 39)
]

def milliseconds(): return int(round(time.time() * 1000))

for input, expected_output in test_cases:
    start_time = milliseconds()
    result = solution(input)
    end_time = milliseconds()
    print("Passed! (" + str(end_time - start_time) + " ms)" if result == expected_output else "Failed! (expected: " + str(expected_output) + ", but got: " + str(result) + ")")
