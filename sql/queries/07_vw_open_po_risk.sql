-- VIEW 3: Open Purchase Orders with Risk Score
CREATE OR REPLACE VIEW autoforge.vw_open_po_risk AS
SELECT 
    po.po_id,
    p.part_name,
    s.supplier_name,
    po.expected_delivery_date,
    COALESCE(po.actual_delivery_date, CURRENT_DATE) AS last_known_date,
    po.status,
    CASE 
        WHEN po.actual_delivery_date IS NULL AND po.expected_delivery_date < CURRENT_DATE 
            THEN 'HIGH RISK - Delayed'
        WHEN po.status = 'Delivered' AND po.actual_delivery_date <= po.expected_delivery_date 
            THEN 'On Time'
        ELSE 'At Risk'
    END AS otif_status,
    s.avg_lead_time_days,
    (CURRENT_DATE - po.order_date) AS days_since_order
FROM autoforge.purchase_orders po
JOIN autoforge.parts_master p ON po.part_id = p.part_id
JOIN autoforge.suppliers s ON po.supplier_id = s.supplier_id
WHERE po.status != 'Delivered';
