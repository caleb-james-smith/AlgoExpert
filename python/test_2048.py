# test_2048.py

# 2048
# The value 0 means the square is empty.

# --------------- #
# Array functions #
# --------------- #

# given an input array,
# return new array from push left
def push_array_left_v1(array):
    n = len(array)
    output = n * [0]
    i = 0
    for value in array:
        if value > 0:
            output[i] = value
            i += 1
    return output

# given an input array,
# return new array from push left
def push_array_left_v2(array):
    n = len(array)
    output = []
    for value in array:
        if value > 0:
            output.append(value)
    while len(output) < n:
        output.append(0)
    return output

# given an array and two indices,
# determine if a nonzero value is between them
def value_is_in_between(array, i, j):
    for index in range(i + 1, j):
        if array[index] > 0:
            return True
    return False

# given an input array,
# update values from push left
# FIXME:
# A combined number should not be combined again!
# Can we keep track of indices that have already been combined?
# We may be safe from this issue by using the original array
# when checking for in between values.
def update_values_left(array):
    n = len(array)
    output = array.copy()
    for i in range(n - 1):
        for j in range(i + 1, n):
            x = output[i]
            y = output[j]
            # require that x and y are nonzero and equal
            if x > 0 and y > 0 and x == y:
                val_in_between = value_is_in_between(array, i, j)
                if not val_in_between:
                    output[i] = x + y
                    output[j] = 0
    return output

# given an input array,
# return new array from push left
def push_array_left(array):
    updated_array = update_values_left(array)
    n = len(updated_array)
    output = []
    for value in updated_array:
        if value > 0:
            output.append(value)
    while len(output) < n:
        output.append(0)
    return output

# given an input array,
# return new array from push right
# Warning: Do not change input array (with reverse).
def push_array_right(array):
    rev_array = list(reversed(array))
    output = push_array_left(rev_array)
    output.reverse()
    return output

# ---------------- #
# Matrix functions #
# ---------------- #

def print_matrix(matrix):
    for row in matrix:
        print(row)

# return transpose of matrix
# input:  m x n matrix
# output: n x m matrix
def transpose_matrix(matrix):
    output = []
    if not matrix:
        return output
    m = len(matrix)
    n = len(matrix[0])
    for i in range(n):
        row = m * [0]
        output.append(row)
    for i in range(n):
        for j in range(m):
            output[i][j] = matrix[j][i]
    return output

# given an input matrix,
# return new matrix from push left
def push_matrix_left(matrix):
    output = []
    for row in matrix:
        new_row = push_array_left(row)
        output.append(new_row)
    return output

# given an input matrix,
# return new matrix from push right
def push_matrix_right(matrix):
    output = []
    for row in matrix:
        new_row = push_array_right(row)
        output.append(new_row)
    return output

# given an input matrix,
# return new matrix from push up
def push_matrix_up(matrix):
    tran_matrix = transpose_matrix(matrix)
    output = push_matrix_left(tran_matrix)
    output = transpose_matrix(output)
    return output

# given an input matrix,
# return new matrix from push down
def push_matrix_down(matrix):
    tran_matrix = transpose_matrix(matrix)
    output = push_matrix_right(tran_matrix)
    output = transpose_matrix(output)
    return output

# test array pushing operations
def test_array_pushing():
    arrays = []
    
    arrays.append([1, 1, 0, 0])
    arrays.append([1, 0, 1, 0])
    arrays.append([1, 0, 0, 1])
    arrays.append([0, 1, 1, 0])
    arrays.append([0, 1, 0, 1])
    arrays.append([0, 0, 1, 1])
    
    arrays.append([1, 1, 1, 0])
    arrays.append([1, 1, 0, 1])
    arrays.append([1, 0, 1, 1])
    arrays.append([0, 1, 1, 1])
    
    arrays.append([1, 1, 1, 1])
    
    arrays.append([1, 1, 2, 0])
    arrays.append([1, 1, 0, 2])
    arrays.append([1, 2, 1, 2])
    arrays.append([1, 1, 2, 2])
    arrays.append([2, 2, 2, 2])
    
    #arrays.append([1, 2, 0, 0])
    #arrays.append([1, 0, 2, 0])
    #arrays.append([1, 0, 0, 2])
    #arrays.append([0, 1, 2, 0])
    #arrays.append([0, 1, 0, 2])
    #arrays.append([0, 0, 1, 2])

    for array in arrays:
        output_left  = push_array_left(array)
        output_right = push_array_right(array)
        print("----------")
        print(f"operation: push_array_left,  input: {array}, output: {output_left}")
        print(f"operation: push_array_right, input: {array}, output: {output_right}")

# test matrix pushing operations
def test_matrix_pushing():
    matrices = []
    matrices.append([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
    matrices.append([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    matrices.append([[1, 1, 0, 0], [1, 0, 1, 0], [1, 0, 0, 1], [0, 0, 1, 1]])

    for matrix in matrices:
        output_left  = push_matrix_left(matrix)
        output_right = push_matrix_right(matrix)
        output_up    = push_matrix_up(matrix)
        output_down  = push_matrix_down(matrix)
        print("----------------------------")
        
        # push matrix left
        print(f"operation: push_matrix_left")
        print(f"input:")
        print_matrix(matrix)
        print(f"output:")
        print_matrix(output_left)
        
        # push matrix right
        print(f"operation: push_matrix_right")
        print(f"input:")
        print_matrix(matrix)
        print(f"output:")
        print_matrix(output_right)
        
        # push matrix up
        print(f"operation: push_matrix_up")
        print(f"input:")
        print_matrix(matrix)
        print(f"output:")
        print_matrix(output_up)
        
        # push matrix down
        print(f"operation: push_matrix_down")
        print(f"input:")
        print_matrix(matrix)
        print(f"output:")
        print_matrix(output_down)

def main():
    #test_array_pushing()
    test_matrix_pushing()

if __name__ == "__main__":
    main()

