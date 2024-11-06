# test_2048.py

# 2048
# The value 0 means the square is empty.

# given an input array,
# return new array from push left
def push_left_v1(array):
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
def push_left_v2(array):
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
def push_left(array):
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
def push_right(array):
    rev_array = list(reversed(array))
    output = push_left(rev_array)
    output.reverse()
    return output

# test pushing operations
def test_pushing():
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
        output_left  = push_left(array)
        output_right = push_right(array)
        print("----------")
        print(f"operation: push_left,  input: {array}, output: {output_left}")
        print(f"operation: push_right, input: {array}, output: {output_right}")

def test_2048():
    pass

def main():
    test_pushing()

if __name__ == "__main__":
    main()

