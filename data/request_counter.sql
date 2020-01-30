DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS http CASCADE;

CREATE TABLE IF NOT EXISTS users (
    user_id INT UNIQUE PRIMARY KEY,
    user_name varchar(255)
);

CREATE TABLE IF NOT EXISTS http (
    id serial NOT NULL PRIMARY KEY,
    request varchar(255),
    number INT,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users (user_id)
);

INSERT INTO http (request, number)
VALUES ('POST', 0);
INSERT INTO http (request, number)
VALUES ('GET', 0);
INSERT INTO http (request, number)
VALUES ('PUT', 0);
INSERT INTO http (request, number)
VALUES ('DELETE', 0);