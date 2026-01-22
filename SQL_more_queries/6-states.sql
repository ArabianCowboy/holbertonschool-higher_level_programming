-- 6. States table
-- Create database hbtn_0d_usa and table states with primary key

CREATE DATABASE  IF NOT EXISTS hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
	id INT NOT NULL AUTO_INCRMENT,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id)

);
