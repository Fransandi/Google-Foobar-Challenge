import time


def solution(m):
    # Edge case: Starting state is also terminal
    if is_terminal(m[0]): return [1] + [0]*(len(m)-1) + [1]

    # Clean non-significant values
    for i in range(len(m)): m[i][i] = 0

    terminal_states = [i+1 for i, state in enumerate(m[1:]) if is_terminal(state)]
    non_terminal_states = [i+1 for i, state in enumerate(m[1:]) if not is_terminal(state)]
    
    # Build probability matrix
    probability_matrix = get_probability_matrix(m)

    # Calculate probabilities
    for i in non_terminal_states: calculate_probabilities(probability_matrix, i)
    
    # Format for output
    terminal_probabilities = list(map(lambda x: probability_matrix[0][x], terminal_states))
    common_denominator = calculate_common_denominator(list(map(lambda x: x[1], terminal_probabilities)))
    probability_numerators = list(map(lambda x: unsimplify(x, common_denominator)[0], terminal_probabilities))

    return probability_numerators + [common_denominator]
                          
def get_probability_matrix(mat):
    probability_matrix = []
    for i in range(len(mat)):
        probability_matrix.append([None] * len(mat))
        for j in range(len(mat)):
            probability_matrix[i][j] = divide_fraction([mat[i][j],1], [sum(mat[i]),1])
    return probability_matrix
    
def calculate_probabilities(mat, node):
    for i in range(len(mat)):
        for j in range(len(mat)):
            if(i != node and j != node):
                mat[i][j] = add_fractions(mat[i][j], multiply_fractions(mat[i][node], mat[node][j]))
                
    for i in range(len(mat)): 
        mat[i][node] = mat[node][i] = [0, 1]
        
    for i in range(len(mat)):
        if(mat[i][i] != [0, 1]):
            multiplier = geometric_series(mat[i][i])
            for j in range(len(mat)):
                mat[i][j] = [0, 1] if i==j else multiply_fractions(mat[i][j], multiplier)
                    
def is_terminal(state): return all(n==0 for n in state)
    
def add_fractions(a, b): return simplify([a[0]*b[1] + b[0]*a[1] , a[1]*b[1]])
    
def substract_fractions(a, b): return simplify([a[0]*b[1] - b[0]*a[1] , a[1]*b[1]])

def multiply_fractions(a, b): return simplify([a[0]*b[0], a[1]*b[1]])

def divide_fraction(a, b):
    if(a[1] == 0 or b[1] == 0): return [0, 1] # Edge case: division by 0
    return simplify([a[0]*b[1], a[1]*b[0]])

def simplify(fraction):
    if(fraction[0] == 0): fraction[1] = 1
    i=2
    while (i <= max(fraction)):
        if all(num%i == 0 for num in fraction):
            fraction[0]//= i
            fraction[1]//= i
        else: i+=1
    return fraction

def unsimplify(a, d): return [int(a[0]*(d/a[1])), d]

def geometric_series(r):
    if r == [1,1]: return r
    difference = substract_fractions([1,1], r)
    return divide_fraction([1,1], difference)
    
def calculate_common_denominator(l):
    common_denominator = min(l)
    while(not all(list(map(lambda x: common_denominator % x == 0, l)))):
        common_denominator+=1
    return common_denominator


# Test solution:
test_cases = [
    ([[0,1,0,0,0,1], [4,0,0,3,2,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0]], [0, 3, 2, 9, 14]),
    ([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], [7, 6, 8, 21]),
    ([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]], [0, 3, 2, 9, 14]),
]

def milliseconds(): return int(round(time.time() * 1000))

for input, expected_output in test_cases:
    start_time = milliseconds()
    result = solution(input)
    end_time = milliseconds()
    print("Passed! (" + str(end_time - start_time) + " ms)" if result == expected_output else "Failed! (expected: " + str(expected_output) + ", but got: " + str(result) + ")")
