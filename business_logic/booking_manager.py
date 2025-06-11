
from datetime import datetime, date
from model.booking import Booking
from model.invoice import Invoice
from data_access.booking_data_access import BookingDataAccess
from business_logic.room_manager import RoomManager
from business_logic.hotel_manager import HotelManager


class BookingManager:
    def __init__(self, booking_dal: BookingDataAccess):
        self.booking_dal = booking_dal # Zufriff auf DB-Schicht

    # Gibt alle Buchunge zurück
    def get_all_bookings(self) -> list[Booking]:
        return self.booking_dal.read_all_bookings()

    # Neue Buchungen erstellen (Logik inkl. Preisberechnung)
    def create_booking(self, check_in: datetime.date, check_out: datetime.date, guest_id: int, room_id: int, price_per_night: float) -> int:
        if check_out <= check_in:
            raise ValueError("Check-out must be the same or after check-in date!")

        nights = (check_out - check_in).days
        total_price = price_per_night * nights

        return self.booking_dal.create_booking(
            check_in_date = check_in.isoformat(),
            check_out_date = check_out.isoformat(),
            guest_id = guest_id,
            room_id = room_id,
            total_amount = total_price,
        )

    # Buchung aktualisieren (z.B. neue Daten)
    def update_booking(self, booking_id: int, new_check_in: date, new_check_out: date, new_total: float) -> bool:
        return self.booking_dal.update_booking(
            booking_id = booking_id,
            check_in_date = new_check_in.isoformat(),
            check_out_date = new_check_out.isoformat(),
            total_amount = new_total
        )

    # Buchung löschen
    def delete_booking(self, booking_id: int) -> bool:
        return self.booking_dal.delete_booking(booking_id)

    # Gibt Buchungsinfo als String zurück
    @staticmethod
    def get_booking_details(booking: Booking) -> str:
        booking_status = "Cancelled" if booking.is_cancelled else "Active"
        return (f"Booking ID: {booking.booking_id},  Guest: {booking.guest.first_name} {booking.guest.last_name} "
                f"Room: {booking.room.room_number}, From: {booking.check_in_date}, to: {booking.check_out_date} "
                f"Total: {booking.total_amount:.2f} CHF, Status: {booking_status}")

    # Berechnet Preis: Anzahl Nächte x Zimmerpreis
    @staticmethod
    def calculate_total_amount(booking: Booking) -> float:
        nights = (booking.check_out_date - booking.check_in_date).days
        if nights <= 0:
            raise ValueError("Booking must be at least 1 night.")
        return nights * booking.room.price_per_night

    # Methoden für Buchungslogik
    @staticmethod
    def cancel_booking(booking: Booking):
        booking.is_cancelled = True
        print(f"Booking ID: {booking.booking_id} has been cancelled.")

    def update_dates(self, booking: Booking, new_check_in: datetime.date, new_check_out: datetime.date):
        if new_check_out < new_check_in:
            raise ValueError("Check-out must be the same or after check-in date!")
        booking.check_in_date = new_check_in
        booking.check_out_date = new_check_out
        booking.__total_amount = self.calculate_total_amount(booking)

    @staticmethod
    def generate_invoice(booking: Booking) -> Invoice:
        if not booking.invoice:
            booking.invoice = Invoice(booking.total_amount, booking)
        return booking.invoice

    @staticmethod
    def is_future_booking(booking: Booking) -> bool:
        return booking.check_in_date > date.today()

    @staticmethod
    def is_active_booking(booking: Booking) -> bool:
        return booking.check_in_date <= date.today() <= booking.check_out_date and not booking.is_cancelled

    @staticmethod
    def stay_duration(booking: Booking) -> int:
        return (booking.check_out_date - booking.check_in_date).days

    def print_confirmation(self, booking: Booking):
        status = "Cancelled" if booking.is_cancelled else "Active"
        print("------Booking Confirmation------")
        print(f"Booking ID: {booking.booking_id},  Guest: {booking.guest.first_name} {booking.guest.last_name}")
        print(f"Room: {booking.room.room_number}, From: {booking.check_in_date}, To: {booking.check_out_date}")
        print(f"Duration: {self.stay_duration(booking)} Nights")
        print(f"Total: {booking.total_amount:.2f} CHF")
        print(f"Status: {status}")
        print("--------------------------------")


    def get_bookings_by_guest(self,first_name:str,last_name:str) -> list[Booking]:
        all_bookings = self.booking_dal.read_all_bookings()
        return [
            b for b in all_bookings
            if b.guest.first_name.lower() == first_name.lower()
            and b.guest.last_name.lower() == last_name.lower()
        ]
