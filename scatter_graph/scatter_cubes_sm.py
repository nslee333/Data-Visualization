import matplotlib.pyplot as plt


x_values = [1, 2, 3, 4, 5]
y_values = [x**3 for x in x_values]

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

ax.axis([0, 5, 0, 75])

plt.show()