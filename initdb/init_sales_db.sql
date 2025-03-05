-- CREATE DATABASE sales;


CREATE TABLE sales_data (
    SaleID INTEGER,
    ProductID VARCHAR(255),
    ProductName VARCHAR(255),
    Brand VARCHAR(255),
    Category VARCHAR(255),
    RetailerID INTEGER,
    RetailerName VARCHAR(255),
    Channel VARCHAR(255),
    Location VARCHAR(255),
    Quantity INTEGER,
    Price INTEGER,
    Date DATE
);

-- Indexing the columns that are queried frequently, especially in WHERE, JOIN, ORDER BY, or GROUP BY clauses.
-- CREATE INDEX index_name ON table_name (column_name);