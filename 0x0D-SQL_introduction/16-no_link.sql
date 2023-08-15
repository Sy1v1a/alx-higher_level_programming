--diplay score name in desc order
SELECT score, name
FROM second_table
HAVING name IS NOT NULL
ORDER BY score DESC;
