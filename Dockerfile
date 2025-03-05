# Use official Python image as a base
FROM python:3.9-slim

# Set the working directory
WORKDIR /opt/airflow/dbt

# Upgrade pip to the latest version
RUN pip install --upgrade pip

# Install system dependencies for psycopg2
RUN apt-get update && apt-get install -y \
    libpq-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install system dependencies and Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy DBT project files into the container
COPY dbt /opt/airflow/dbt
