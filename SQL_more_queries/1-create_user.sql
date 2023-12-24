-- Creates the MySQL server user user_0d_1 and grants all privileges
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd'; 
GRANT ALL ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
