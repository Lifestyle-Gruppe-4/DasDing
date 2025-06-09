#!/usr/bin/env python3
from data_access.room_data_access import RoomDataAccess

def user_story_9(db_path: str):
    room_dal = RoomDataAccess(db_path)

    try:
        rooms = room_dal.read_all_rooms()
        if not rooms:
            print("Keine Zimmer gefunden.")
            return

        print("\nZimmerliste mit Ausstattung:")
        for room in rooms:
            hotel_name    = room.hotel.name
            room_number   = room.room_number
            amenity_names = [f.facility_name for f in room.facilities] or []
            amenities_str = ", ".join(amenity_names) if amenity_names else "Keine Ausstattung"
            print(f"{hotel_name} – Zimmer {room_number}: {amenities_str}")
    except Exception as e:
        print(f"Fehler: {e}")

if __name__ == "__main__":
    DB_PATH = "../database/hotel_sample.db"
    user_story_9(DB_PATH)
