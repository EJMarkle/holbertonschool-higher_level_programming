-- Lists number of records with the same score in second_table. 
SELECT score, COUNT(*) AS NUM 
FROM second_table GROUP BY score 
ORDER BY score DESC;