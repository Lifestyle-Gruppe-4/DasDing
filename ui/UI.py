from business_logic.guest_manager import GuestManager
from business_logic.address_manager import AddressManager
from data_access.address_data_access import AddressDataAccess
from data_access.guest_data_access import GuestDataAccess
from model.address import Address
from model.guest import Guest

db_path = "../database/hotel_sample.db"
guest_dal = GuestDataAccess(db_path)
address_dal = AddressDataAccess(db_path)

guest_manager = GuestManager(guest_dal)
address_manager = AddressManager(address_dal)

# first_name = input("Enter First Name: ")
# last_name = input("Enter Last Name: ")
# email = input("Enter Email: ")
#
# address = address_manager.find_address_by_id(1)
#
# if address is None:
#     print("Address Not Found")
# else:
#     new_guest = Guest(guest_id=None, first_name=first_name, last_name=last_name, email=email, address=address)
#
# guest_id = guest_manager.add_guest(new_guest)
# print(f"Gast gespeichert mit ID: {guest_id}")

# delete_id = input("Enter ID to delete")
#
# delete_guest = guest_manager.delete_guest(delete_id)

for guest in guest_manager.get_all_guests():
    print(guest)
