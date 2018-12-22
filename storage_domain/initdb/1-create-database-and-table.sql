DROP DATABASE IF EXISTS memegen;
CREATE DATABASE memegen;

\c memegen;

CREATE TABLE memes(
	width INTEGER,
	height INTEGER,
	base64 TEXT,
	mimetype VARCHAR(10),
	top_text TEXT,
	bottom_text TEXT,
	uid VARCHAR(13),
	base64_600_thumb TEXT,
	base64_200_thumb TEXT
);

CREATE TABLE templates(
	width INTEGER,
	height INTEGER,
	base64 TEXT,
	mimetype VARCHAR(10),
	uid VARCHAR(13),
	base64_600_thumb TEXT,
	base64_200_thumb TEXT
);