SELECT g.name, count(mg.musician_id) FROM genre g
JOIN musiciangenre mg ON g.id = mg.genre_id
GROUP BY g.name;

SELECT count(t.id) FROM track t
JOIN album a ON t.album_id = a.id
WHERE a.release_year >= '2019-01-01' AND a.release_year <= '2020-12-31';

SELECT a.id, avg(t.duration) FROM album a
JOIN track t ON t.album_id = a.id
GROUP BY a.id
ORDER BY a.id ASC;

SELECT m.musician_id FROM musicianalbum m
LEFT JOIN album a ON m.album_id = a.id AND 
a.release_year >= '2020-01-01' AND a.release_year <= '2020-12-31'
GROUP BY m.musician_id
HAVING count(a.id) = 0;

SELECT DISTINCT c.name FROM trackcollection tc
LEFT JOIN collection c ON c.id = tc.collection_id
JOIN track t ON t.id = tc.track_id
JOIN musicianalbum ma ON ma.album_id = t.album_id
JOIN musician m ON m.id = ma.musician_id
WHERE m.name = 'dyrachyo';

SELECT DISTINCT a.name FROM album a
JOIN musicianalbum ma ON a.id = ma.album_id
JOIN musician m ON m.id = ma.musician_id
JOIN musiciangenre mg ON mg.musician_id = m.id
GROUP BY a.name
HAVING count(DISTINCT mg.genre_id) > 1;

SELECT t.name FROM track t
LEFT JOIN trackcollection t2 ON t.id = t2.track_id
WHERE t2.collection_id IS NULL;

SELECT DISTINCT m.name FROM musicianalbum ma
JOIN track t ON ma.album_id = t.album_id
JOIN musician m ON m.id = ma.musician_id
WHERE t.duration = (SELECT min(duration) FROM track);

SELECT a.name FROM album a
JOIN track t ON t.album_id = a.id
GROUP BY a.id
HAVING count(t.id) = (
	SELECT count(id) FROM track
	GROUP BY album_id
	ORDER BY 1
	LIMIT 1
);












