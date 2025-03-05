import pandas as pd
import numpy as np


# Path to the CSV file
CSV_FILE_PATH = '/opt/airflow/python/data/generated_sales_data.csv'


# Function to replace empty strings based on the value in another column and dictionary
def replace_empty_based_on_another_column(df, column_to_replace, match_column, replacement_dict):
    df[column_to_replace] = df.apply(
        lambda row: replacement_dict.get(row[match_column], row[column_to_replace]) 
        if row[column_to_replace] == ' ' else row[column_to_replace], 
        axis=1
    )
    return df


def process_data(csv_file_path):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file_path)

    # Data Quality Handling
    # Drop duplicate rows
    df.drop_duplicates(inplace=True)
    
    # Replace ProductID values when null based on ProductName field mapping
    replacement_dict = {
        'Laptop': 1, 
        'Coffee Maker': 2,
        'Smartphone': 3,
        'Desk Chair': 4,
        'Blender': 5,
        'Desk Lamp': 6,
        'Office Desk': 7,
        'Coffee Machine': 8
        }

    df = replace_empty_based_on_another_column(df, 'ProductID', 'ProductName', replacement_dict)

    # Remove non-numeric characters
    df['Price'] = df['Price'].str.replace(r'\D+', '', regex=True)
    # Convert the column to numeric type
    df['Price'] = df['Price'].astype(int)
    df['ProductID'] = df['ProductID'].astype(int)

    # Optionally, handle incremental loading logic: This would require a method to track the lastest data (e.g., last Date)

    return df

def main():
    # Process the data
    processed_data = process_data(CSV_FILE_PATH)
    
    # Save processed data to a new file (for example) or return it for later steps
    processed_data.to_csv('/opt/airflow/python/data/processed_sales_data.csv', index=False)  # Save processed data
    print("Data processed and saved to '/opt/airflow/python/data/processed_sales_data.csv'.")

if __name__ == '__main__':
    main()
