import collections

def solution(data, n):
    count = collections.Counter(data)
    return([id for id in data if count[id]<=n])


# Test solution:
test_cases = [
    (([1, 2, 3], 0), []),
    (([1, 2, 2, 3, 3, 3, 4, 5, 5], 1), [1,4])
]

for input, expected_output in test_cases:
    result = solution(*input)
    print("Passed!" if result == expected_output else "Failed! (expected: " + str(expected_output) + ", but got: " + str(result) + ")")
