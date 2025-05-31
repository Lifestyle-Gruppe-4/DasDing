from typing import List
from datetime import datetime
from model.booking import Booking

from data_access.booking_data_access import BookingDataAccess

class BookingManager:
    def __init__(self, booking_dal: BookingDataAccess):
        self.booking_dal = booking_dal # Zufriff auf DB-Schicht

    # Gibt alle Buchunge zurück
    def get_all_bookings(self) -> List["Booking"]:
        from model.booking import Booking
        return self.booking_dal.read_all_bookings()

    # Neue Buchungen erstellen (Logik inkl. Preisberechnung)
    def create_booking(self, check_in: datetime, check_out: datetime, guest_id: int, room_id: int, price_per_night: float) -> "Booking":
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
    def update_booking(self, booking_id: int, new_check_in: datetime, new_check_out: datetime, new_total: float) -> bool:
        return self.booking_dal.update_booking(
            booking_id = booking_id,
            check_in_date = new_check_in.isoformat(),
            check_out_date = new_check_out.isoformat(),
            total_amount = new_total,
        )

    # Buchung löschen
    def delete_booking(self, booking_id: int) -> bool:
        return self.booking_dal.delete_booking(booking_id)

    # Gibt Buchungsinfo als String zurück
    def get_booking_details(self) -> str:
        booking_status = "Cancelled" if self.is_cancelled else "Active"
        return (f"Booking ID: {self.booking_id},  Guest: {self.guest.first_name} {self.guest.last_name} "
                f"Room: {self.room.room_nr}, From: {self.check_in_date}, to: {self.check_out_date} "
                f"Total: {self.total_amount} CHF, Status: {booking_status}")

    # Berechnet Preis: Anzahl Nächte x Zimmerpreis
    def calculate_total_amount(self, booking: Booking) -> float:
        nights = (booking.check_out_date - booking.check_in_date).days
        if nights <= 0:
            raise ValueError("Booking must be at least 1 night.")
        if not booking.room:
            raise ValueError("Booking has no room assigned.")
        return nights * booking.room.price_per_night

    # Methoden für Buchungslogik
    def cancel_booking(self):
        self.is_cancelled = True
        print(f"Booking ID: {self.booking_id} has been cancelled.")

    def update_dates(self, new_check_in: datetime, new_check_out: datetime):
        if new_check_out < new_check_in:
            raise ValueError("Check-out must be the same or after check-in date!")
        self.check_in_date = new_check_in
        self.check_out_date = new_check_out
        self.__total_amount = self.calculate_total_amount()

    def generate_invoice(self):
        if not self.invoice:
            from model.invoice import Invoice # Lokale Import in der Methode
            self.invoice = Invoice(self.total_amount, self)
        return self.invoice

    def is_future_booking(self) -> bool:
        return self.check_in_date > datetime.now()

    def is_active_booking(self) -> bool:
        return self.check_in_date <= datetime.now() <= self.check_out_date and not self.is_cancelled

    def stay_duration(self) -> int:
        return (self.check_out_date - self.check_in_date).days

    def print_confirmation(self):
        print("------Booking Confirmation------")
        print(self.get_booking_details())
        print(f"Duration: {self.stay_duration()} Nights")
        print(f"Total: {self.total_amount} CHF")
        print("--------------------------------")