-- VIEW 1: Critical JIT Stock Status (most important daily dashboard)
CREATE OR REPLACE VIEW autoforge.vw_critical_jit_stock AS
SELECT 
    p.part_id,
    p.part_name,
    p.category,
    p.abc_classification,
    p.critical_for_jit,
    i.current_stock,
    i.reorder_point,
    i.safety_stock,
    (i.current_stock::DECIMAL / NULLIF(i.reorder_point, 0)) * 100 AS percent_of_reorder,
    CASE 
        WHEN i.current_stock <= i.reorder_point THEN 'STOCKOUT RISK - STOP LINE IMMEDIATELY'
        WHEN i.current_stock <= i.safety_stock THEN 'LOW STOCK - REORDER NOW'
        ELSE 'OK'
    END AS stock_status
FROM autoforge.parts_master p
JOIN autoforge.inventory_levels i ON p.part_id = i.part_id
WHERE p.critical_for_jit = TRUE
ORDER BY percent_of_reorder ASC;
