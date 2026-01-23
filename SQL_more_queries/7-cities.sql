-- TASK7

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa ;

CREATE TABLE  IF NOT EXISTS cities (
        id INT UNIQUE NOT NULL AUTO_INCREMENTL PRIMARY KEY,
        state_id INT NOT NULL,
        FOREIGN KEY (state_id) references (state.id),
        name VARCHAR (256) NOT NULL
);
