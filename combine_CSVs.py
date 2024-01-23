import os
import pandas as pd

csv_directory = os.path.join(os.getcwd(), 'data')
csv_files = [file for file in os.listdir(csv_directory) if file.endswith('.csv')]
combined_df = pd.DataFrame()

for csv_file in csv_files:
    file_path = os.path.join(csv_directory, csv_file)
    df = pd.read_csv(file_path)
    combined_df = pd.concat([combined_df, df], ignore_index=True)

combined_csv_path = './data/combined_data.csv'  # Replace this with the desired name for the combined CSV file
combined_df.to_csv(combined_csv_path, index=False)

print(f'Combined CSV file saved to {combined_csv_path}')
