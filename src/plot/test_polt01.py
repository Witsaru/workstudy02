import matplotlib.pyplot as plt
import csv

# Read the CSV file
with open('csv_data/Witsarut_Butdee/real_Left_Witsarut_Butdee_9.csv', 'r') as file:
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
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('real_time_right_toey')
plt.grid(True)
plt.show()
