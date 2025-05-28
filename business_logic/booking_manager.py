from typing import List
from datetime import datetime

from data_access.booking_data_access import BookingDataAccess
from model.booking import Booking

class BookingManager:
    def __init__(self, booking_dal: BookingDataAccess):
        self.booking_dal = booking_dal

    def get_all_bookings(self) -> List[Booking]:
        return self.booking_dal.read_all_bookings()

    def create_booking(self, check_in: datetime, check_out: datetime, guest_id: int, room_id: int, price_per_night: float) -> Booking:
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

    def update_booking(self, booking_id: int, new_check_in: datetime, new_check_out: datetime, new_total: float) -> bool:
        return self.booking_dal.update_booking(
            booking_id = booking_id,
            check_in_date = new_check_in.isoformat(),
            check_out_date = new_check_out.isoformat(),
            total_amount = new_total,
        )

    def delete_booking(self, booking_id: int) -> bool:
        return self.booking_dal.delete_booking(booking_id)

