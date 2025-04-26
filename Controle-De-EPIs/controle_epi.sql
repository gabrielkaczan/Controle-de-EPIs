CREATE DATABASE controle_epi DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE USER 'usuario_django'@'localhost' IDENTIFIED BY 'sua_senha';
GRANT ALL PRIVILEGES ON controle_epi.* TO 'usuario_django'@'localhost';
FLUSH PRIVILEGES;