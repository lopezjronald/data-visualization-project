import matplotlib.pyplot as plt

# exercise 15-1
x_values = range(1, 6)
y_values = [pow(x, 3) for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=20)

ax.set_title("Cubed Numbers", fontsize=16)
ax.set_xlabel("Values", fontsize=10)
ax.set_ylabel("Cubed Values", fontsize=10)

ax.axis([0, 10, 0, 200])
plt.show()

x_values = range(1, 5000)
y_values = [pow(x, 3) for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10)

ax.set_title("Cubed Numbers", fontsize=16)
ax.set_xlabel("Values", fontsize=10)
ax.set_ylabel("Cubed Values", fontsize=10)

ax.axis([0, 5000, 0, 140_000_000_000])
plt.show()

# exercise 15-2

x_values = range(1, 6)
y_values = [pow(x, 3) for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=20)

ax.set_title("Cubed Numbers", fontsize=16)
ax.set_xlabel("Values", fontsize=10)
ax.set_ylabel("Cubed Values", fontsize=10)

ax.axis([0, 10, 0, 200])
plt.show()

x_values = range(1, 5000)
y_values = [pow(x, 3) for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

ax.set_title("Cubed Numbers", fontsize=16)
ax.set_xlabel("Values", fontsize=10)
ax.set_ylabel("Cubed Values", fontsize=10)

ax.axis([0, 5000, 0, 140_000_000_000])
plt.show()

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active
while True:

    # Make a random walk
    rw = RandomWalk(5_000)
    rw.fill_walk()

    # Plot the points in the walk
    plt.style.use('classic')
    # fig, ax = plt.subplots()
    # fig, ax = plt.subplots(figsize=(15, 9))
    fig, ax = plt.subplots(figsize=(10, 6),)
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values, c=point_numbers, linewidth=4)

    # Emphasize the first and last points.

    # Remove the axes.


    plt.show()


# exercise 15-3
