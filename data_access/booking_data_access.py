# Added all model import to visualize all information for booking
# Depending on the use cases for the manager, the imports will be adjusted
# IMPORTANT! - If imports are maintained then class BookingDataAccess needs to be adjusted.



from data_access.base_data_access import BaseDataAccess
from model.room import Room
from model.guest import Guest
from model.address import Address
from model.hotel import Hotel
from model.room_type import RoomType
from model.facility import Facility
from model.booking import Booking

# Wandelt SQL-Zeile in Booking-Objekte um
def _create_booking(rows):
    from model.booking import Booking  # Lokaler Import vermeidet circular import

    base = rows[0]
    facilities = [Facility(row[25], row[26]) for row in rows]

    return Booking(
        check_in_date=base[1],
        check_out_date=base[2],
        guest=Guest(
            guest_id=base[4],
            first_name=base[5],
            last_name=base[6],
            email=base[7],
            address=Address(
                address_id=base[8],
                street=base[9],
                city=base[10],
                zip_code=base[11]
            )
        ),
        room=Room(
            room_id=base[12],
            room_number=base[13],
            price_per_night=base[14],
            hotel=Hotel(
                hotel_id=base[15],
                name=base[16],
                address=Address(
                    address_id=base[17],
                    street=base[18],
                    city=base[19],
                    zip_code=base[20]
                ),
                stars=base[21]
            ),
            room_type=RoomType(base[22], base[23], base[24]),
            facilities=facilities
        )
    )

class BookingDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path) # Verbindung zur DB aufbauen

    # Holt alle Buchungen aus der DB
    def read_all_bookings(self) -> list["Booking"]:
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
    def get_booking_by_id(self, booking_id: int) -> "Booking | None":
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