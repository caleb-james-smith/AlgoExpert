# complexity.py

import matplotlib.pyplot as plt
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

    def plot_data(self, name):
        print(f"Plotting data for function {name}...")
        
        # load data from file
        input_file = "{0}/{1}.csv".format(self.data_dir, name)
        data = tools.readCSV(input_file)
        
        # get header and points from data
        # note: x,y values, must convert from string to float
        header = data[0]
        points = data[1:]
        x_label = header[0]
        y_label = header[1]
        x_values = [float(point[0]) for point in points]
        y_values = [float(point[1]) for point in points]
        print(f"header: {header}")
        print(f"x_values: {x_values}")
        print(f"y_values: {y_values}")
        
        # plot data
        fig, ax = plt.subplots(figsize=(6, 6))
        xlim = [0, 5e3]
        ylim = [0, 5]
        plt.plot(x_values, y_values, 'o')
        ax.set_xlim(xlim)
        ax.set_ylim(ylim)
        ax.set_title(f"run time for function {name}")
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        plt.show()

