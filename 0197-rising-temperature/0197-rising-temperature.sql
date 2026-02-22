SELECT w.id
FROM Weather w
JOIN Weather p
  ON p.recordDate = DATE_SUB(w.recordDate, INTERVAL 1 DAY)
WHERE w.temperature > p.temperature;