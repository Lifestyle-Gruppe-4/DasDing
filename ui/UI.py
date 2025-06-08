from business_logic.guest_manager import GuestManager
from business_logic.address_manager import AddressManager
from business_logic.room_manager import RoomManager
from data_access.address_data_access import AddressDataAccess
from data_access.guest_data_access import GuestDataAccess
from data_access.hotel_data_access import HotelDataAccess
from data_access.booking_data_access import BookingDataAccess
from business_logic.hotel_manager import HotelManager
from business_logic.booking_manager import BookingManager
from data_access.room_data_access import RoomDataAccess
from model.address import Address
from model.guest import Guest
from model.hotel import Hotel



db_path = "../database/hotel_sample_old.db"
address_dal = AddressDataAccess(db_path)
booking_dal     = BookingDataAccess(db_path)
room_dal = RoomDataAccess(db_path)
hotel_dal = HotelDataAccess(db_path, room_dal)

booking_manager = BookingManager(booking_dal)
hotel_manager = HotelManager(hotel_dal)
address_manager = AddressManager(address_dal)
room_manager = RoomManager(room_dal)


def get_user_choice():
    print("\n -----------Welcome to our Hotel Reservation System!-----------\n")
    print("1. Display available hotels")
    print("2. Search for hotels")
    print("3. Search for hotels by city")
    print("4. Erweiterte Suche")
    print("5. Admin center")
    print("6. Exit")
    return int(input("Enter your choice: "))
def get_admin_choice():
    print("\n -----------Welcome to our Admin Center!-----------\n")
    print("1. Add new hotel")
    print("2. Delete existing hotel")
    print("3. Update existing hotel")
    print("4. Display all hotels")
    print("5. Display all bookings")
    print("6. Display rooms with amenities")
    print("7. Stammdaten verwalten")
    print("8. Exit")
    choice = input ("Enter your choice: ")

    try:
        num = int(choice)
    except ValueError:
        print("Ungültige Eingabe: Bitte eine Zahl eingeben.")

    if 1 <= num <= 8:
        return num
    else:
        print("Ungültige Auswahl: Bitte eine Zahl zwischen 1 und 8 eingeben.")

def get_user_choice_plus():
    print("\nBitte gib hier deine Kriterien ein")

    city = input("Enter your city: ")

    while True:
        stars_input = input("Enter your minimum stars: ")
        try:
            stars = int(stars_input)
            if stars < 1 or stars > 5:
                print("Bitte gib eine Zahl zwischen 1 und 5 ein.")
            else:
                break
        except ValueError:
            print("Ungültige Eingabe - bitte eine Zahl eingeben")
    return city, stars

#start im Guest-Modus
mode = "guest"
is_continue = True


while is_continue:
    if mode =="guest":
        user_choice = get_user_choice()

        if user_choice == 1:
            print("Hier sind alle Hotels")
            for hotel in hotel_manager.get_all_hotels():
                print(f"{hotel.name} ({hotel.stars} Sterne) in {hotel.address.city}")
        elif user_choice == 2:
            search_input = input("Gib den Name des Hotels ein: ")
            results = hotel_manager.find_by_name(search_input)
            if results:
                for hotel in results:
                    print(f"{hotel.name} ({hotel.stars} Sterne) in {hotel.address.city}")
            else:
                print("Kein Hotel mit diesem Name gefunden")
        elif user_choice == 3:
            search_input = input("Gib die Stadt des Hotels ein: ")
            results = hotel_manager.find_by_city(search_input)
            if results:
                for hotel in results:
                    print(f"{hotel.name} in {hotel.address.city} mit {hotel.stars} Sternen (Strasse: {hotel.address.street})")
            else:
                print("Kein Hotel in dieser Stadt gefunden")
        elif user_choice == 4:
            mode = "erweiterte_suche"
        elif user_choice == 5:
            mode = "admin"
        elif user_choice == 6:
            print("Exit")
            is_continue = False
        else:
            print("Invalid choice, try again")

    elif mode =="erweiterte_suche":
        city, stars = get_user_choice_plus()
        result = hotel_manager.find_hotel_by_city_and_min_stars(city,stars)
        if result:
            for hotel in result:
                print(f"{hotel.name} in {hotel.address.city} mit {hotel.stars} Sterne (Strasse: {hotel.address.street})")
                is_continue = False
        else:
            print("Kein passendes Hotel gefunden")






    elif mode == "admin":
        admin_choice = get_admin_choice()

        if admin_choice == 1:
            print("-> Neues Hotel hinzufügen")

        elif admin_choice == 2:
            print("-> Hotel löschen")

        elif admin_choice == 3:
            print("-> Hotel aktualisieren")

        elif admin_choice == 4:
            for hotel in hotel_manager.get_all_hotels():
                print(f"{hotel.hotel_id}: {hotel.name} ({hotel.stars} Sterne) in {hotel.address.city}")

        elif admin_choice == 5:
            all_bookings = booking_manager.get_all_bookings()
            if not all_bookings:
                print("Keine Buchungen vorhanden.")
            else:
                print("\nAlle Buchungen:")
                for b in all_bookings:
                    print(
                        f"{b.booking_id}: Hotel „{b.hotel.name}“, "
                        f"Gast {b.guest.first_name} {b.guest.last_name}, "
                        f"Zimmer {b.room.room_number}, {b.check_in}–{b.check_out}"
                    )

        elif admin_choice == 6:
            rooms = room_manager.get_all_rooms_with_facilities()
            if not rooms:
                print("Keine Zimmer gefunden.")
            else:
                print("\nZimmer mit Ausstattung:")
                for room in rooms:
                    # angenommen: room.facilities ist List[Facility]
                    amenities = ", ".join(f.name for f in room.facilities)
                    print(f"Zimmer {room.room_number} (ID {room.room_id}): {amenities}")

        elif admin_choice == 8:
            print("Verlasse Admin-Center")
            mode = "guest"

        else:
            print("Ungültige Auswahl, bitte erneut versuchen")
