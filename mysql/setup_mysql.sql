-- Prepares MySQL Database and ×××-User for the Project

CREATE DATABASE IF NOT EXISTS careerLink_DB;
CREATE USER IF NOT EXISTS 'admin'@'localhost' IDENTIFIED BY 'careerLink_password';
GRANT ALL PRIVILEGES ON `careerLink_DB`.* TO 'admin'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'admin'@'localhost';
FLUSH PRIVILEGES;
