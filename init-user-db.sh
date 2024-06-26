#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER $DB_USER;
    ALTER USER $DB_USER WITH ENCRYPTED PASSWORD '$DB_PASS';
    GRANT ALL PRIVILEGES ON DATABASE $POSTGRES_DB TO $DB_USER;
    CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
    SET TIME ZONE 'UTC';
EOSQL