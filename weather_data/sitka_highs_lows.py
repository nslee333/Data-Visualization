from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[4])
    low = int(row[5])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)

# Plot the high temperatures.
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red')
ax.plot(dates, lows, color='blue')

# Format plot.
ax.set_title("Daily high and temperatures, 2021", fontsize=20)
ax.set_xlabel('', fontsize=14)
fig.autofmt_xdate() 
ax.set_ylabel("Temperature (F)", fontsize=14)
ax.tick_params(labelsize=14)

plt.show()
