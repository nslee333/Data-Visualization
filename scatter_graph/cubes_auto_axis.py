import matplotlib.pyplot as plt

x_values = range(1, 5000)
x_max_range = x_values[-1]

y_values = [x**3 for x in x_values]
y_max_range = y_values[-1]

fig, ax = plt.subplots()

ax.scatter(
    x_values, 
    y_values, 
    s=10
)

ax.set_title("Cubed numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

ax.tick_params(labelsize=14)

ax.axis([1, x_max_range + (x_max_range / 10), 
         1, y_max_range + (y_max_range / 10)])

plt.show()
