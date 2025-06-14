from data_access.room_type_data_access import RoomTypeDataAccess
from data_access.facility_data_access import FacilityDataAccess
from data_access.room_data_access import RoomDataAccess
from model.hotel import Hotel
from data_access.base_data_access import BaseDataAccess
from model.address import Address
from model.room import Room



class HotelDataAccess(BaseDataAccess):
    def __init__(self, db_path:str=None, room_dal: RoomDataAccess = None):
        super().__init__(db_path)
        self.db_path = db_path
        self.room_dal = room_dal

    def read_all_hotels(self) -> list[Hotel]:
        sql = """
        SELECT h.hotel_id, h.name, h.stars, a.address_id, a.street, a.city, a.zip_code
        FROM Hotel h
        JOIN Address a ON h.address_id = a.address_id
        """
        hotels = self.fetchall(sql)

        return [
            Hotel(
                hotel_id=row[0],
                name=row[1],
                stars=row[2],
                address=Address(
                    address_id=row[3],
                    street=row[4],
                    city=row[5],
                    zip_code=row[6]
                ),
                rooms=self.room_dal.read_rooms_for_hotel(row[0])
            )
            for row in hotels
        ]

    def create_hotel(self, hotel: Hotel) -> int:
        sql = """
        INSERT INTO Hotel(name, stars, address_id)
            VALUES (?, ?, ?)
        """

        params = (hotel.name, hotel.stars, hotel.address.address_id,)
        lastrowid, _ = self.execute(sql, params)
        return lastrowid

    def delete_hotel(self, hotel_id: int) -> bool:
        sql = """
        DELETE FROM Hotel WHERE hotel_id = ?
        """
        params = (hotel_id,)
        _, rows_affected = self.execute(sql, params)
        return rows_affected > 0

    def update_hotel(self, hotel: Hotel) -> bool:
        sql = """
        UPDATE Hotel 
        SET name = ?, stars = ?, address_id = ?
        WHERE hotel_id = ?
        """
        params = (
            hotel.name,
            hotel.stars,
            hotel.address.address_id,
            hotel.hotel_id,
        )
        _, rows_affected = self.execute(sql, params)
        return rows_affected > 0

    def create_room_for_hotel(self,hotel_id:int,room_number:str,type_id:int, price_per_night:float) -> int:
        sql = """
              INSERT INTO Room (hotel_id, room_number, type_id, price_per_night)
              VALUES (?, ?, ?, ?)
              """
        params = (hotel_id,room_number,type_id,price_per_night)
        lastrowid, _ = self.execute(sql, params)
        return lastrowid

    def read_room_by_id(self, room_id: int) -> Room:
        sql = """
        SELECT room_id, room_number, type_id, price_per_night
        FROM Room 
        WHERE room_id = ?
        """

        rows = self.fetchall(sql, (room_id,))
        if not rows:
            return None

        row = rows[0]

        room_type_dal = RoomTypeDataAccess(self.db_path)
        room_type = room_type_dal.read_room_type_by_id(row[2])

        fac_dal = FacilityDataAccess(self.db_path)
        facilities = fac_dal.read_facilities_by_room_id(row[0])

        return Room(
            room_id=row[0],
            room_number=row[1],
            price_per_night=row[3],
            hotel=None,
            room_type=room_type,
            facilities=facilities,
        )


