# fibonacci.py

def fibonacci(n):
    if n < 0:
        return -1
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return fibonacci(n - 1) + fibonacci(n - 2)

def test_fibonacci(max_n):
    for n in range(max_n + 1):
        f_n = fibonacci(n)
        print(f"F_{n} = {f_n}")

def check_fibonacci(sequence, max_n):
    for n in range(max_n + 1):
        is_fibonacci = (n in sequence)
        print(f"n = {n}, is_fibonacci = {is_fibonacci}")

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
    
    check_fibonacci(fibonacci_list, max_val)

if __name__ == "__main__":
    main()

