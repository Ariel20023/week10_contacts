CREATE DATABASE IF NOT EXISTS contacts_db;

USE contacts_db;

CREATE TABLE contacts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    phone_number VARCHAR(20) NOT NULL UNIQUE
);

INSERT INTO contacts (first_name, last_name, phone_number) VALUES
('Ariel', 'Izralevitch', '054-5300888'),
('Avigail', 'Izralevitch', '052-2991895'),
('Beky','Lev','052-2341234'),
('Avraham','Fried','053-5672354');





