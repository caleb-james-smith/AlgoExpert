# fibonacci.py

# get n_th fibonacci number
def fibonacci(n):
    if n < 0:
        return -1
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return fibonacci(n - 1) + fibonacci(n - 2)

# given a list of fibonacci numbers,
# determine if a number is a fibonacci number
def is_fibonacci(sequence, n): 
    return (n in sequence)

# given a list of fibonacci numbers,
# determine if two numbers are consecutive fibonacci numbers
# handle (0, 1), (1, 1), and (1, 2) cases
def consecutive_fibonacci(sequence, n1, n2):
    if n1 in sequence and n2 in sequence:
        if n1 == 1 and n2 == 1:
            return True
        if n1 == 1 and n2 == 2:
            return True
        if n1 == 2 and n2 == 1:
            return True
        idx_1 = sequence.index(n1)
        idx_2 = sequence.index(n2)
        diff = abs(idx_1 - idx_2)
        if diff == 1:
            return True
        else:
            return False
    else:
        return False

def test_fibonacci(max_n):
    for n in range(max_n + 1):
        f_n = fibonacci(n)
        print(f"F_{n} = {f_n}")

def test_consecutive_fibonacci(sequence):
    pairs = [[0, 1], [1, 0], [1, 2], [2, 1], [2, 3], [3, 2], [1, 1], [2, 2], [1, 3], [2, 4], [2, 5], [3, 5], [5, 3]]
    for pair in pairs:
        n1 = pair[0]
        n2 = pair[1]
        consecutive = consecutive_fibonacci(sequence, n1, n2)
        print(f"n1 = {n1}, n2 = {n2}, consecutive = {consecutive}")

def check_fibonacci(sequence, max_n):
    for n in range(max_n + 1):
        is_fib = is_fibonacci(sequence, n)
        #print(f"n = {n}, is_fib = {is_fib}")
        if is_fib:
            print(f"n = {n} - fibonacci")
        else:
            print(f"n = {n}")

# generate fibonacci sequence as list
def generate_fibonacci_list(max_val):
    sequence = []
    if max_val < 0:
        return sequence
    if max_val >= 0:
        sequence.append(0)
    if max_val >= 1:
        sequence.append(1)

    n = 1
    while n <= max_val: 
        sequence.append(n)
        n = sequence[-1] + sequence[-2]

    return sequence

# generate fibonacci sequence as dictionary
# this may not work as elements are not ordered...
def generate_fibonacci_dict(max_val):
    sequence = []
    if max_val < 0:
        return sequence
    if max_val >= 0:
        sequence.append(0)
    if max_val >= 1:
        sequence.append(1)

    n = 1
    while n <= max_val: 
        sequence.append(n)
        n = sequence[-1] + sequence[-2]

    return sequence

def main():
    #max_n = 30
    #test_fibonacci(max_n)
    
    max_val = int(1e2)
    fibonacci_list = generate_fibonacci_list(max_val)
    n_fibonacci = len(fibonacci_list)
    print(f"n_fibonacci: {n_fibonacci}")
    print(f"fibonacci_list: {fibonacci_list}")
    
    #check_fibonacci(fibonacci_list, max_val)
    test_consecutive_fibonacci(fibonacci_list)

if __name__ == "__main__":
    main()

