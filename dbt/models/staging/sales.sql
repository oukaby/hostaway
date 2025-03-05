WITH rename_sales_raw_data AS (
    SELECT
        SaleID as sale_id,
        ProductID as product_id,
        ProductName as product_name,
        Brand as brand,
        Category as category,
        RetailerID as retailer_id,
        RetailerName as retailer_name,
        Channel as channel,
        Location as location,
        Quantity as quantity,
        Price as price,
        Date as date
    FROM
        {{ source('raw_sales','sales_data') }}
)

SELECT
    *
FROM
    rename_sales_raw_data