-- Prepares MySQL Database and ×××-User for the Project

CREATE DATABASE IF NOT EXISTS careerLink_DB_test;
CREATE USER IF NOT EXISTS 'admin_test'@'localhost' IDENTIFIED BY 'careerLink_password_test';
GRANT ALL PRIVILEGES ON `careerLink_DB_test`.* TO 'admin_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'admin_test'@'localhost';
FLUSH PRIVILEGES;
