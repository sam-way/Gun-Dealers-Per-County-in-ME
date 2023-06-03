import matplotlib.pyplot as plt

# Generate a grouped DataFrame based on the number of dealers in each county
grouped_df = df.groupby('County').size().reset_index(name='Number of Dealers')

# Plotting
plt.figure(figsize=(10,6))
plt.bar(grouped_df['County'], grouped_df['Number of Dealers'])
plt.xlabel('County')
plt.ylabel('Number of Dealers')
plt.title('Number of Dealers in Each County')
plt.xticks(rotation=90)
plt.show()
