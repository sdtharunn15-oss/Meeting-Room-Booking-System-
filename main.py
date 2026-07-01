from fastapi import FastAPI

from database import Base, engine
from models.user import User
from models.room import Room
from models.booking import Booking
from routes import bookings

from routes import rooms, bookings
from auth import auth

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Meeting Room Booking System",
    version="0.1.0"
)

app.include_router(
    auth.router,
    tags=["Authentication"]
)

app.include_router(
    rooms.router,
    tags=["Rooms"]
)

app.include_router(
    bookings.router,
    tags=["Bookings"]
)


@app.get("/")
def root():
    return {
        "message": "Meeting Room Booking System API is running"
    }