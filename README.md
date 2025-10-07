# Movie Ticket Booking System

A backend system for booking movie tickets, built with **Django** and **Django REST Framework (DRF)**. The project includes user authentication, movie management, show scheduling, booking, and cancellation functionalities.

## Features

- **User Authentication**
  - Signup
  - JWT-based login and token refresh

- **Movies**
  - List all movies
  - View shows for each movie

- **Bookings**
  - Book seats for a specific show
  - Cancel bookings
  - View user's bookings

- **Database Constraints**
  - Each seat can only be booked once per show
  - Indexed for optimized querying

- **API Documentation**
  - Swagger UI and ReDoc available

---

## Tech Stack

- Python 3.x
- Django
- Django REST Framework
- djangorestframework-simplejwt (JWT Authentication)
- drf-yasg (Swagger/OpenAPI Documentation)
- SQLite (default, can be changed)

---

---

## Installation


## Project Structure
Create a virtual environment and activate it
Install dependencies
Run migrations
Create a superuser
Start the development server
