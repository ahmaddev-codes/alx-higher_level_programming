-- creates the MySQL server user user_0d_1.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';

-- Granting privileges
GRANT ALL
ON *.*
TO 'user_0d_1'@'localhost'
WITH GRANT OPTION;

-- Confirms user privileges and saves
FLUSH PRIVILEGES;
