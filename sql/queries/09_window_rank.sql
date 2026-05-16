-- Advanced Query with Window Function: Rank parts by inventory value within ABC class
SELECT 
    p.abc_classification,
    p.part_name,
    (i.current_stock * p.unit_cost_usd) AS inventory_value_usd,
    RANK() OVER (PARTITION BY p.abc_classification 
                 ORDER BY (i.current_stock * p.unit_cost_usd) DESC) AS value_rank_within_abc
FROM autoforge.inventory_levels i
JOIN autoforge.parts_master p ON i.part_id = p.part_id
ORDER BY p.abc_classification, value_rank_within_abc;
