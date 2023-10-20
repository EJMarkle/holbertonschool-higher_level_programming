-- Computes the average score in second_table. 
ALTER TABLE second_table 
ADD COLUMN average DECIMAL(10,4);
UPDATE second_table 
SET average = (SELECT AVG(score) FROM second_table);