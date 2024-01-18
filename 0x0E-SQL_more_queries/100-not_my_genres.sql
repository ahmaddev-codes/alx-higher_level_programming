-- uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT
    tg.name
FROM
    tv_genres tg
WHERE
    tg.id NOT IN (
        -- create a subquery to include
        -- records with "Dexter"
        SELECT
            tsg.genre_id
        FROM
            tv_show_genres tsg
        JOIN
            tv_shows ts
            ON tsg.show_id = ts.id
        WHERE
            ts.title = "Dexter"
    )
ORDER BY
    tg.name ASC;
