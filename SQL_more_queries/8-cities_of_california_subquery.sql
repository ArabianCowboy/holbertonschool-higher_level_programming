-- TASK8

SELECT id, name FROM cities
WHERE stat_id = (
	SELECT ID
	FROM states
	WHERE NAME ='California'
)
ORDER BY id ASC;
