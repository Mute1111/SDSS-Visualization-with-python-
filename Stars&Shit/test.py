import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('data.csv')

# Define colors for each object type
colors = {'GALAXY': 'blue', 'STAR': 'orange', 'QSO': 'green'}

# Plot scatter plot of redshift vs. object type
plt.figure(figsize=(10, 6))
for obj_type, color in colors.items():
    plt.scatter(df[df['class'] == obj_type]['redshift'], df[df['class'] == obj_type]['class'], label=obj_type, color=color, alpha=0.5)

plt.title('Redshift vs. Object Type')
plt.xlabel('Redshift')
plt.ylabel('Object Type')
plt.legend()
plt.grid(True)

# Set detailed tick marks on the x-axis
plt.xticks(rotation=45)
plt.gca().get_xaxis().get_major_formatter().set_useOffset(False)  # Disable scientific notation

plt.tight_layout()
plt.show()  