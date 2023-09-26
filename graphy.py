import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Specify the full path to the CSV file
csv_file_path = 'C:\\module visualization\\matplotlib\\personality_responses3.csv'
df = pd.read_csv(csv_file_path, header=0)

# Define categories and responses
categories = df['Categories']
responses = df['Response']

# Define the response scale
response_scale = [1, 2, 3, 4, 5, 6, 7]  # Response scale from 1 to 7

# Create a spider chart
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, polar=True)

# Number of categories
num_categories = len(categories)

# Define angles for the spider chart
angles = np.linspace(0, 2 * np.pi, num_categories, endpoint=False).tolist()

# Make the spider chart circular
angles += angles[:1]

# Plot the data
values = responses.values.tolist()  # Get all response values
values += values[:1]  # Close the loop
ax.fill(angles, values, alpha=0.25)

# Add labels to the chart
plt.xticks(angles[:-1], categories, fontsize=10)
plt.yticks([1, 2, 3, 4, 5, 6, 7], [str(i) for i in response_scale], color="grey", size=10)

# Show the chart
plt.title("Personality Spider Chart")
plt.show()
