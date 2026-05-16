-- VIEW 2: Supplier Risk Dashboard
CREATE OR REPLACE VIEW autoforge.vw_supplier_risk AS
SELECT 
    s.supplier_name,
    p.abc_classification,
    COUNT(DISTINCT p.part_id) AS part_count,
    ROUND(AVG(s.on_time_delivery_rate), 2) AS avg_otd_percent,
    ROUND(SUM(i.current_stock * p.unit_cost_usd), 2) AS total_inventory_value_usd,
    ROUND(AVG(s.avg_lead_time_days), 1) AS avg_lead_time_days
FROM autoforge.inventory_levels i
JOIN autoforge.parts_master p ON i.part_id = p.part_id
JOIN autoforge.suppliers s ON p.supplier_id = s.supplier_id
GROUP BY s.supplier_name, p.abc_classification
HAVING AVG(s.on_time_delivery_rate) < 96 OR AVG(s.avg_lead_time_days) > 10;
