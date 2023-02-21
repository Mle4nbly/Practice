
CREATE TABLE IF NOT EXISTS musician(
	id SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT NULL
);

CREATE TABLE IF NOT EXISTS genre(
	id SERIAL PRIMARY KEY,
	name VARCHAR(60) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS musiciangenre(
	musician_id INTEGER REFERENCES musician(id),
	genre_id INTEGER REFERENCES genre(id),
	CONSTRAINT musician_genre PRIMARY KEY (musician_id, genre_id)
);

CREATE TABLE IF NOT EXISTS album(
	id SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT NULL,
	release_year DATE
);

CREATE TABLE IF NOT EXISTS musicianalbum(
	musician_id INTEGER REFERENCES musician(id),
	album_id INTEGER REFERENCES album(id),
	CONSTRAINT musician_album PRIMARY KEY (musician_id, album_id)
);

CREATE TABLE IF NOT EXISTS track(
	id SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT NULL,
	duration TIME,
	album_id INTEGER REFERENCES album(id)
);

CREATE TABLE IF NOT EXISTS collection(
	id SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT NULL,
	release_year DATE
);

CREATE TABLE IF NOT EXISTS trackcollection(
	track_id INTEGER REFERENCES track(id),
	collection_id INTEGER REFERENCES collection(id),
	CONSTRAINT track_collection PRIMARY KEY (track_id, collection_id)
);