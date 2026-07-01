from sqlalchemy import Column, Integer, Date, Time, ForeignKey
from database import Base


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True)
    room_id = Column(Integer, ForeignKey("rooms.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    booking_date = Column(Date)
    start_time = Column(Time)
    end_time = Column(Time)