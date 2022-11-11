import time

def solution(l):
    divisors_count = [0]*len(l)
    count = 0
    
    for i in range(len(l)):
        for j in range(i):
            if l[i] % l[j]==0:
                divisors_count[i]+=1 
                count+=divisors_count[j]
    
    return count


# Test solution:
test_cases = [
    ([1, 2, 3, 4, 5, 6], 3),
    ([1, 1, 1], 1),
]

def milliseconds(): return int(round(time.time() * 1000))

for input, expected_output in test_cases:
    start_time = milliseconds()
    result = solution(input)
    end_time = milliseconds()
    print("Passed! (" + str(end_time - start_time) + " ms)" if result == expected_output else "Failed! (expected: " + str(expected_output) + ", but got: " + str(result) + ")")