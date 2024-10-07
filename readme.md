# Django Appointment System

## Project Description

This is a web-based appointment scheduling system built with Django. The system allows users to book appointments with doctors, manage their profiles, and view upcoming and past appointments. It's designed for medical clinics to streamline their booking processes. Key features include user authentication, time slot availability checking, and user profile updates.

## Features

- **User Authentication**: Sign up, login, and password reset functionalities.
- **Appointments**: Users can book, edit, and cancel appointments with doctors. The system checks for available time slots before booking.
- **Profile Management**: Users can update their username, email, and password.
- **Appointment Restrictions**: Appointment editing restricts the modification of doctors and specialties after an appointment is created.

## Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML5, Bootstrap, JavaScript
- **Database**: SQLite (default).
- **Libraries/Tools**:
  - Django Forms for form handling
  - Bootstrap for styling
  - JavaScript for fetching available appointment times
  - Django Messages framework for user feedback

## Installation and Setup

### Prerequisites
- Python 3.x
- Django 4.x
- pip (Python package installer)

### Steps to Run Locally

1. **Clone the repository**:
    ```bash
    git clone https://github.com/MarinaGregorini/doctorsappointments.git
    cd doctorsappointments
    ```

2. **Create a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser (for admin access)**:
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server**:
    ```bash
    python manage.py runserver
    ```



