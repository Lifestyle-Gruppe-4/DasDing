from datetime import datetime

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
from ui.UI import is_continue, user_choice

# Datenbankpfad und Initialisierung der DALs
db_path = "../database/hotel_sample.db"
address_dal = AddressDataAccess(db_path)
booking_dal = BookingDataAccess(db_path)
facility_dal = FacilityDataAccess(db_path)
guest_dal = GuestDataAccess(db_path)
hotel_dal = HotelDataAccess(db_path)
invoice_dal = InvoiceDataAccess(db_path)
room_dal = RoomDataAccess(db_path)
room_type_dal = RoomTypeDataAccess(db_path)

# Intialisierung der Manager
address_manager = AddressManager(address_dal)
hotel_manager = HotelManager(hotel_dal)
booking_manager = BookingManager(booking_dal)
facility_manager = FacilityManager(facility_dal)
guest_manager = GuestManager(guest_dal)
invoice_manager = InvoiceManager(invoice_dal)
room_manager = RoomManager(room_dal)
room_type_manager = RoomTypeManager(room_type_dal)

def main_menu():
        print("""
        ==== HOTELVERWALTUNGSSYSTEM ====
        1. Hotels nach Stadt/Sternen/Gästezahl anzeigen
        2. Verfügbare Zimmer suchen (nach Zeitraum und Gästezahl)
        3. Zimmer buchen
        4. Buchungen verwalten (anzeigen, ändern, stornieren)
        5. Rechnungen verwalten
        6. Hotelverwaltung (Admin)
        7. Dynamische Preisanzeige
        8. Buchungsübersicht (Admin)
        9. Zimmerausstattung anzeigen
        10. Stammdaten verwalten (Admin)
        11. Beenden
        """)
        return int(input("Gib deine Wahl ein"))

def search_by_city_stars_guests():
    print("\nBitte gib hier deine Kriterien ein")
    city = input("Stadt: ")
    stars = int(input("Sterne: "))
    guests = int(input("Anzahl Gäste: "))
    return city, stars, guests

mode = "main"
is_continue = True

while is_continue:
    if mode =="main":
        user_choice = main_menu()
        if user_choice == 1:
            city = input("Stadt: ")
            stars = int(input("Sterne: "))
            guests = int(input("Anzahl Gäste: "))
            result = hotel_manager.find_hotels_with_matching_rooms(city, stars, guests)
            if result:
                for hotel, room in result:
                    print(f"{hotel.name} in {hotel.address.city} mit {hotel.stars} Sterne "
                          f"(Strasse: {hotel.address.street}) – Platz für {room.room_type.max_guests} Gäste")
                    is_continue = False
            else:
                print("Kein passendes Hotel gefunden")






        elif user_choice == 11:
            print("Tschau")
            is_continue = False
