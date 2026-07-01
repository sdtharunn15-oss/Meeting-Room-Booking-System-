from pydantic import BaseModel


class RoomCreate(BaseModel):
    room_name: str
    capacity: int
    floor: int
    amenities: str