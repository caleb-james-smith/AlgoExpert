# complexity.py

import numpy as np
import time

def f1(a):
    return 1 + a[0]

def f2(a):
    total = 0
    for x in a:
        total += x
    return total

def f3(a):
    pairs = []
    for x in a:
        for y in a:
            pairs.append([x,y])
    n_pairs = len(pairs)
    return n_pairs

def test():
    print("Starting test...")
    n = int(1e3)
    a = np.random.randint(10, size=(n))
    
    print("Running function...")
    start_time = time.time()
    #result = f1(a)
    #result = f2(a)
    result = f3(a)
    end_time = time.time()
    
    run_time = end_time - start_time
    
    print(f"n: {n}")
    print(f"result: {result}")
    print("run time: {0:.3f} seconds".format(run_time))


def main():
    test()

if __name__ == "__main__":
    main()
