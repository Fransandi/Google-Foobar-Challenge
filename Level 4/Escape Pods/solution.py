import time
from collections import deque

MAX_NUM = 2000001


def build_graph(entrances, exits, path):
    rooms_len = len(path)
    graph_len = rooms_len + 2
    graph = [[0] * graph_len for _ in range(graph_len)]

    # Increase matrix length by 2, leaving first and last row empty
    for i in range(rooms_len):
        for j in range(rooms_len):
            graph[i + 1][j + 1] = path[i][j]

    # Join entrances on first row
    for entrance in entrances:
        graph[0][entrance + 1] = MAX_NUM

    # Join escape pods on last row
    for exit in exits:
        graph[exit + 1][-1] = MAX_NUM

    return graph


def find_path(graph):
    # Get parents of each node
    parents = [-1] * len(graph)
    queue = deque()
    queue.append(0)
    while queue and parents[-1] == -1:
        node = queue.popleft()
        for child in range(len(graph)):
            if graph[node][child] > 0 and parents[child] == -1:
                queue.append(child)
                parents[child] = node

    # Calculate next possible path
    path = []
    node = parents[-1]
    while node != 0:
        if node == -1:
            return None
        path.append(node)
        node = parents[node]
    path.reverse()
    return path


def solution(input):
    entrances, exits, path = input
    graph = build_graph(entrances, exits, path)
    path = find_path(graph)
    max_flow = 0
    while path:
        # Calculate max_flow in path
        capacity = MAX_NUM
        node = 0
        for child in path:
            capacity = min(capacity, graph[node][child])
            node = child
        max_flow += capacity

        # Remove flow from path
        node = 0
        for child in path:
            graph[node][child] -= capacity
            graph[child][node] += capacity
            node = child
        path = find_path(graph)

    return max_flow


# Test solution:
test_cases = [
    (([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]), 6),
    (
        (
            [0, 1],
            [4, 5],
            [
                [0, 0, 4, 6, 0, 0],
                [0, 0, 5, 2, 0, 0],
                [0, 0, 0, 0, 4, 4],
                [0, 0, 0, 0, 6, 6],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
            ],
        ),
        16,
    ),
]


def milliseconds():
    return int(round(time.time() * 1000))


for input, expected_output in test_cases:
    start_time = milliseconds()
    result = solution(input)
    end_time = milliseconds()
    print(
        "Passed! (" + str(end_time - start_time) + " ms)"
        if result == expected_output
        else "Failed! (expected: "
        + str(expected_output)
        + ", but got: "
        + str(result)
        + ")"
    )
    print()
