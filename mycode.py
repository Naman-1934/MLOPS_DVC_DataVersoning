import pandas as pd
import os

# Create a sample dataframe 

data = {'Name': ['Alice', 'Bob', 'Charlis'],
        'Age': [25,30,35],
        'City': ['New York', 'Los Angles', 'Chicago']
}

df = pd.DataFrame(data)

# Add a new row to df for v2
new_row_loc = {'Name': 'GF1', 'Age': 22, 'City': 'Delhi'}
df.loc[len(df.index)] = new_row_loc


# This is ensures that root direcctory exists at the root levels.
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

# Define the file path
file_path = os.path.join(data_dir, 'sample_data.csv')

# save the dataframe to a csv file, including column names
df.to_csv(file_path, index=False)

print(f"CSV file saved at: {file_path}")