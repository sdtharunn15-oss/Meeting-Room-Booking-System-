from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.room import Room
from database import get_db
from models.booking import Booking
from models.room import Room
from schemas.booking import BookingCreate
from auth.dependencies import get_current_user
router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"]
)


@router.post("/")
def create_booking(
    booking: BookingCreate,
   db: Session = Depends(get_db),
user=Depends(get_current_user)
):
    room = db.query(Room).filter(Room.id == booking.room_id).first()

    if not room:
        raise HTTPException(
            status_code=404,
            detail="Room not found"
        )

    conflict = db.query(Booking).filter(
        Booking.room_id == booking.room_id,
        Booking.booking_date == booking.booking_date,
        Booking.start_time < booking.end_time,
        Booking.end_time > booking.start_time
    ).first()

    if conflict:
        raise HTTPException(
            status_code=400,
            detail="Room already booked for this time"
        )

    data = Booking(
    room_id=booking.room_id,
    booking_date=booking.booking_date,
    start_time=booking.start_time,
    end_time=booking.end_time,
    user_id=user["id"]
)

    db.add(data)
    db.commit()
    db.refresh(data)

    return data


@router.get("/")
def get_bookings(db: Session = Depends(get_db)):
    return db.query(Booking).all()


@router.get("")
def get_bookings(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):

    if user["role"] == "Admin":
        return db.query(Booking).all()

    return db.query(Booking).filter(
        Booking.user_id == user["id"]
    ).all()


@router.put("/{booking_id}")
def update_booking(
    booking_id: int,
    booking: BookingCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    data = db.query(Booking).filter(
        Booking.id == booking_id
    ).first()

    if not data:
        raise HTTPException(
            status_code=404,
            detail="Booking not found"
        )

    if user["role"] != "Admin" and data.user_id != user["id"]:
        raise HTTPException(
            status_code=403,
            detail="Not allowed"
        )

    conflict = db.query(Booking).filter(
        Booking.room_id == booking.room_id,
        Booking.booking_date == booking.booking_date,
        Booking.start_time < booking.end_time,
        Booking.end_time > booking.start_time,
        Booking.id != booking_id
    ).first()

    if conflict:
        raise HTTPException(
            status_code=400,
            detail="Room already booked for this time slot"
        )

    data.room_id = booking.room_id
    data.booking_date = booking.booking_date
    data.start_time = booking.start_time
    data.end_time = booking.end_time

    db.commit()
    db.refresh(data)

    return data

@router.delete("/{booking_id}")
def delete_booking(
    booking_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    booking = db.query(Booking).filter(
        Booking.id == booking_id
    ).first()

    if not booking:
        raise HTTPException(
            status_code=404,
            detail="Booking not found"
        )

    if user["role"] != "Admin" and booking.user_id != user["id"]:
        raise HTTPException(
            status_code=403,
            detail="Not allowed"
        )

    db.delete(booking)
    db.commit()

    return {
        "message": "Booking deleted successfully"
    }


@router.get("/my-bookings")
def my_bookings(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return db.query(Booking).filter(
        Booking.user_id == user["id"]
    ).all()