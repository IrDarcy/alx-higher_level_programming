-- script 21
-- script that displays the max temperatureof each state
SELECT state, MAX(value) AS max_temp FROM temperatures
GROUP BY state
ORDER BY state ASC
LIMIT 3;
