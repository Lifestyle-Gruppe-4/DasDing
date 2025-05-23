from business_logic.guest_manager import GuestManager
from business_logic.address_manager import AddressManager
from data_access.address_data_access import AddressDataAccess
from data_access.guest_data_access import GuestDataAccess
from model.address import Address
from model.guest import Guest

# db_path = "../database/hotel_sample.db"
# guest_dal = GuestDataAccess(db_path)
# address_dal = AddressDataAccess(db_path)
#
# guest_manager = GuestManager(guest_dal)
# address_manager = AddressManager(address_dal)

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

# for guest in guest_manager.get_all_guests():
#     print(guest)





def get_user_choice():
    print("\n -----------Welcome to our Hotel Reservation System!-----------\n")
    print("1. Display available hotels")
    print("2. Search for hotels")
    print("3. Admin center")
    print("4. Exit")
    return int(input("Enter your choice: "))

def get_admin_choice():
    print("\n -----------Welcome to our Admin Center!-----------\n")
    print("1. Add new hotel")
    print("2. Delete existing hotel")
    print("3. Update existing hotel")
    print("4. Exit")
    return int(input("Enter your choice: "))

# start im Guest-Modus
mode = "guest"
is_continue = True

while is_continue:
    if mode =="guest":
        user_choice = get_user_choice()

        if user_choice == 1:
            print("-> alle hotels anzeigen")
        elif user_choice == 2:
            print("-> Hotel suchen")
        elif user_choice == 3:
            mode = "admin"
        elif user_choice == 4:
            print("Exit")
            is_continue = False
        else:
            print("Invalid choice, try again")

    elif mode =="admin":
        admin_choice = get_admin_choice()

        if admin_choice == 1:
            print("-> neues Hotel hinzufügen")
        elif admin_choice == 2:
            print("-> Hotel löschen")
        elif admin_choice == 3:
            print("-> Hotel aktualisieren")
        elif admin_choice == 4:
            print("Exit")
            is_continue = False
        else:
            print("Invalid choice, try again")