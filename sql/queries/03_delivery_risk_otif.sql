-- Delivery performance & risk scoring
SELECT 
    po.po_id,
    p.part_name,
    s.supplier_name,
    po.expected_delivery_date,
    COALESCE(po.actual_delivery_date, CURRENT_DATE) AS last_known_date,
    CASE 
        WHEN po.actual_delivery_date IS NULL AND po.expected_delivery_date < CURRENT_DATE 
            THEN 'HIGH RISK - Delayed'
        WHEN po.status = 'Delivered' AND po.actual_delivery_date <= po.expected_delivery_date 
            THEN 'On Time'
        ELSE 'At Risk'
    END AS otif_status,
    CASE 
        WHEN s.avg_lead_time_days > 12 THEN 'High Lead Time Risk'
        WHEN s.avg_lead_time_days BETWEEN 8 AND 12 THEN 'Medium Risk'
        ELSE 'Low Risk'
    END AS lead_time_risk
FROM autoforge.purchase_orders po
JOIN autoforge.parts_master p ON po.part_id = p.part_id
JOIN autoforge.suppliers s ON po.supplier_id = s.supplier_id
WHERE po.status != 'Delivered'
ORDER BY lead_time_risk DESC, otif_status;
