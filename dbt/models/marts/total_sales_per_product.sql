WITH sales_data AS (
    SELECT
        product_name,
        SUM(price*quantity) AS total_sales,
        COUNT(sale_id) AS total_transactions
    FROM
        {{ ref('sales') }}
    GROUP BY
        product_name
)
SELECT
    product_name,
    total_sales,
    total_transactions
FROM
    sales_data