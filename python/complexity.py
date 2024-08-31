# complexity.py

import numpy as np
import time
import tools

class Complexity:
    def __init__(self, data_dir):
        print("I am Complexity... fear me!")
        self.data_dir = data_dir
    
    def get_run_time(self, function, array):
        start_time = time.time()
        result = function(array)
        end_time = time.time()
        run_time = end_time - start_time
        return run_time

    def collect_data(self, name, function, n_values):
        print(f"Collecting data for function {name}...")
        data = []
        header = ["n", "run_time"]
        data.append(header)
        for n in n_values:
            array = np.random.randint(10, size=(n))
            run_time = self.get_run_time(function, array)
            print(f"n: {n}, run time: {run_time:.3f} seconds")
            row = [n, run_time]
            data.append(row)
        print(data)
        output_file = "{0}/{1}.csv".format(self.data_dir, name)
        tools.makeDir(self.data_dir)
        tools.writeCSV(output_file, data)

    def plot_data(self):
        print("Plotting data...")


