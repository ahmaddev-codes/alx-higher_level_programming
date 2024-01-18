-- creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.

-- create the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- use database
USE hbtn_0d_usa;

-- create table with the default data types, if not exists
-- and if it exists, doesn't fail
CREATE TABLE IF NOT EXISTS states (
    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);