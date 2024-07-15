-- settings.sql
CREATE DATABASE tickit;
CREATE USER tickituser WITH PASSWORD 'tickit';
GRANT ALL PRIVILEGES ON DATABASE tickit TO tickituser;
ALTER DATABASE tickit OWNER TO tickituser;