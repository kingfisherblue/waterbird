CREATE TABLE Users
(
UserId int(4) NOT NULL AUTO_INCREMENT PRIMARY KEY,
Username varchar(25) NOT NULL,
Password varchar(15) NOT NULL,
Email varchar(50) NOT NULL,
Created timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
);
