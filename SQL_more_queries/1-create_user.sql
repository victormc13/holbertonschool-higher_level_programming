/* creates the MySQL server user user_0d_1 and grants all privileges */
-- create user if not exists
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';  
-- grants all privileges to the user
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;  
-- update privileges
FLUSH PRIVILEGES;  

