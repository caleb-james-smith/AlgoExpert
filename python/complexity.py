# complexity.py

import numpy as np
import time

class Complexity:
    def __init__(self):
        print("I am Complexity... fear me!")
    
    def get_run_time(self, function, array):
        start_time = time.time()
        result = function(array)
        end_time = time.time()
        run_time = end_time - start_time
        return run_time

    def collect_data(self, name, function, n_values):
        print(f"Collecting data for function {name}...")
        for n in n_values:
            array = np.random.randint(10, size=(n))
            run_time = self.get_run_time(function, array)
            print(f"n: {n}, run time: {run_time:.3f} seconds")

    def plot_data(self):
        print("Plotting data...")

