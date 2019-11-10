CREATE DATABASE communications_server

CREATE TABLE Users (
  id SERIAL PRIMARY KEY,
  email VARCHAR(255) unique,
  username VARCHAR(255),
  hashed_password VARCHAR(80)
);