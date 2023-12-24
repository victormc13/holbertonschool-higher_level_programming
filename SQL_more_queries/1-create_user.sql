/* creates the MySQL server user user_0d_1 and grants all privileges */
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';  -- create user if not exists
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;  -- grants all privileges to the user
FLUSH PRIVILEGES;  -- update privileges

