from model import room
from model.facility import Facility
from model.room import Room
from model.hotel import Hotel
from model.room_type import RoomType
from data_access.base_data_access import BaseDataAccess
from model.address import Address
from model.facility import Facility

class RoomDataAccess(BaseDataAccess):
    def __init__(self, db_path:str=None):
        super().__init__(db_path)

    def read_all_rooms(self)-> list[Room]:
        sql = """
        SELECT 
            r.room_id, r.room_number, r.price_per_night,
            t.type_id, t.description, t.max_guests,
            h.hotel_id, h.name, h.stars,
            a.address_id, a.street, a.city, a.zip_code
        FROM Room r
        JOIN Hotel h ON r.hotel_id = h.hotel_id
        JOIN Address a ON h.address_id = a.address_id
        JOIN Room_Type t ON r.type_id = t.type_id;
        """

        rooms = self.fetchall(sql)

        return [
            Room(
                room_id=row[0],
                room_number=row[1],
                price_per_night=row[2],
                room_type=RoomType(
                    room_type_id=row[3],
                    description=row[4],
                    max_guests=row[5]
                ),
                hotel=Hotel(
                    hotel_id=row[6],
                    name=row[7],
                    stars=row[8],
                    address=Address(
                        address_id=row[9],
                        street=row[10],
                        city=row[11],
                        zip_code=row[12]
                    )
                ),
                facilities=self.read_facilities_for_room(row[0])
            )

            for row in rooms
        ]

    def read_facilities_for_room(self, room_id: int) -> list[Facility]:
        sql = """
        SELECT f.facility_id, f.facility_name
        FROM Room_Facilities rf
        JOIN Facilities f ON rf.facility_id = f.facility_id
        WHERE rf.room_id = ?
        """
        rows = self.fetchall(sql, (room_id,))
        return [Facility(facility_id=row[0], facility_name=row[1]) for row in rows]

if __name__ == "__main__":
   db_path = "../database/hotel_sample.db"
   room_dal = RoomDataAccess(db_path)
   rooms = room_dal.read_all_rooms()

   for room in rooms:
       print(room)