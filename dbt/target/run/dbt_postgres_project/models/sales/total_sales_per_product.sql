
  
    

  create  table "sales"."public"."total_sales_per_product__dbt_tmp"
  
  
    as
  
  (
    WITH sales_data AS (
    SELECT
        ProductName,
        SUM(Price*Quantity) AS total_sales,
        COUNT(SaleID) AS total_transactions
    FROM
        "sales"."public"."sales_data"
    GROUP BY
        ProductName
)
SELECT
    ProductName,
    total_sales,
    total_transactions
FROM
    sales_data
  );
  