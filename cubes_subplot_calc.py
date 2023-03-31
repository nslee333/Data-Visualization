import matplotlib.pyplot as plt

x_values = range(1, 5000)
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

ax.axis([1, 150, 1, 1_250_000])

plt.show()

# How can I automatically calculate the axis?

# ! LEFT AT TRYING TO CHANGE WRONG COMMIT MESSAGES.