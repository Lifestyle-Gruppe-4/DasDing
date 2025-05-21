import model.hotel as model
from model.booking import Booking
from base_data_access import BaseDataAccess

class BookingDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def read_all_bookings(self) -> list[model.Booking]:
            sql = """
            SELECT b.booking_id, b.check_in_date, b.check_out_date, b.total_amount, g.first_name, g.last_name, r.room_number, r.price_per_night
            FROM Booking b
            JOIN Guest g ON b.guest_id = g.guest_id
            JOIN Room r ON r.room_id = r.room_id
            """
            bookings = self.fetchall(sql)

            return [model.Booking(booking_id=booking_id) for booking_id in Booking]

# Delete this methode - this will be done on the booking_manager
 #   def get_booking_by_id(self, booking_id: int):
        #sql = """
         #   SELECT b.booking_id, b.check_in_date, b.check_out_date, b.total_amount, g.first_name, g.last_name, r.room_number, r.price_per_night
          #  FROM Booking b
           # JOIN Guest g ON b.guest_id = g.guest_id
            #JOIN Room r ON b.room_id = r.room_id
            #WHERE b.booking_id = ?
           # """
        #return self.fetchone(sql, (booking_id,)) #return tuple of booking IDs

#Delete this methode - this will be done on the booking_manager
 #   def get_booking_by_guest_id(self, guest_id: int):
  #      sql = """
   #         SELECT b.booking_id, b.check_in_date, b.check_out_date, b.total_amount, r.room_number, r.price_per_night
    #        FROM Booking b
     #       JOIN ROOM r ON b.room_id = r.room_id
      #      WHERE b.guest_id = ?
       #     """
        #return self.fetchone(sql, (guest_id,)) #return tuple of guest IDs

    def create_booking(self, check_in_date: str, check_out_date: str, guest_id: int, room_id: int, total_amount: float):
        sql = """
            INSERT INTO Booking (check_in_date, check_out_date, guest_id, room_id, total_amount)
            VALUES (?, ?, ?, ?, ?)
            """
        return self.execute(sql, (check_in_date, check_out_date, guest_id, room_id, total_amount))

    def update_booking(self, booking_id: int, check_in_date: str, check_out_date: str, total_amount: float):
        sql = """
            UPDATE Booking
            SET check_in_date = ?, check_out_date = ?, total_amount = ?
            WHERE booking_id = ?
            """
        return self.execute(sql, (check_in_date, check_out_date, total_amount, booking_id))

    def delete_booking(self, booking_id: int):
        sql = """
            DELETE FROM Booking WHERE booking_id = ?
            """
        return self.execute(sql, (booking_id,)) #return tuple of booking IDs