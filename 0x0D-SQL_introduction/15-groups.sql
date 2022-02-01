-- script that lists the number of records with the same score in the table second_table
-- count the value score as number
SELECT score, COUNT(*) AS number FROM second_table
GROUP BY score
ORDER BY score DESC;
