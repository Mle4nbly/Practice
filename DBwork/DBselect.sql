SELECT name, release_year FROM album
WHERE '2018-12-31' >= release_year AND release_year >= '2018-01-01';

SELECT name, duration FROM track
WHERE duration = (SELECT max(duration) FROM track);

SELECT name FROM track
WHERE duration >= '00:03:30';

SELECT name FROM collection
WHERE '2020-12-31' >= release_year AND release_year >= '2018-01-01';

SELECT name FROM musician
WHERE NOT name LIKE '% %';

SELECT name FROM track
WHERE lower(name) LIKE '%my%';
