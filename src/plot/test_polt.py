import matplotlib.pyplot as plt
import csv

filenames = ['csv_data/Teerajate_Panpuek/time_poor_Teerajate_Panpuek_1.csv',
            'csv_data/Teerajate_Panpuek/time_poor_Teerajate_Panpuek_2.csv',
            'csv_data/Teerajate_Panpuek/time_poor_Teerajate_Panpuek_3.csv',
            'csv_data/Teerajate_Panpuek/time_poor_Teerajate_Panpuek_4.csv',
            'csv_data/Teerajate_Panpuek/time_poor_Teerajate_Panpuek_5.csv']

x_all = []
y_all = []

# Plot data from each file
for filename in filenames:
    # Read the CSV file
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    
    # Extract the y values from the data
    y = [float(row[1]) for row in data[1:]]
    
    # Calculate the new x values by shifting previous x range
    x = [val + len(y_all) for val in range(len(y))]
    
    # Append data to the lists
    x_all.extend(x)
    y_all.extend(y)
    
    # Plot the data
    # plt.plot(x, y, marker='o', linestyle='-', label=filename)

# Plot the data
plt.plot(x_all, y_all, marker='o', linestyle='-')
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('real_time_left_Teerajate_Panpuek')
plt.grid(True)
plt.show()
