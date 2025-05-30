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

    def read_rooms_for_hotel(self, hotel_id: int) -> list[Room]:
        sql = """
        SELECT 
            r.room_id, r.room_number, r.price_per_night,
            t.type_id, t.description, t.max_guests
        FROM Room r
        JOIN Room_Type t ON r.type_id = t.type_id
        WHERE r.hotel_id = ?
        """
        rows = self.fetchall(sql, (hotel_id,))
        return [
            Room(
                room_id=row[0],
                room_number=row[1],
                price_per_night=row[2],
                hotel=None,  # wird vom aufrufenden Hotel gesetzt
                room_type=RoomType(room_type_id=row[3], description=row[4], max_guests=row[5]),
                facilities=self.read_facilities_for_room(row[0])
            )
            for row in rows
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

    def create_room(self, room: Room) -> int:
        sql = """
        INSERT INTO Room (hotel_id, room_number, type_id, price_per_night)
        VALUES (?,?,?,?)
        """

        params = (room.hotel_id, room.room_number,room.room_type.room_type_id, room.price_per_night)
        room_id, _ = self.fetchone(sql, params)
        return room_id

    def read_all_rooms_with_facilities(self) -> list[Room]:
        sql = """
              SELECT r.room_id,
                     r.room_number,
                     f.facility_id,
                     f.name
              FROM Room r
                       LEFT JOIN RoomFacility rf ON r.room_id = rf.room_id
                       LEFT JOIN Facility f ON rf.facility_id = f.facility_id \
              """
        rows = self.fetchall(sql)
        rooms: dict[int, Room] = {}
        for room_id, room_number, fac_id, fac_name in rows:
            if room_id not in rooms:
                rooms[room_id] = Room(room_id=room_id,
                                      room_number=room_number,
                                      facilities=[])
            if fac_id is not None:
                rooms[room_id].facilities.append(
                    Facility(facility_id=fac_id, name=fac_name)
                )
        return list(rooms.values())

if __name__ == "__main__":
   db_path = "../database/hotel_sample.db"
   room_dal = RoomDataAccess(db_path)
   rooms = room_dal.read_all_rooms()

   for room in rooms:
       print(room)

