Meeting Room Booking System

A backend API application built using **FastAPI** that allows users to register, authenticate using JWT, manage meeting rooms, and book rooms with proper validation and conflict checking.



Features

- User Registration
- User Login with JWT Authentication
- Secure Password Hashing using bcrypt
- Role-based user management
- Create Meeting Rooms
- View Meeting Rooms
- Create Room Bookings
- View Bookings
- Prevent Double Booking / Time Conflicts
- Protected APIs using JWT Token
- SQLAlchemy Database Integration
- Pytest Unit Testing
- Swagger API Documentation


Tech Stack

- **Backend:** FastAPI
- **Language:** Python
- **Database:** SQLite
- **ORM:** SQLAlchemy
- **Authentication:** JWT
- **Password Security:** Passlib + bcrypt
- **Validation:** Pydantic
- **Testing:** Pytest



Project Structure


meeting_room_booking_system/

│
├── auth/
│   └── auth.py
│
├── models/
│   ├── user.py
│   ├── room.py
│   └── booking.py
│
├── schemas/
│   ├── user.py
│   ├── room.py
│   └── booking.py
│
├── routes/
│   ├── rooms.py
│   └── bookings.py
│
├── tests/
│   ├── conftest.py
│   ├── test_auth.py
│   ├── test_rooms.py
│   └── test_bookings.py
│
├── database.py
├── main.py
├── requirements.txt
└── README.md





Installation & Setup

1. Clone Repository

bash
git clone <repository-url>


Move into project folder:

bash
cd meeting_room_booking_system


2. Create Virtual Environment

bash
python -m venv venv

Activate virtual environment:

Windows

bash
venv\Scripts\activate


3. Install Dependencies

bash
pip install -r requirements.txt


Run Application

Start FastAPI server:

bash
uvicorn main:app --reload

Application will run at:

http://127.0.0.1:8000


API Documentation

Swagger UI:
http://127.0.0.1:8000/docs


Authentication APIs

Register User

POST
/auth/register

Request Body

json
{
  "username": "testuser",
  "password": "12345",
  "role": "Admin"
}

Response

json
{
  "message": "User registered successfully"
}



Login User

POST


/auth/login

Request Body

json
{
  "username": "testuser",
  "password": "12345"
}

Response

json
{
  "message": "Login successful",
  "access_token": "jwt_token",
  "token_type": "bearer"
}

Room APIs

Create Room

POST


/rooms/


Authorization required.

Example:

json
{
  "name": "Conference Room",
  "capacity": 10
}

Get Rooms

GET

/rooms/

Returns available meeting rooms.


Booking APIs

Create Booking

POST
/bookings/

Authorization required.

Request:

json
{
  "room_id": 1,
  "booking_date": "2026-07-01",
  "start_time": "10:00:00",
  "end_time": "11:00:00"
}

Get Bookings

GET
/bookings/

Returns all bookings.


JWT Authentication

Protected APIs require JWT token.

Add the following header:


Authorization: Bearer <your_token>


Testing

Run test cases:

bash
pytest

Expected output:


6 passed



Database

This project uses SQLite database.

Tables:

- Users
- Rooms
- Bookings


User Table

Stores:

- Username
- Hashed Password
- Role


Room Table

Stores:

- Room Name
- Capacity


Booking Table

Stores:

- User ID
- Room ID
- Booking Date
- Start Time
- End Time

Validation

The system handles:

- Duplicate username prevention
- Invalid login credentials
- Unauthorized access
- Room availability checking
- Booking time conflicts


Future Enhancements

- Email booking confirmation
- Admin dashboard
- Calendar integration
- PostgreSQL support
- Docker deployment
- Cloud hosting


Author

Tharun

---

## Project Status

✅ Completed  
✅ Tested  
✅ Ready for Submission
