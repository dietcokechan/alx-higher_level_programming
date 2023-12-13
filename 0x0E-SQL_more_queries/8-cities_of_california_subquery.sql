-- lists all cities of cali
SELECT c.id, c.name FROM cities c, states s
WHERE c.id = s.id
ORDER BY c.id ASC;
