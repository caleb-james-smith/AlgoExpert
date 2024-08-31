# tools.py

import os
import csv

# creates directory if it does not exist
def makeDir(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

# read csv file: takes a csv file as input and outputs data in a matrix
def readCSV(input_file):
    data = []
    with open(input_file, mode="r", newline='') as f:
        reader = csv.reader(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            data.append(row)
    return data

# write csv file: takes data matrix as input and outputs a csv file 
def writeCSV(output_file, data):
    with open(output_file, mode="w", newline='') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in data:
            writer.writerow(row)
