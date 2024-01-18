-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.

SELECT
    tg.name AS genre,
    COUNT(tsg.show_id) AS number_of_shows
FROM
    tv_genres tg
INNER JOIN
    tv_show_genres tsg
GROUP BY
    genre
ORDER BY
    number_of_shows DESC;