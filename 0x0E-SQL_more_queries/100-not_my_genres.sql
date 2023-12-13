-- use db to list all genres not linked to certain show
SELECT `name` FROM tv_genres
WHERE `name` NOT IN (
	SELECT tgg.name FROM tv_genres AS tgg
	JOIN tv_show_genres AS tgs
	ON tgs.genre_id = tgg.id
	JOIN tv_shows AS ts
	ON ts.id = tgs.show_id
	WHERE ts.title ='Dexter'
	)
ORDER BY name;
