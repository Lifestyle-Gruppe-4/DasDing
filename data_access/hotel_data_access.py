from data_access.room_data_access import RoomDataAccess
from model.hotel import Hotel
from data_access.base_data_access import BaseDataAccess
from model.address import Address



class HotelDataAccess(BaseDataAccess):
    def __init__(self, db_path:str=None, room_dal: RoomDataAccess = None):
        super().__init__(db_path)
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
        hotel_id, _ = self.execute(sql, params)
        return hotel_id

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


# if __name__ == "__main__":
#    db_path = "../database/hotel_sample.db"
#    room_dal = RoomDataAccess(db_path)
#    hotel_dal = HotelDataAccess(db_path, room_dal)
#    hotels = hotel_dal.read_all_hotels()
#
#    for hotel in hotels:
#        print(hotel)

