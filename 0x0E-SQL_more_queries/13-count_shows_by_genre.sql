SELECT genres.name AS genre, COUNT(*) AS number_of_shows
FROM genres
INNER JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
