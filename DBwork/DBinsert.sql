DELETE FROM musiciangenre;
DELETE FROM musicianalbum;
DELETE FROM trackcollection;
DELETE FROM musician;
DELETE FROM genre;
DELETE FROM track;
DELETE FROM album;
DELETE FROM collection;


INSERT INTO musician(id, name)
VALUES
(1,'ALWAYS WANNA FLY'),
(2, 'RVMZES'),
(3, 'Ukio'),
(4, 'NO NAME'),
(5, 'dyrachyo'),
(6, 'Poete'),
(7, 'Seleri'),
(8, 'Solo');

INSERT INTO genre(id, name)
VALUES
(1, 'Hip-Hop'),
(2, 'Rock'),
(3, 'Pop'),
(4, 'Musicl'),
(5, 'Jazz');

INSERT INTO album(id, name, release_year)
VALUES
(1, '322 Dollars', '15/09/2000'),
(2, 'Once in a major', '15/09/2000'),
(3, '1 X 9', '15/09/2000'),
(4, 'Major winner', '15/09/2000'),
(5, 'The World', '15/09/2000'),
(6, 'Future', '15/09/2000'),
(7, 'Moon Adventure', '15/09/2000'),
(8, 'BreakUP', '15/09/2000');

INSERT INTO track(id, name, duration, album_id)
VALUES
(1, 'Daubi', '00:02:30', 4),
(2, 'My carry', '00:02:30', 1),
(3, 'Iceberg BETS', '00:02:30', 7),
(4, '5 majors', '00:02:30', 2),
(5, 'NIX casts', '00:02:30', 3),
(6, 'Joke', '00:02:30', 6),
(7, '3 years 2 months 2 days', '00:02:30', 1),
(8, 'Public legend', '00:02:30', 3),
(9, 'Golovach?', '00:02:30', 3),
(10, 'Flusk', '00:02:30', 8),
(11, 'Sunrise', '00:02:30', 5),
(12, 'Forever all time', '00:02:30', 5),
(13, 'Just track', '00:02:30', 8),
(14, 'Just second track', '00:02:30', 6),
(15, 'Just third track', '00:02:30', 5);

INSERT INTO collection(id, name, release_year)
VALUES
(1,'Defence of TA', '15/09/2000'),
(2,'Winners', '15/09/2000'),
(3,'Rock collection', '15/09/2000'),
(4,'Relax music', '15/09/2000'),
(5,'Motivational music', '15/09/2000'),
(6,'Sad!!', '15/09/2000'),
(7,'Pop collection', '15/09/2000'),
(8,'noitcelloc poP', '15/09/2000');

INSERT INTO musiciangenre(musician_id, genre_id)
VALUES
(1,5),
(2,1),
(3,3),
(4,4),
(5,2),
(6,4),
(7,2),
(8,1);

INSERT INTO musicianalbum(musician_id, album_id)
VALUES
(1,7),
(1,3),
(2,2),
(2,4),
(3,5),
(4,6),
(5,3),
(5,4),
(6,8),
(7,4),
(8,1),
(8,2);

INSERT INTO trackcollection(collection_id, track_id)
VALUES
(1,1), (1,2), (1,4), (1,8), (1,9),
(2,1), (2,4), (2,7), (2,9),
(3,1), (3,5), (3,8), (3,9),
(4,6), (4,10), (4,11), (4,12),
(5,13), (5,14), (5,15),
(6,6), (6,10), (6,13),
(7,13), (7,6), (7,11),
(8,11), (8,6), (8,13);