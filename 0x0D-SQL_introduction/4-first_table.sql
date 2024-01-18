-- creates a table called first_table in the current database
-- in MySQL server.

-- create database
CREATE DATABASE IF NOT EXISTS hbtn_0c_0;

-- use databse
USE hbtn_0c_0;

-- create table if it doesn't exist
CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));
