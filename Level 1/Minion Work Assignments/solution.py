import collections
import time

def solution(data, n):
    count = collections.Counter(data)
    return([id for id in data if count[id]<=n])


# Test solution:
test_cases = [
    (([1, 2, 3], 0), []),
    (([1, 2, 2, 3, 3, 3, 4, 5, 5], 1), [1,4])
]

def milliseconds(): return int(round(time.time() * 1000))

for input, expected_output in test_cases:
    start_time = milliseconds()
    result = solution(input)
    end_time = milliseconds()
    print("Passed! (" + str(end_time - start_time) + " ms)" if result == expected_output else "Failed! (expected: " + str(expected_output) + ", but got: " + str(result) + ")")