# Write your MySQL query statement below
SELECT weather.id FROM weather
JOIN weather W ON DATEDIFF(weather.recordDate, W.recordDate)= 1
AND weather.temperature > W.temperature