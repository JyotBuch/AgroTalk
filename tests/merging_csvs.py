import pandas as pd
import glob
import os

# Use glob to find all csv files matching the pattern
csv_files = glob.glob('/Users/jyotbuch/Downloads/CroplandCROS_AOI_Data *.csv')

# Initialize an empty list to hold DataFrames
dfs = []

# Loop through each file
for file in csv_files:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file)

    # Extract the year from the filename
    year = int(file.split('_Data ')[1].split('.csv')[0])

    # Add the 'Year' column to the DataFrame
    df['Year'] = year

    # Append the DataFrame to the list
    dfs.append(df)

# Concatenate all DataFrames in the list into a single DataFrame
merged_df = pd.concat(dfs, ignore_index=True)

# Save the merged DataFrame to a new CSV file
merged_df.to_csv('merged_data.csv', index=False)

print("Merged data saved to 'merged_data.csv'")