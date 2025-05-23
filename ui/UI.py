from business_logic.guest_manager import GuestManager
from business_logic.address_manager import AddressManager
from data_access.address_data_access import AddressDataAccess
from data_access.guest_data_access import GuestDataAccess
from data_access.hotel_data_access import HotelDataAccess
from business_logic.hotel_manager import HotelManager
from model.address import Address
from model.guest import Guest
from model.hotel import Hotel

db_path = "../database/hotel_sample.db"
hotel_dal = HotelDataAccess(db_path)
address_dal = AddressDataAccess(db_path)

hotel_manager = HotelManager(hotel_dal)
address_manager = AddressManager(address_dal)

# hotel_name = input("Enter Hotel Name: ")
# stars = input("Enter Hotel Stars: ")
#
# address = address_manager.find_address_by_id(1)
#
# if address is None:
#     print("Address Not Found")
# else:
#     new_hotel = Hotel(hotel_id=None, name=hotel_name, stars=stars, address=address)
#
# hotel_id = hotel_manager.create_hotel(new_hotel)
# print(f"Gast gespeichert mit ID: {hotel_id}")

# delete_id = input("Enter ID to delete")
#
# delete_hotel = hotel_manager.delete_hotel(delete_id)
#
# for hotel in hotel_manager.get_all_hotels():
#     print(hotel)



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
            print("Hier sind alle Hotels")
            for hotel in hotel_manager.get_all_hotels():
                print(hotel)
        elif user_choice == 2:
            search_input = input("gib den Name des Hotels ein: ")
            results = hotel_manager.find_by_name(search_input)
            if results:
                for hotel in results:
                    print(hotel)
            else:
                print("kein Hotel Gefunden")

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