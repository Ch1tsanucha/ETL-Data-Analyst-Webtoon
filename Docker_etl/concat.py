import pandas as pd

# List to hold dataframes
dataframes = []

# Loop through the files and read them into dataframes
for i in range(10):  # data0.csv to data9.csv
    filename = f'data{i}.csv'
    try:
        df = pd.read_csv(filename)
        dataframes.append(df)
    except FileNotFoundError:
        print(f"{filename} not found. Skipping.")

# Concatenate all dataframes
if dataframes:  # Check if there are any dataframes to concatenate
    combined_df = pd.concat(dataframes, ignore_index=True)
    combined_df.to_csv('data.csv', index=False)  # Write to data.csv
    print("Data concatenated successfully into data.csv.")
else:
    print("No data files found to concatenate.")
