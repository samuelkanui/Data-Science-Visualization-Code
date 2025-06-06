# Import required libraries
import matplotlib.pyplot as plt
import numpy as np

# Data from the histogram
months = ['07/2019', '08/2019', '09/2019', '10/2019', '11/2019']
search = [50, 53, 59, 56, 62]  # Blue (Search traffic in thousands)
direct = [39, 47, 42, 51, 51]  # Pink (Direct traffic in thousands)
social_media = [70, 80, 90, 87, 92]  # Yellow (Social Media traffic in thousands)

# Set the bar width
bar_width = 0.25

# Set the position of the bars
r1 = np.arange(len(months))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]

# Create the histogram
plt.figure(figsize=(10, 6))
bars1 = plt.bar(r1, search, color='blue', width=bar_width, label='Search')
bars2 = plt.bar(r2, direct, color='pink', width=bar_width, label='Direct')
bars3 = plt.bar(r3, social_media, color='yellow', width=bar_width, label='Social Media')

# Add labels on top of each bar
for bar, value in zip(bars1, search):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1, str(value), 
             ha='center', va='bottom', fontsize=10)

for bar, value in zip(bars2, direct):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1, str(value), 
             ha='center', va='bottom', fontsize=10)

for bar, value in zip(bars3, social_media):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1, str(value), 
             ha='center', va='bottom', fontsize=10)

# Add labels and title
plt.xlabel('Months')
plt.ylabel('Visitors (in thousands)')
plt.title('Visitors by web traffic sources')
plt.xticks([r + bar_width for r in range(len(months))], months)
plt.legend()

# Display the plot
plt.tight_layout()
plt.show()