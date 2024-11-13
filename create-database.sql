CREATE DATABASE dogcollector;
CREATE USER dog_admin WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE dogcollector to dog_admin;
