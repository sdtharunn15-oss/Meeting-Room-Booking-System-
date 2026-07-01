from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models.room import Room
from schemas.room import RoomCreate
from auth.dependencies import get_current_user
router = APIRouter(
    prefix="/rooms",
    tags=["Rooms"]
)


# Create Room
@router.post("")
def create_room(
    room: RoomCreate,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    if user["role"] != "Admin":
        raise HTTPException(
            status_code=403,
            detail="Only Admin can create rooms"
        )

    data = Room(**room.dict())

    db.add(data)
    db.commit()
    db.refresh(data)

    return data
# Get All Rooms
@router.get("/")
def get_rooms(
    db: Session = Depends(get_db)
):

    return db.query(Room).all()


# Get Room By ID
# Get Room By ID
@router.get("/{room_id}")
def get_room(
    room_id: int,
    db: Session = Depends(get_db)
):
    room = db.query(Room).filter(
        Room.id == room_id
    ).first()

    if not room:
        raise HTTPException(
            status_code=404,
            detail="Room not found"
        )

    return room

@router.put("/{room_id}")
def update_room(
    room_id: int,
    room: RoomCreate,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    if user["role"] != "Admin":
        raise HTTPException(
            status_code=403,
            detail="Only Admin can update rooms"
        )

    data = db.query(Room).filter(Room.id == room_id).first()

    if not data:
        raise HTTPException(404, "Room not found")

    data.name = room.name
    data.capacity = room.capacity

    db.commit()
    db.refresh(data)

    return data
# Delete Room
@router.delete("/{room_id}")
def delete_room(
    room_id: int,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    if user["role"] != "Admin":
        raise HTTPException(
            status_code=403,
            detail="Only Admin can delete rooms"
        )

    data = db.query(Room).filter(Room.id == room_id).first()

    if not data:
        raise HTTPException(404, "Room not found")

    db.delete(data)
    db.commit()

    return {"message": "Room deleted successfully"}