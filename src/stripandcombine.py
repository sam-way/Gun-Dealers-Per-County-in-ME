import re
import pandas as pd
import matplotlib.pyplot as plt

# Function to build town-to-county map
def build_town_to_county_map():
    town_to_county = {}
    with open('maine_towns_counties.csv', 'r') as f:
        for line in f:
            town, county = line.strip().split(',')
            town_to_county[town.strip().lower()] = county.strip()
    return town_to_county

# Function to map town to county
def town_to_county_mapper(town_name):
    town_to_county = build_town_to_county_map()
    town_name = town_name.strip().lower()
    return town_to_county.get(town_name, "Unknown")

# Read the input file
with open('input.txt', 'r') as f:
    content = f.read()

# Extract lines
lines = re.findall(r'\[(.*?)\]', content)

data_for_csv = []

# Process each line
for line in lines:
    items = line.replace("'", "").split(',')
    items = [item.strip() for item in items]
    if len(items) < 9 or items[2].strip() != 'Dealer':
        continue
    county = town_to_county_mapper(items[3].strip())
    items[4] = county  # Replacing 'ME' with the county name
    
 # Checking if dealer's name ends with '.html'
    dealer_name = items[7].split('<br>')[0]  # Extracting dealer's name
    if dealer_name.endswith('.html'):
        dealer_name = 'Unknown'

    # Checking if address starts with a number
    address = ' '.join(items[7].split('<br>')[1:4])  # Extracting address
    if not address.split() or not address.split()[0].isdigit():
        address = 'Unknown'

    data_for_csv.append(items[:6] + [dealer_name, address])  # Adding dealer's name and address to the data


# Convert data into a DataFrame
df = pd.DataFrame(data_for_csv, columns=['Gun Shop Name', 'Unknown', 'Type', 'Town', 'County', 'Phone Number', 'Dealer Name', 'Address'])
df = df.drop(columns=['Unknown'])

# Sorting DataFrame by 'County' column
df = df.sort_values('County')

# Save DataFrame to a CSV file
df.to_csv('List of Maine Gun Dealers by County.csv', index=False)

# Generate a grouped DataFrame based on the number of dealers in each county
grouped_df = df.groupby('County').size().reset_index(name='Number of Dealers')

# Plotting
plt.figure(figsize=(10,6))
plt.bar(grouped_df['County'], grouped_df['Number of Dealers'])
plt.xlabel('County')
plt.ylabel('Number of Dealers')
plt.title('Number of Dealers in Each County')
plt.xticks(rotation=90)

# Save the plot as a file
plt.savefig('Bar Graph of Gun Dealers.png', bbox_inches='tight', dpi=300)


