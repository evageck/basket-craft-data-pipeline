WITH raw_orders AS (
    SELECT *
    FROM {{ source('basket_craft', 'orders') }}
),
stg_orders AS (
    SELECT
        order_id,
        user_id,
        primary_product_id,
        price_usd,
        created_at,
        CURRENT_TIMESTAMP AS loaded_at
    FROM raw_orders
)

SELECT *
FROM stg_orders
