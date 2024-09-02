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

def run_f1(run_collect_data, run_plot_data, data_dir, plot_dir):
    # create complexity object
    complexity = Complexity(data_dir, plot_dir)
    
    # collect data
    if run_collect_data:
        n_values = np.linspace(0.5, 5.0, 10)
        n_values = [int(1e7 * n) for n in n_values]
        # print to debug
        #print(f"n_values: {n_values}")
        complexity.collect_data("f1", f1, n_values)
    # plot data
    if run_plot_data:
        xlim = [0, 1e8]
        ylim = [0, 10]
        complexity.plot_data("f1", xlim, ylim)

def run_f2(run_collect_data, run_plot_data, data_dir, plot_dir):
    # create complexity object
    complexity = Complexity(data_dir, plot_dir)
    
    # collect data
    if run_collect_data:
        n_values = np.linspace(0.5, 5.0, 10)
        n_values = [int(1e7 * n) for n in n_values]
        # print to debug
        #print(f"n_values: {n_values}")
        complexity.collect_data("f2", f2, n_values)
    # plot data
    if run_plot_data:
        xlim = [0, 1e8]
        ylim = [0, 10]
        complexity.plot_data("f2", xlim, ylim)

def run_f3(run_collect_data, run_plot_data, data_dir, plot_dir):
    # create complexity object
    complexity = Complexity(data_dir, plot_dir)
    
    # collect data
    if run_collect_data:
        n_values = np.linspace(0.5, 5.0, 10)
        n_values = [int(1e3 * n) for n in n_values]
        # print to debug
        #print(f"n_values: {n_values}")
        complexity.collect_data("f3", f3, n_values)
    # plot data
    if run_plot_data:
        xlim = [0, 1e4]
        ylim = [0, 10]
        complexity.plot_data("f3", xlim, ylim)

def main():
    run_collect_data = False
    run_plot_data    = True
    data_dir = "data"
    plot_dir = "plots"

    run_f1(run_collect_data, run_plot_data, data_dir, plot_dir)
    run_f2(run_collect_data, run_plot_data, data_dir, plot_dir)
    run_f3(run_collect_data, run_plot_data, data_dir, plot_dir)
    
if __name__ == "__main__":
    main()
