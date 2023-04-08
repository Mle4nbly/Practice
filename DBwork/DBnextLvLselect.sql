SELECT g.id, count(mg.musician_id) FROM genre g
JOIN musiciangenre mg ON g.id = mg.genre_id
GROUP BY g.id;

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

SELECT c.name, t.name FROM trackcollection tc
LEFT JOIN collection c ON c.id = tc.collection_id
JOIN track t ON t.id = tc.track_id
JOIN musicianalbum m ON m.album_id = t.album_id
WHERE m.musician_id = 6;

SELECT a.name, count(DISTINCT g.genre_id) FROM album a
JOIN musicianalbum m ON m.album_id = a.id 
JOIN musiciangenre g ON g.musician_id = m.musician_id
GROUP BY a.name
HAVING count(DISTINCT g.genre_id) > 1;

SELECT t.name FROM track t
LEFT JOIN trackcollection t2 ON t.id = t2.track_id
WHERE t2.collection_id IS NULL;

SELECT m.musician_id FROM musicianalbum m
JOIN track t ON m.album_id = t.album_id
WHERE t.duration = (SELECT min(duration) FROM track);

SELECT c.name 
FROM (SELECT a.name AS name, count(t.id) AS num_of_tracks FROM track t JOIN album a ON t.album_id = a.id GROUP BY a.name) c
JOIN (SELECT min(c2.num_of_tracks) AS min_count FROM (SELECT a2.name AS name, count(t2.id) AS num_of_tracks FROM track t2 JOIN album a2 ON t2.album_id = a2.id GROUP BY a2.name) c2) mc 
ON c.num_of_tracks = mc.min_count;












