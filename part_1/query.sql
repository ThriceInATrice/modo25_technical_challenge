-- this query summarizes the totaly quantity, sales, and commission
-- for each campaign run by a specific publisher
SELECT 
    campaign, 
    SUM(quantity) AS "total quantity", 
    SUM(sale_value) AS "total sale value", 
    SUM(commission_value) AS "total commission value"
FROM 
    publisher_campaign_report 
JOIN 
    publisher ON publisher_campaign_report.publisher_id = publisher.publisher_id
WHERE 
    publisher_id = 1
GROUP BY 
    campaign
;