from model.address import Address

class Guest:
    def __init__(self, guest_id:int, first_name:str, last_name:str, email:str, address:Address):
        self.guest_id = guest_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.address = address

    def make_booking(self):
        pass

    def cancel_booking(self):
        pass

    def view_booking_history(self):
        pass

    def get_booking(self):
        pass
