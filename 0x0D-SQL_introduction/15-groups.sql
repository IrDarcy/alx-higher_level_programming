-- scrip 16
-- script that lists the number of records with the same score
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
order by score DESC;
