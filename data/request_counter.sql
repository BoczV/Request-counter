CREATE TABLE IF NOT EXISTS HTTP (
    id INT UNIQUE PRIMARY KEY,
    request varchar(255),
    number INT,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES USERS (user_id)
);

CREATE TABLE IF NOT EXISTS USERS (
    user_id INT UNIQUE PRIMARY KEY,
    user_name varchar(255)
);
