-- Prepares MySQL Database and ×××-User for the Project

CREATE DATABASE IF NOT EXISTS careerLink_DB;
CREATE USER IF NOT EXISTS 'admin'@'localhost' IDENTIFIED BY 'careerLink_password';
GRANT ALL PRIVILEGES ON `careerLink_DB`.* TO 'admin'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'admin'@'localhost';
FLUSH PRIVILEGES;

-- CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
-- GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
-- FLUSH PRIVILEGES;
