CREATE DATABASE deckly;

USE deckly;

CREATE TABLE if NOT EXISTS user (
    id INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(30),
    name VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    picture VARCHAR(200),
    password VARCHAR(80),
    CONSTRAINT PRIMARY key (id),
    CONSTRAINT UNIQUE (email)
) ENGINE = INNODB;
