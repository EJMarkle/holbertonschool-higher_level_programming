-- Lists number of records with the same score in second_table. 
SELECT name, COUNT(*) AS NUM FROM second_table GORUP BY score DESC;