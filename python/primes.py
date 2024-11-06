# primes.py

# input:  maximum value (max_val)
# output: list of primes with p <= max_val

# Method 1:
# - for each n, compute the number of divisors
# - if n has 2 divisors, it is prime

# Method 2:
# - create an array of length max_val + 1
# - the indices of the array represent numbers
# - the contents of the array represent if the number is prime
# - iterate over index (p)
# - if p is prime (array contains True at index p),
# - starting at 2 * p, set array at each multiple of p to False
# - collect prime numbers (contain True at index) into output array

def get_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

def get_num_divisors(n):
    divisors = get_divisors(n)
    num_divisors = len(divisors)
    return num_divisors

# Method 1
def get_primes_v1(max_val):
    output = []
    for n in range(1, max_val + 1):
        num_divisors = get_num_divisors(n)
        if num_divisors == 2:
            output.append(n)
    return output

# Method 2
def get_primes_v2(max_val):
    output = []
    numbers = (max_val + 1) * [True]
    # set non prime numbers to false
    numbers[0] = False
    numbers[1] = False
    for p in range(2, max_val + 1):
        if numbers[p]:
            for i in range(2 * p, max_val + 1, p):
                numbers[i] = False
    # collect primes
    for i in range(max_val + 1):
        if numbers[i]:
            output.append(i)
    return output

def main():
    max_val     = int(29)
    primes_v1   = get_primes_v1(max_val)
    primes_v2   = get_primes_v2(max_val)
    n_primes_v1 = len(primes_v1)
    n_primes_v2 = len(primes_v2)
    print(f"max_val: {max_val}")
    print("-----------------------")
    print(f"primes_v1: {primes_v1}")
    print(f"n_primes_v1: {n_primes_v1}")
    print("-----------------------")
    print(f"primes_v2: {primes_v2}")
    print(f"n_primes_v2: {n_primes_v2}")

if __name__ == "__main__":
    main()



