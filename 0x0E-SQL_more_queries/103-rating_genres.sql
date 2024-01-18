-- lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT
    tg.name,
    SUM(tsr.rate)
FROM
    tv_genres tg
LEFT JOIN
    tv_show_genres tsg
    ON tg.id = tsg.genre_id
LEFT JOIN
    tv_shows ts
    ON tsg.show_id = ts.id
LEFT JOIN
    tv_show_ratings tsr
    ON tsr.show_id = ts.id
GROUP BY
    tg.name
ORDER BY
    SUM(tsr.rate) DESC;