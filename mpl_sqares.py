import matplotlib.pyplot as plt

input_values = []
squares = []
for i in range(25):
    input_values.append(i)
    squares.append(i ** 2)
print(len(input_values))
print(len(squares))
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', labelsize=14)
plt.show()

x_values = y_values = []
for i in range(25):
    x_values.append(i)
    y_values.append(i ** 2)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=100)

# Set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()

x_values = range(1, 1001)
y_values = [x ** 2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=(0, 0.8, 0), s=10)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set the range for each axis
ax.axis([0, 1100, 0, 1_100_000])

plt.show()

# Using colormap

x_values = range(1, 1001)
y_values = [x ** 2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set the range for each axis
ax.axis([0, 1100, 0, 1_100_000])

# shows plt
# plt.show()

# saves plot to a file
plt.savefig('squarese_plot.png')
