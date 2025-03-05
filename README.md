# Senior Data Engineer Take-Home Assignment

👋 Hi there it's Robin

## Overview
This project demonstrates the setup of an automated data pipeline for processing, transforming, and loading sales data into a PostgreSQL database using Docker Compose, Airflow, and DBT. The pipeline is structured into the following main stages:

1. Ingestion and Processing: The ingest_and_process_data.py script processes the raw generated_sales_data.csv file, handling data quality issues before storing the processed data into a new file processed_sales_data.csv.

2. Data Loading: The processed sales data is loaded into PostgreSQL via the load_data_to_postgres.py script, using Docker Compose to run a PostgreSQL container.

3. Data Transformation: DBT (Data Build Tool) is used to transform the raw data into useful analytics-ready tables.

4. Orchestration with Airflow: An Airflow DAG is created to automate and orchestrate the entire pipeline, from ingestion to transformation.

### Key Technologies Used
- Python: For scripts to process and load data.
- PostgreSQL: To store the sales data in a relational database.
- Airflow: To manage the orchestration of the ETL pipeline.
- DBT: To perform transformations on the sales data.
- Docker Compose: To create and manage the containers for PostgreSQL, Airflow, and DBT.

## Setup Instructions
### Prerequisites

1. Docker and Docker Compose must be installed on your machine.
    - Install Docker: https://docs.docker.com/get-docker/
    - Install Docker Compose: https://docs.docker.com/compose/install/

2. Python 3.x: For running the ingestion and data loading scripts.

### Steps to run the Pipeline

1. Clone the Repository: Download or clone the repository containing the project files.
    git clone <your-repository-url>
    cd <your-repository-name>

2. Start the Containers: Run the following command to start all the services.
    - docker-compose up --build
    (This will start PostgreSQL, Airflow webserver, Airflow scheduler, and DBT containers as defined in the docker-compose.yml file.)

3. Running Airflow DAG
    To trigger the DAG manually:
    - Open the Airflow web UI: http://localhost:8080
    - Use username: airflow and password: airflow to login
    - In the DAGs section, locate the sales_data_ingestion_dag.
    - Trigger the DAG to start processing the data and running the DBT transformations.
    You can monitor the progress of the tasks through the Airflow UI.


### Project Architecture
The project architecture consists of several components working together:

- PostgreSQL Database: Stores the processed and transformed sales data.
- DBT: Performs transformations on the raw sales data to create staging, dimensional, and aggregated models.
- Airflow: Orchestrates the pipeline tasks by setting up a DAG and task dependencies to run the scripts and DBT models in sequence.
- Docker Compose: Manages the different services as containers (PostgreSQL, DBT, and Airflow).

### DBT Models
Staging Model (sales): This model renames and cleans the raw sales data, preparing it for further analysis.
Dimensional Model (dim_product): Adds product-level information such as product id and product name.
Aggregated Model (total_sales_per_product): Aggregates the total sales per product, calculating the total volume of sales for each product.

### DBT Test
The sales staging model includes several data quality tests:

- sale_id: Ensures it is unique and not null.
- product_id: Ensures it is not null.
- product_name: Validates against a set of accepted values (e.g., 'Laptop', 'Blender').
- category: Validates against accepted values (e.g., 'Electronics', 'Furniture').
- retailer_id: Ensures it is not null.
- channel: Validates against accepted values ('Online', 'Offline').

### Indexing
At this stage, indexing is not implemented because it was determined to be unnecessary for the current dataset size and downsteam use. However, as the dataset grows and more dbt models are being build, it may be beneficial to consider adding indexes to improve query performance.