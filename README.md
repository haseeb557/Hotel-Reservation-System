# PostgreSQL Hotel Reservation System

This repository contains the PostgreSQL database schema, Python backend code, and Flask frontend application for a hotel reservation system. The system allows users to register, make reservations for different types of rooms, and manage reservation details through a web interface.

## Table of Contents

- [Database Schema](#database-schema)
- [Backend Code](#backend-code)
- [Frontend Code](#frontend-code)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)


## Database Schema

The database consists of the following tables:

- **User1**: Stores user information including email, name, password, and last login timestamp.
- **Reservation**: Manages reservation details such as reservation ID, reserved by (user email), room type, reservation date, and checkout date. It has a foreign key constraint referencing the email column in the User1 table.
- **Delux**, **Premium**, **Suite**: These tables represent different types of rooms available for reservation. Each table stores information about the reservation ID, price, availability status, and maximum number of people allowed.

## Backend Code

The backend code, written in Python, includes functionality for user registration and reservation management. It uses the psycopg2 library to interact with the PostgreSQL database. The `User1` and `add_reservation` functions handle the insertion of user and reservation data into the database, respectively.

## Frontend Code

The frontend code is implemented using the Flask web framework, providing a user-friendly interface for interacting with the reservation system. The Flask application includes routes for adding users (`/add_user`) and making reservations (`/add_reservation`), as well as a homepage (`/`) to render the main interface.

## Setup Instructions

To set up the PostgreSQL database, backend, and frontend application:

1. Ensure PostgreSQL is installed on your system.
2. Create the necessary tables and functions by executing the provided SQL scripts (`database.sql`) in your PostgreSQL database.
3. Update the database connection parameters in the Python code (`database.ini`) to match your PostgreSQL configuration.
4. Run the Flask application (`app.py`) to start the backend server.
5. Access the web interface in your browser at `http://localhost:5000`.

## Usage

Once the backend server and frontend application are running, users can navigate to the web interface to register and make reservations using the provided forms.




