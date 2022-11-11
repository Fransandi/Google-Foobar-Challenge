import time

def solution(xs):
    negative_values = [panel for panel in xs if panel<0]
    positive_values = [panel for panel in xs if panel>0]

    # Edge cases: only negative values
    if not len(positive_values):
        # There was at least a zero at the beggining
        if len(xs)!=len(negative_values): return '0'
        # Return the greatest negative number
        else: return '-'+str(abs(sorted(negative_values)[0]))

    # Remove the worst negative number, if odd amount
    if len(negative_values)%2: 
        negative_values.sort()
        negative_values.pop()

    power = 1
    for val in positive_values + negative_values: power*= val
    
    return str(abs(power))

# Test solution:
test_cases = [
    ([-2, -3, 4, 10], '240'),
    ([0, 0, -1], '0'),
    ([2, 0, 2, 2, 0], '8'),
    ([-2, -3, 4, -5], '60'),
    ([-2, -3, 4, -5, -1], '120'),
    ([-2, 4], '4'),
    ([-1], '-1')
]

def milliseconds(): return int(round(time.time() * 1000))

for input, expected_output in test_cases:
    start_time = milliseconds()
    result = solution(input)
    end_time = milliseconds()
    print("Passed! (" + str(end_time - start_time) + " ms)" if result == expected_output else "Failed! (expected: " + str(expected_output) + ", but got: " + str(result) + ")")