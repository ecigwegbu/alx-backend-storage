-- alter the default for column country in table users

ALTER TABLE users MODIFY country ENUM('US', 'CO', 'TN') NOT NULL;
