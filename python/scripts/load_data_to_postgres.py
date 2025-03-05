import pandas as pd
from airflow.providers.postgres.hooks.postgres import PostgresHook


# Path to the processed CSV file
PROCESSED_CSV_PATH = '/opt/airflow/python/data/processed_sales_data.csv'

def load_data_to_postgres(csv_file_path):
    # Read the processed data
    df = pd.read_csv(csv_file_path)

    # Connect to PostgreSQL using Airflow's PostgresHook
    pg_hook = PostgresHook(postgres_conn_id='postgres_conn')
    conn = pg_hook.get_conn()
    cursor = conn.cursor()

    # Insert data from DataFrame into PostgreSQL table
    for index, row in df.iterrows():
        query = """
        INSERT INTO sales_data (SaleID, ProductID, ProductName, Brand, Category, RetailerID, RetailerName, Channel, Location, Quantity, Price, Date)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (row['SaleID'], row['ProductID'], row['ProductName'], row['Brand'], row['Category'], row['RetailerID'], row['RetailerName'], row['Channel'], row['Location'], row['Quantity'], row['Price'], row['Date'])
        cursor.execute(query,values)
    
    conn.commit()
    cursor.close()
    conn.close()
    print("Data successfully loaded into PostgreSQL.")

if __name__ == '__main__':
    load_data_to_postgres(PROCESSED_CSV_PATH)
