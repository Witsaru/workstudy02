import matplotlib.pyplot as plt
import csv
import os


def plotTimeProcess(file_):
# Read the CSV file
    name = file_
    file_name = os.path.basename(name)
    with open(file_, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)

    # Extract the data, filtering out unrealistic values
    x = []
    y = []
    for row in data[1:]:
        index = int(row[0])
        value = float(row[1])
        if value < 100:  # Filter out values greater than 100 (adjust threshold as needed)
            x.append(index)
            y.append(value)

    # Plot the filtered data
    plt.plot(x, y, marker='o', linestyle='-')
    plt.xlabel('Item')
    plt.ylabel('Time(s)')
    plt.title(file_name)
    plt.grid(True)
    plt.show()
