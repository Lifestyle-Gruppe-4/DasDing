from datetime import datetime
from model.guest import Guest
from model.room import Room
from model.invoice import Invoice

class Booking:
    booking_counter = 1

    def __init__(self, check_in_date: datetime, check_out_date: datetime, guest: Guest, room: Room):
        self.booking_id = Booking.booking_counter
        Booking.booking_counter += 1

        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.guest = guest
        self.room = room
        self.is_cancelled = False
        self.total_amount = self.calculate_total_amount()
        self.invoice = None

    def get_booking_details(self) -> str:
        booking_status = "Cancelled" if self.is_cancelled else "Active"
        return (f"Booking ID: {self.booking_id},  Guest: {self.guest.first_name} {self.guest.last_name} "
                f"Room: {self.room.room_nr}, From: {self.check_in_date}, to: {self.check_out_date} "
                f"Total: {self.total_amount} CHF, Status: {booking_status}")

    def update_dates(self, new_check_in: datetime, new_check_out: datetime):
        if new_check_out < new_check_in:
            raise ValueError("Check-out must be the same or after check-in date!")
        self.check_in_date = new_check_in
        self.check_out_date = new_check_out
        self.total_amount = self.calculate_total_amount()

    def calculate_total_amount(self) -> float:
        nights = (self.check_out_date - self.check_in_date).days
        if nights <= 0:
            raise ValueError("Booking must be at least 1 night.")
        return nights * self.room.price_per_night

    def cancel_booking(self):
        self.is_cancelled = True
        print(f"Booking ID: {self.booking_id} has been cancelled.")

    def generate_invoice(self):
        if not self.invoice:
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
