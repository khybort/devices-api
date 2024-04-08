# GPS Devices Rest API
This API is used to manage GPS devices. GPS devices can be added, updated, deleted, and retrieved. Clean Architecture implemented with Dependency Injection in FastAPI. This app uses RabbitMQ as message broker, and PostgreSQL as database. It also uses TCP Socket for communication. Soft delete implemented as deletion pattern.

# Features
Fake GPS devices are generated using Faker.
Transfer fake data with TCP Socket.
Consume data from RabbitMQ.
Write data to PostgreSQL.

## Features of Devices API:
- Add device
- List devices
- Get device locations
- Get last locations of all devices
- Delete device

## Tech stack
- Python
- FastAPI
- TCP Socket
- RabbitMQ
- SQLAlchemy
- PostgreSQL
- Docker
- Docker Compose

## Prerequisites
- Docker
- Make
- Docker Compose


## Installation
make build-dev
make up

## Usage
http://localhost:8000

# DOCS
http://localhost:8000/docs
http://localhost:8000/redoc


