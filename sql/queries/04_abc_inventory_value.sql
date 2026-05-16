-- Inventory Value by ABC Classification
SELECT 
    p.abc_classification,
    COUNT(DISTINCT p.part_id) AS part_count,
    ROUND(SUM(i.current_stock * p.unit_cost_usd), 2) AS total_inventory_value_usd,
    ROUND(AVG(s.reliability_score)*100, 2) AS avg_supplier_reliability_percent
FROM autoforge.inventory_levels i
JOIN autoforge.parts_master p ON i.part_id = p.part_id
JOIN autoforge.suppliers s ON p.supplier_id = s.supplier_id
GROUP BY p.abc_classification
ORDER BY total_inventory_value_usd DESC;
