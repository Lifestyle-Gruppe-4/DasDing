from datetime import datetime
from model.guest import Guest
from model.room import Room

class Booking:
    def __init__(self, booking_id:int, check_in_date:datetime, check_out_date:datetime, is_cancelled:bool, total_amount:float, guest:Guest, room:Room):
        self.booking_id = booking_id
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.is_cancelled = is_cancelled
        self.total_amount = total_amount
        self.guest = guest
        self.room = room

    def make_booking(self):
        pass

    def cancel_booking(self):
        pass

    def view_booking_history(self):
        pass

    def get_booking(self):
        pass