-- example
SELECT cities.id, states.name FROM cities
INNER JOIN
states
ON cities.state_id = states.id
WHERE states.name = "California"
GROUP BY cities.id;
