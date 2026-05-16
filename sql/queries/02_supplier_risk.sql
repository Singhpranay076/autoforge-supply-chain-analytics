-- High-risk A-class suppliers
SELECT 
    s.supplier_name,
    p.category,
    COUNT(*) AS part_count,
    ROUND(AVG(s.on_time_delivery_rate), 2) AS avg_otd_rate,
    SUM(i.current_stock * p.unit_cost_usd) AS total_inventory_value_usd
FROM autoforge.inventory_levels i
JOIN autoforge.parts_master p ON i.part_id = p.part_id
JOIN autoforge.suppliers s ON p.supplier_id = s.supplier_id
WHERE p.abc_classification = 'A'
GROUP BY s.supplier_name, p.category
HAVING AVG(s.on_time_delivery_rate) < 96
ORDER BY total_inventory_value_usd DESC;
