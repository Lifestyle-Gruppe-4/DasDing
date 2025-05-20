import model.hotel as model
from base_data_access import BaseDataAccess
from model.address import Address

class HotelDataAccess(BaseDataAccess):
    def __init__(self, db_path:str=None):
        super().__init__(db_path)

    def read_all_hotels(self) -> list[model.Hotel]:
        sql = """
        SELECT h.hotel_id, h.name, h.stars, a.address_id, a.street, a.city, a.zip_code
        FROM Hotel h
        JOIN Address a ON h.address_id = a.address_id
        """
        hotels = self.fetchall(sql)

        return [
            model.Hotel(
                hotel_id=row[0],
                name=row[1],
                stars=row[2],
                address=Address(
                    address_id=row[3],
                    street=row[4],
                    city=row[5],
                    zip_code=row[6]
                )
            )
            for row in hotels
        ]

    def read_hotels_by_city(self, city: str) -> list[model.Hotel]:
        sql = """
        SELECT h.hotel_id, h.name, h.stars, a.address_id, a.street, a.city, a.zip_code
        FROM Hotel h
        JOIN Address a ON h.address_id = a.address_id
        WHERE a.city = ?
        """
        hotels = self.fetchall(sql, (city,))
        return [
            model.Hotel(
                hotel_id=row[0],
                name=row[1],
                stars=row[2],
                address=Address(
                    address_id=row[3],
                    street=row[4],
                    city=row[5],
                    zip_code=row[6]
                )
            )
            for row in hotels
        ]

    def read_hotels_by_city_and_min_stars(self, city: str, min_stars: int) -> list[model.Hotel]:
        sql = """
        SELECT h.hotel_id, h.name, h.stars, a.address_id, a.street, a.city, a.zip_code
        FROM Hotel h
        JOIN Address a ON h.address_id = a.address_id
        WHERE a.city = ? AND h.stars >= ?
        """
        hotels = self.fetchall(sql, (city, min_stars))
        return [
            model.Hotel(
                hotel_id=row[0],
                name=row[1],
                stars=row[2],
                address=Address(
                    address_id=row[3],
                    street=row[4],
                    city=row[5],
                    zip_code=row[6]
                )
            )
            for row in hotels
        ]


if __name__ == "__main__":
    db_path = "../database/hotel_sample.db"
    hotel_dal = HotelDataAccess(db_path)
    hotels = hotel_dal.read_all_hotels()

    for hotel in hotels:
        print(hotel)

