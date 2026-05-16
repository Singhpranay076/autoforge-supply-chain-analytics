-- Advanced Query with CTE: OTIF % per supplier
WITH recent_deliveries AS (
    SELECT 
        s.supplier_name,
        COUNT(*) AS total_orders,
        SUM(CASE WHEN po.actual_delivery_date <= po.expected_delivery_date THEN 1 ELSE 0 END) AS on_time_orders
    FROM autoforge.purchase_orders po
    JOIN autoforge.suppliers s ON po.supplier_id = s.supplier_id
    WHERE po.actual_delivery_date IS NOT NULL
    GROUP BY s.supplier_name
)
SELECT 
    supplier_name,
    total_orders,
    on_time_orders,
    ROUND((on_time_orders::DECIMAL / total_orders) * 100, 2) AS otif_percent
FROM recent_deliveries
ORDER BY otif_percent DESC;
