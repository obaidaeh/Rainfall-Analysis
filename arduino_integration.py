import matplotlib.pyplot as plt
import numpy as np
# Read data from file
with open('DATA2.txt', 'r') as file:
    data = file.readlines()

# Split data into x and y values
x_values = []
y_values = []
for line in data:
    x, y = line.strip().split(',')
    x_values.append(float(x))
    y_values.append(float(y))

# Create contour plotz
plt.tricontour(x_values, y_values, np.random.rand(len(x_values)), levels=14, linewidths=0.5, colors='k')
plt.tricontourf(x_values, y_values, np.random.rand(len(x_values)), levels=14)
plt.colorbar()
plt.xlabel('Moisture Values')
plt.ylabel('Temperature Values')
plt.title('Contour Plot')
plt.show()

# Create bar plot
x_pos = np.arange(len(x_values))
plt.bar(x_pos, y_values)
plt.xticks(x_pos, x_values)
plt.xlabel('Moisture Values')
plt.ylabel('Temperature Values')
plt.title('Bar Plot')
plt.show()
