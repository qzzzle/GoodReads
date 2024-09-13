# GoodReads API Clone

This project is a simplified version of the GoodReads website, implemented using Django and Django REST Framework (DRF). It provides a backend API where users can register, log in, rate books, write reviews, and bookmark books. The project is structured to be easily extendable and maintainable, following best practices and clean code principles.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **User Authentication**: Register and log in using an email and password.
- **Book Management**: Admin users can manage books (add, edit, delete) via the Django admin panel.
- **Rating and Reviews**: Logged-in users can rate books (1 to 5 stars) and write reviews.
- **Bookmarks**: Users can bookmark books they want to read later.
- **API Documentation**: Provides clear and concise API endpoints for interacting with the system.

## Installation

### Prerequisites

- Python 3.8+
- Django 3.2+
- Django REST Framework
- SQLite3 (default) or another database (e.g., PostgreSQL)

### Setup Instructions

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/qzzzle/goodreads-clone.git
    cd goodreads-clone
    ```

2. **Create a Virtual Environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Make and Run Migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a Superuser:**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the Development Server:**

    ```bash
    python manage.py runserver
    ```

7. **Access the Admin Panel:**

    - Go to `http://127.0.0.1:8000/admin` and log in with your superuser credentials.

## Usage

### Register a New User

- Endpoint: `POST /account/auth/`
- Payload:
    ```json
    {
        "email": "newuser@example.com",
        "password": "newpassword123"
    }
    ```

### Log In as an Existing User

- Endpoint: `POST /account/auth/`
- Payload:
    ```json
    {
        "email": "existinguser@example.com",
        "password": "existingpassword123"
    }
    ```

### Get List of Books

- Endpoint: `GET /books/`

### Get Book Details

- Endpoint: `GET /books/<book_id>/`

### Bookmark a Book

- Endpoint: `POST /books/<book_id>/bookmark/`

### Submit a Review

- Endpoint: `POST /books/<book_id>/review/`
- Payload:
    ```json
    {
        "rating": 5,
        "comment": "This book is fantastic!"
    }
    ```

## API Endpoints

| Method | Endpoint                          | Description                      |
|--------|-----------------------------------|----------------------------------|
| POST   | `/account/auth/`                  | Register or log in a user        |
| GET    | `/books/`                         | Get a list of all books          |
| GET    | `/books/<book_id>/`               | Get detailed information on a book |
| POST   | `/books/<book_id>/bookmark/`      | Bookmark or unbookmark a book    |
| POST   | `/books/<book_id>/review/`        | Submit a rating and/or review    |

