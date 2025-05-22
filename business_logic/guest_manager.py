from data_access.guest_data_access import GuestDataAccess
from model.guest import Guest

class GuestManager:
    def __init__(self, guest_dal: GuestDataAccess):
        self.guest_dal = guest_dal

    def get_all_guests(self) -> list[Guest]:
        return self.guest_dal.read_all_guests()

    def find_by_id(self, guest_id: int) -> Guest:
        guests = self.guest_dal.read_all_guests()
        for guest in guests:
            if guest.guest_id == guest_id:
                return guest
        return None

    def find_by_name(self, name: str) -> Guest:
        guests = self.guest_dal.read_all_guests()
        for guest in guests:
            if guest.last_name.lower() == name.lower():
                return guest
        return None

    def find_by_email(self, email: str) -> Guest:
        guests = self.guest_dal.read_all_guests()
        for guest in guests:
            if guest.email.lower() == email.lower():
                return guest
        return None

    def add_guest(self, guest: Guest) -> int:
        return self.guest_dal.create_guest(guest)

    def update_guest(self, guest: Guest) -> bool:
        return self.guest_dal.update_guest(guest)

    def delete_guest(self, guest_id:int) -> bool:
        return self.guest_dal.delete_guest(guest_id)

guest_dal = GuestDataAccess("../database/hotel_sample.db")
manager = GuestManager(guest_dal)
