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

def test_fibonacci(max_val):
    for n in range(max_val + 1):
        f_n = fibonacci(n)
        print(f"F_{n} = {f_n}")

def main():
    max_val = 30
    test_fibonacci(max_val)

if __name__ == "__main__":
    main()

