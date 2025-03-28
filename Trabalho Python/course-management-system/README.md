# Course Management System

This is a simple web application for managing courses, including user authentication, admin-only account registration, and a check-in system for tracking attendance.

## Features

- **User Login**: Users can log in to access their accounts.
- **Admin Registration**: Only admin users can register new accounts.
- **Check-In System**: Users can check in to log their attendance with date and time.

## Project Structure

```
course-management-system
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── forms.py
│   ├── templates
│   │   ├── base.html
│   │   ├── login.html
│   │   ├── register.html
│   │   └── checkin.html
│   └── static
│       ├── css
│       │   └── styles.css
│       └── js
│           └── scripts.js
├── instance
│   └── config.py
├── requirements.txt
├── run.py
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd course-management-system
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Configuration

- Update the `instance/config.py` file with your database URI and secret key.

## Running the Application

To run the application, execute the following command:
```
python run.py
```

The application will be available at `http://127.0.0.1:5000`.

## Usage

- Navigate to the login page to access your account.
- Admin users can register new accounts via the registration page.
- Users can check in to log their attendance on the check-in page.

## License

This project is licensed under the MIT License.