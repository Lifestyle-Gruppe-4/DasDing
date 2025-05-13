from data_access.v2_base_data_access import BaseDataAccess

class HotelDataAccess(BaseDataAccess):
    def get_all_hotels(self) -> list:
        sql = "SELECT hotel_id, name FROM Hotel"
        return self.fetchall(sql)

    def get_hotel_by_id(self, hotel_id: int) -> list:
        sql = "SELECT hotel_id, name FROM Hotel WHERE hotel_id = ?"
        return self.fetchall(sql, [hotel_id])

dao = HotelDataAccess()
hotel_by_id = dao.get_hotel_by_id(3)
print(hotel_by_id)


hotel_dao = HotelDataAccess()
hotels = hotel_dao.get_all_hotels()
for hotel in hotels:
    print(hotel)