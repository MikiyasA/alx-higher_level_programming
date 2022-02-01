-- script that lists all records of the table second_table
-- list all recored of the table and ordered by score
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
