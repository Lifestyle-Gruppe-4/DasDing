from datetime import datetime, date

# Importiere alle Manager,DataAccess-Klassen und Models
from business_logic import AddressManager,BookingManager,FacilityManager,GuestManager,HotelManager,InvoiceManager,RoomManager,RoomTypeManager
from data_access import AddressDataAccess,BookingDataAccess,FacilityDataAccess,GuestDataAccess,HotelDataAccess,InvoiceDataAccess,RoomDataAccess,RoomTypeDataAccess
from model import Address,Booking,Facility,Guest,Hotel,Invoice,Room,RoomType

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

def user_story_7():
    """Dynamische Preisberechnung anzeigen"""
    try:
        city = input("Stadt: ").strip()
        check_in = datetime.strptime(input("Check-in (YYYY-MM-DD): "), "%Y-%m-%d").date()
        check_out = datetime.strptime(input("Check-out (YYYY-MM-DD): "), "%Y-%m-%d").date()

        results = hotel_manager.find_available_hotels_by_date(city, check_in, check_out)
        if not results:
            print("Keine verfügbaren Zimmer gefunden.")
            return

        nights = (check_out - check_in).days
        for hotel, room in results:
            season_price, factor = room_manager.calculate_seasonal_price(room.price_per_night, check_in)
            total = season_price * nights

            print(f"{hotel.name} - Zimmer {room.room_number}")
            print(f" Zeitraum: {check_in} bis {check_out} ({nights} Nächte)")
            print(f" Standardpreis pro Nacht: {room.price_per_night:.2f} CHF")
            print(f" Saisonpreis pro Nacht: (Faktor {factor:.2f}): {season_price:.2f} CHF")
            print(f" Gesamtpreis: {total:.2f} CHF\n")

    except Exception as e:
        print(f"Fehler: {e}")