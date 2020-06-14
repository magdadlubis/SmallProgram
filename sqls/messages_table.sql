CREATE TABLE Messages (
    id SERIAL PRIMARY KEY,
    from_id int NOT NULL,
    to_id int NOT NULL,
    text varchar(255),
    creation_date timestamp DEFAULT Now(),
    FOREIGN KEY(from_id) REFERENCES Users(id) ON DELETE CASCADE,
    FOREIGN KEY(to_id) REFERENCES Users(id) ON DELETE CASCADE,
);