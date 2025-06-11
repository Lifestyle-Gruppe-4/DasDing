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

def user_story_4():
    try:
        city = input("Stadt: ").strip()
        check_in = datetime.strptime(input("Check_in (YYYY-MM-DD)"), "%Y-%m-%d").date()
        check_out = datetime.strptime(input("check_out (YYYY-MM-DD"), "%Y-%m-%d").date()

        if check_out <= check_in:
            print("Check-out muss nach dem Check-in liegen.")
            return

        results = hotel_manager.find_available_hotels_by_date(city, check_in, check_out)
        if not results:
            print("Keine verfügbaren Zimmer gefunden.")
            return

        print("\nVerfügbare Hotels und Zimmer:")
        for idx, (hotel, room) in enumerate(results, start=1):
            print(f"{idx}. {hotel.name} -  Zimmer {room.room_number} (Preis/Nacht: {room.price_per_night:2f} CHF)")

        try:
            selection = int(input("Wähle ein Hotel/Zimmer (0 zum Abbrechen): "))
        except ValueError:
            print("Ungültige Eingabe.")
            return
        if selection == 0 or selection > len(results):
            print("Abgebrochen.")
            return

        hotel, room = results[selection - 1]
        guest_id = int(input("Gäste-ID: "))
        booking_id = booking_manager.create_booking(check_in, check_out, guest_id, room.room_id, room.price_per_night)
        print(f"Buchung abgeschlossen. Buchung-ID: {booking_id}")
    except Exception as e:
        print(f"Fehler: {e}")

user_story_4()