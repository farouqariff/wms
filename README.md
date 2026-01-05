# Warehouse Management System (WMS)

A full-stack warehouse management system with role-based access control.

## Tech Stack

### Backend

- Django
- Django REST Framework
- SQLite Database

### Frontend

- React
- Tailwind CSS

## Features

- Role-based authentication (Admin, Manager, Operator)
- Secure user management
- Modern responsive UI

## Project Structure

```
wms/
├── client/          # React frontend
├── server/          # Django backend
└── README.md
```

## Getting Started

### Backend Setup

1. Navigate to the server directory:

   ```bash
   cd server
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run migrations:

   ```bash
   python manage.py migrate
   ```

4. Setup initial users:

   ```bash
   python manage.py setup_users
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

### Frontend Setup

1. Navigate to the client directory:

   ```bash
   cd client
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```

## License

This project is open source and available under the MIT License.
