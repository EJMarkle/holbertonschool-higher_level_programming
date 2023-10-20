-- Computes the average score in second_table. 
ALTER TABLE second_table;
ADD COLUMN average;
UPDATE second_table SET average = AVG(score);