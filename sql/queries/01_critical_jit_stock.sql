-- Critical JIT parts at risk of stockout
SELECT 
    p.part_name,
    p.category,
    i.current_stock,
    i.reorder_point,
    i.safety_stock,
    (i.current_stock::DECIMAL / NULLIF(i.reorder_point, 0)) * 100 AS percent_of_reorder_point
FROM autoforge.parts_master p
JOIN autoforge.inventory_levels i ON p.part_id = i.part_id
WHERE p.critical_for_jit = TRUE 
  AND i.current_stock <= i.reorder_point
ORDER BY i.current_stock ASC;
