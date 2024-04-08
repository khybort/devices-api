#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE TABLE IF NOT EXISTS gps_devices (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) UNIQUE NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        is_deleted BOOLEAN DEFAULT FALSE);
    CREATE TABLE IF NOT EXISTS locations (
        id SERIAL PRIMARY KEY,
        longitude FLOAT NOT NULL,
        latitude FLOAT NOT NULL,
        device_id INTEGER NOT NULL REFERENCES gps_devices(id),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        is_deleted BOOLEAN DEFAULT FALSE
    );
    INSERT INTO gps_devices (name)
        VALUES ('test')
        ON CONFLICT (name) DO UPDATE SET updated_at = CURRENT_TIMESTAMP;

EOSQL



