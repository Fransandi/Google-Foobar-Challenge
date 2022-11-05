
def solution(x, y):
    worker_id = 0
    
    increment = 1
    for _ in range(x):
        worker_id+=increment
        increment+=1
    
    increment = x
    for _ in range(y-1):
        worker_id+=increment
        increment+=1

    return str(worker_id)

# Test solution:
test_cases = [
    ((5, 10), '96'),
    ((3, 2), '9'),
    ((5, 2), '20'),
]

for input, expected_output in test_cases:
    result = solution(*input)
    print("Passed!" if result == expected_output else "Failed! (expected: " + str(expected_output) + ", but got: " + str(result) + ")")
