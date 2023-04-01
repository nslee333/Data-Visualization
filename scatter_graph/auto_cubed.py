import matplotlib.pyplot as plt

fig, ax = plt.subplots()


while True:
    x_value = input("Please enter a value to be cubed:")
    
    try:
        x_number = int(x_value)
        
    except:
        print("Please enter a numeric digit that is below 1,000,000.")
        continue
    
    if x_number > 1_000_000:
        print("Please enter a number smaller than 1,000,000.")
        continue
    
    break


x_values = range(1, int(x_value))
y_values = [x**3 for x in x_values]


ax.scatter(x_values, y_values, s=10)

ax.set_title("Cubed numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

plt.show()