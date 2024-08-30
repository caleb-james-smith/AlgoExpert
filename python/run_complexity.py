# run_complexity.py

import numpy as np
import time
from complexity import Complexity

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

def test(function, n, array):
    print("Testing function: {0}".format(function.__name__))    
    start_time = time.time()
    print("Running function...")
    result = function(array)
    end_time = time.time()
    run_time = end_time - start_time
    
    print(f"n: {n}")
    print(f"result: {result}")
    print("run time: {0:.3f} seconds".format(run_time))

    return run_time

def main():
    #n = int(1e3)
    #array = np.random.randint(10, size=(n))
    #run_time = test(f3, n, array)
    
    complexity = Complexity()
    n_values = [1e3, 2e3, 3e3, 4e3]
    n_values = [int(n) for n in n_values]
    complexity.collect_data("f3", f3, n_values)
    #complexity.plot_data()

if __name__ == "__main__":
    main()
