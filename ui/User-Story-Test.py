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

# User Story 1.5
def suche_zimmer_stadt_zeitraum_gaeste_sterne():
    city = input("Stadt: ").strip()
    check_in = datetime.strptime(input("Check-in (YYYY-MM-DD): "), "%Y-%m-%d")
    check_out = datetime.strptime(input("Check-out (YYYY-MM-DD): "), "%Y-%m-%d")
    guests = int(input("Gib die Anzahl der Gäste ein: "))
    stars = int(input("Gib die Mindestanzahl Sterne ein: "))

    results = hotel_manager.find_available_hotels_by_date_guest_stars(city, check_in, check_out, guests, stars)
    if results:
        for hotel, room in results:
            print(f"{hotel.name} in {hotel.address.city}, Zimmer {room.room_number}")
    else:
        print("Keine passenden Hotels/Zimmer in diesem Zeitraum gefunden.")

#suche_zimmer_stadt_zeitraum_gaeste_sterne()

# User Story 1.6
def hotel_suche():
    print("""
        === Hotelsuche ===
        1. Nach Stadt
        2. Nach Stadt und Mindeststerne
        3. Verfügbare Zimmer nach Stadt und Gästezahl
                """)
    user_input = input("Wähle eine Suchoption: ")

    if user_input == "1":
        search_input = input("Gib die Stadt des Hotels ein: ")
        results = hotel_manager.find_by_city(search_input)
        if results:
            for hotel in results:
                print(f"{hotel.name} in {hotel.address.city} mit {hotel.stars} Sternen (Strasse: {hotel.address.street})")
        else:
            print("Kein Hotel in dieser Stadt gefunden")

    elif user_input == "2":
        city = input("Gib die Stadt des Hotels ein: ")
        stars = int(input("Gib die mindest Anzahl Sterne ein: "))
        results = hotel_manager.find_hotel_by_city_and_min_stars(city,stars)
        if results:
            for hotel in results:
                print(f"{hotel.name} in {hotel.address.city} mit {hotel.stars} Sternen (Strasse: {hotel.address.street})")
        else:
            print("Kein Hotel mit diesen Kriterien gefunden")

    elif user_input == "3":
        city = input("Stadt: ").strip()
        guests = int(input("Anzahl Gäste (mind. 1): "))
        if guests < 1:
            print("Die Gästeanzahl muss mindestens 1 sein.")
            return
        results = hotel_manager.find_hotels_with_matching_rooms(city, guests)
        if results:
            for hotel, room in results:
                print(f"{hotel.name} in {hotel.address.city} mit {hotel.stars} Sternen (Strasse: {hotel.address.street})")
        else:
            print("Keine passenden Hotels/Zimmer gefunden.")

#hotel_suche()

def info_pro_zimmer():
    city = input("Stadt: ").strip()
    check_in = datetime.strptime(input("Check-in (YYYY-MM-DD): "), "%Y-%m-%d")
    check_out = datetime.strptime(input("Check-out (YYYY-MM-DD): "), "%Y-%m-%d")

    results = hotel_manager.find_available_hotels_by_date(city, check_in, check_out)
    if results:
        for hotel, room in results:
            nights = (check_out - check_in).days
            total_price = nights * room.price_per_night
            facilities = ', '.join(f.facility_name for f in room.facilities)
            print(f"{hotel.name} in {hotel.address.city}, Zimmer {room.room_number} ({room.room_type.description}, max. Gäste: {room.room_type.max_guests}) "
                  f"mit {facilities} für CHF {room.price_per_night:.2f} pro Nacht. "
                  f"Gesamtpreis CHF {total_price:.2f}")

info_pro_zimmer()