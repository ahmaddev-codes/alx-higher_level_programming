## 0x0E-SQL_more_queries
![mysql](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/rtcwz.jpg)

### Learning Objectives
#### General
* How to create a new MySQL user
* How to manage privileges for a user to a database or table
* What’s a `PRIMARY KEY`
* What’s a `FOREIGN KEY`
* How to use `NOT NULL` and `UNIQUE` constraints
* How to retrieve datas from multiple tables in one request
* What are subqueries
* What are `JOIN` and `UNION`

### Tasks
File | Description
-----|------------
[0-privileges.sql](0-privileges.sql) | Script that lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on your server (in `localhost`).
[1-create_user.sql](1-create_user.sql) | Script that creates the MySQL server user `user_0d_1`.
[2-create_read_user.sql](2-create_read_user.sql) | Script that creates the database `hbtn_0d_2` and the user `user_0d_2`.
[3-force_name.sql](3-force_name.sql) | Script that creates the table `force_name` on your MySQL server.
[4-never_empty.sql](4-never_empty.sql) | Script that creates the table `id_not_null` on your MySQL server.
[5-unique_id.sql](5-unique_id.sql) | Script that creates the table `unique_id` on your MySQL server.
[6-states.sql](6-states.sql) | Script that creates the database `hbtn_0d_usa` and the table `states` (in the database `hbtn_0d_usa`) on your MySQL server.
[7-cities.sql](7-cities.sql) | Script that creates the database `hbtn_0d_usa` and the table `cities` (in the database `hbtn_0d_usa`) on your MySQL server.
[8-cities_of_california_subquery.sql](8-cities_of_california_subquery.sql) | Script that lists all the cities of California that can be found in the database `hbtn_0d_usa`.
[9-cities_by_state_join.sql](9-cities_by_state_join.sql) | Script that lists all cities contained in the database `hbtn_0d_usa`.
[10-genre_id_by_show.sql](10-genre_id_by_show.sql) | Script that lists all shows contained in `hbtn_0d_tvshows` that have at least one genre linked.
[11-genre_id_all_shows.sql](11-genre_id_all_shows.sql) | Script that lists all shows contained in the database `hbtn_0d_tvshows`.
[12-no_genre.sql](12-no_genre.sql) | Script that lists all shows contained in `hbtn_0d_tvshows` without a genre linked.
[13-count_shows_by_genre.sql](13-count_shows_by_genre.sql) | Script that lists all genres
[14-my_genres.sql](14-my_genres.sql) | Script that uses the `hbtn_0d_tvshows` database to lists all genres of the show `Dexter`.
[15-comedy_only.sql](15-comedy_only.sql) | Script that lists all Comedy shows in the database `hbtn_0d_tvshows`.
[16-shows_by_genre.sql](16-shows_by_genre.sql) | Script that lists all shows, and all genres linked to that show, from the database `hbtn_0d_tvshows`.

Advanced Tasks | Description
---------------|------------
[100-not_my_genres.sql](100-not_my_genres.sql) | Script that uses the `hbtn_0d_tvshows` database to list all genres not linked to the show `Dexter`.
[101-not_a_comedy.sql](101-not_a_comedy.sql) | Script that lists all shows without the genre `Comedy` in the database `hbtn_0d_tvshows`.
[102-rating_shows.sql](102-rating_shows.sql) | Script that lists all shows from `hbtn_0d_tvshows_rate` by their rating.
[103-rating_genres.sql](103-rating_genres.sql) | Script that lists all genres in the database `hbtn_0d_tvshows_rate` by their rating.
