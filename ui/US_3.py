from datetime import datetime, date

#Importieren der Models
from model.address import Address
from model.hotel import Hotel

# Importiere alle Manager und DataAccess-Klassen
from business_logic.address_manager import AddressManager
from business_logic.booking_manager import BookingManager
from business_logic.facility_manager import FacilityManager
from business_logic.guest_manager import GuestManager
from business_logic.hotel_manager import HotelManager
from business_logic.invoice_manager import InvoiceManager
from business_logic.room_manager import RoomManager
from business_logic.room_type_manager import RoomTypeManager

from data_access.address_data_access import AddressDataAccess
from data_access.booking_data_access import BookingDataAccess
from data_access.facility_data_access import FacilityDataAccess
from data_access.guest_data_access import GuestDataAccess
from data_access.hotel_data_access import HotelDataAccess
from data_access.invoice_data_access import InvoiceDataAccess
from data_access.room_data_access import RoomDataAccess
from data_access.room_type_data_access import RoomTypeDataAccess

# Datenbankpfad und Initialisierung der DALs
db_path = "../database/hotel_sample.db"
address_dal = AddressDataAccess(db_path)
booking_dal = BookingDataAccess(db_path)
facility_dal = FacilityDataAccess(db_path)
guest_dal = GuestDataAccess(db_path)
invoice_dal = InvoiceDataAccess(db_path)
room_dal = RoomDataAccess(db_path)
room_type_dal = RoomTypeDataAccess(db_path)
hotel_dal = HotelDataAccess(db_path,room_dal)

# Intialisierung der Manager
address_manager = AddressManager(address_dal)
booking_manager = BookingManager(booking_dal)
facility_manager = FacilityManager(facility_dal)
guest_manager = GuestManager(guest_dal)
invoice_manager = InvoiceManager(invoice_dal)
room_manager = RoomManager(room_dal)
room_type_manager = RoomTypeManager(room_type_dal)
hotel_manager = HotelManager(hotel_dal)

def user_story_3():
    while True:
        print("\n-- Hotelverwaltung (Admin) --")
        print("1. Hotel hinzufügen")
        print("2. Hotel entfernen")
        print("3. Hotel aktualisieren")
        print("0. Zurück")
        choice = input("Wähle eine Option: ").strip()

        if choice == "0":
            break

        # 3.1 Hotel hinzufügen
        elif choice == "1":
            print("\n--- Neues Hotel mit Adresse erstellen ---")

            name = input("Hotelname: ").strip()
            stars = int(input("Anzahl Sterne (1–5): ").strip())

            street = input("Strasse: ").strip()
            city = input("Stadt: ").strip()
            zip_code = input("PLZ: ").strip()

            # Address-Instanz direkt erstellen (ID = None, wird automatisch durch DB vergeben)
            new_address = Address(address_id=None, street=street, city=city, zip_code=zip_code)
            address = address_manager.create_address(new_address)

            hotel = Hotel(
                hotel_id=None,
                name=name,
                stars=stars,
                address=address
            )

            hotel_id = hotel_manager.create_hotel(hotel)
            print(f"\nHotel '{name}' wurde erfolgreich erstellt (ID: {hotel_id})")

        # 3.2 Hotel entfernen
        elif choice == "2":
            hid     = int(input("Hotel-ID zum Entfernen: ").strip())
            success = hotel_manager.delete_hotel(hid)
            print("Hotel entfernt." if success else "Hotel nicht gefunden.")

        # 3.3 Hotel aktualisieren
        elif choice == "3":
            hid    = int(input("Hotel-ID zum Aktualisieren: ").strip())
            hotels = hotel_manager.get_all_hotels()
            hotel  = next((h for h in hotels if h.hotel_id == hid), None)
            if not hotel:
                print("Hotel nicht gefunden.")
                continue

            name_input  = input(f"Neuer Name ({hotel.name}): ").strip()
            stars_input = input(f"Neue Sterne ({hotel.stars}): ").strip()

            updated = Hotel(
                hotel_id=hid,
                name   = name_input or hotel.name,
                stars  = int(stars_input) if stars_input else hotel.stars,
                address=hotel.address
            )
            hotel_manager.update_hotel(updated)
            print("Hotelinformationen aktualisiert.")

        else:
            print("Ungültige Auswahl.")

user_story_3()

# if __name__ == "__main__":
#     DB_PATH = "../database/hotel_sample.db"
#     user_story_3(DB_PATH)
