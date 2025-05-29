# Added all model import to visualize all information for booking
# Depending on the use cases for the manager, the imports will be adjusted
# IMPORTANT! - If imports are maintained then class BookingDataAccess needs to be adjusted.



from data_access.base_data_access import BaseDataAccess
from model.room import Room
from model.guest import Guest
from model.booking import Booking
from model.address import Address
from model.hotel import Hotel
from model.room_type import RoomType
from model.facility import Facility

# Wandelt SQL-Zeile in Booking-Objekte um
def _create_booking(row):
    return Booking(
        check_in_date=row[1],
        check_out_date=row[2],
        guest=Guest(
            guest_id=row[4],
            first_name=row[5],
            last_name=row[6],
            email=row[7],
            address=Address(
                address_id=row[8],
                street=row[9],
                city=row[10],
                zip_code=row[11]
            )
        ),
        room=Room(
            room_id=row[12],
            room_nr=row[13],
            price_per_night=row[14],
            hotel=Hotel(
                hotel_id=row[15],
                name=row[16],
                address=Address(
                    address_id=row[17],
                    street=row[18],
                    city=row[19],
                    zip_code=row[20]
                ),
                stars=row[21]
            ),
            room_type=RoomType(row[22], row[23], row[24]),
            facility=[]
        )
    )


class BookingDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path) # Verbindung zur DB aufbauen

    # Holt alle Buchungen aus der DB
    def read_all_bookings(self) -> list[Booking]:
        sql = """
            SELECT b.booking_id, b.check_in_date, b.check_out_date, b.total_amount,
                   g.guest_id, g.first_name, g.last_name, g.email,
                   a.address_id, a.street, a.city, a.zip_code,
                   r.room_id, r.room_number, r.price_per_night,
                   h.hotel_id, h.name, ha.address_id, ha.street, ha.city, ha.zip_code, h.stars,
                   rt.type_id, rt.description, rt.max_guests,
                   f.facility_id, f.facility_name
            FROM Booking b
            JOIN Guest g ON b.guest_id = g.guest_id
            JOIN Address a ON g.address_id = a.address_id
            JOIN Room r ON b.room_id = r.room_id
            JOIN Hotel h ON r.hotel_id = h.hotel_id
            JOIN Address ha ON h.address_id = ha.address_id
            JOIN Room_Type rt ON r.type_id = rt.type_id
            JOIN Room_Facilities rf ON r.room_id = rf.room_id
            JOIN Facilities f ON rf.facility_id = f.facility_id
        """
        results = self.fetchall(sql)
        return [_create_booking(row) for row in results]

    # Holt 1 Buchung anhand der ID
    def get_booking_by_id(self, booking_id: int) -> Booking | None:
        sql = """
            SELECT b.booking_id, b.check_in_date, b.check_out_date, b.total_amount,
                   g.guest_id, g.first_name, g.last_name, g.email,
                   a.address_id, a.street, a.city, a.zip_code,
                   r.room_id, r.room_number, r.price_per_night,
                   h.hotel_id, h.name, ha.address_id, ha.street, ha.city, ha.zip_code, h.stars,
                   rt.type_id, rt.description, rt.max_guests,
                   f.facility_id, f.facility_name
            FROM Booking b
            JOIN Guest g ON b.guest_id = g.guest_id
            JOIN Address a ON g.address_id = a.address_id
            JOIN Room r ON b.room_id = r.room_id
            JOIN Hotel h ON r.hotel_id = h.hotel_id
            JOIN Address ha ON h.address_id = ha.address_id
            JOIN Room_Type rt ON r.type_id = rt.type_id
            JOIN Room_Facilities rf ON r.room_id = rf.room_id
            JOIN Facilities f ON rf.facility_id = f.facility_id
            WHERE b.booking_id = ?
        """
        row = self.fetchone(sql, (booking_id,))
        return _create_booking(row) if row else None

    # Neue Buchungen in DB einfügen
    def create_booking(self, check_in_date: str, check_out_date: str, guest_id: int, room_id: int, total_amount: float):
        sql = """
            INSERT INTO Booking (check_in_date, check_out_date, guest_id, room_id, total_amount)
            VALUES (?, ?, ?, ?, ?)
        """
        return self.execute(sql, (check_in_date, check_out_date, guest_id, room_id, total_amount))

    # Vorhandene Buchungen aktualisieren
    def update_booking(self, booking_id: int, check_in_date: str, check_out_date: str, total_amount: float):
        sql = """
            UPDATE Booking
            SET check_in_date = ?, check_out_date = ?, total_amount = ?
            WHERE booking_id = ?
        """
        return self.execute(sql, (check_in_date, check_out_date, total_amount, booking_id))

    # Buchung löschen
    def delete_booking(self, booking_id: int):
        sql = """
            DELETE FROM Booking WHERE booking_id = ?
        """
        return self.execute(sql, (booking_id,))