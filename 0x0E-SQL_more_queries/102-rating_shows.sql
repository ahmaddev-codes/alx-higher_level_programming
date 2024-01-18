-- lists all shows from hbtn_0d_tvshows_rate by their rating.
SELECT
    DISTINCT ts.title,
    SUM(tsr.rate) AS `rating sum`
FROM
    tv_shows ts
LEFT JOIN
    tv_show_ratings tsr
    ON ts.id = tsr.show_id
GROUP BY
    ts.title
ORDER BY
    `rating sum` DESC;
