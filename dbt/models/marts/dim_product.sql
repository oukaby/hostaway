WITH product AS (
    SELECT
        product_id,
        product_name
    FROM
        {{ ref('sales') }}
)

SELECT
    *
FROM
    product