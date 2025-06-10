from datetime import datetime, date

# Importiere alle Manager,DataAccess-Klassen und Models
from business_logic import AddressManager,BookingManager,FacilityManager,GuestManager,HotelManager,InvoiceManager,RoomManager,RoomTypeManager
from data_access import AddressDataAccess,BookingDataAccess,FacilityDataAccess,GuestDataAccess,HotelDataAccess,InvoiceDataAccess,RoomDataAccess,RoomTypeDataAccess
from model import address,booking,facility,guest,hotel,invoice,room,room_type

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


def suche_zimmer_stadt_zeitraum_gaeste_sterne():
    city = input("Stadt: ").strip()
    try:
        check_in = datetime.strptime(input("Check-in (YYYY-MM-DD): "), "%Y-%m-%d").date()
        check_out = datetime.strptime(input("Check-out (YYYY-MM-DD): "), "%Y-%m-%d").date()
        if check_in < date.today():
            print("Das Check-in Datum darf nicht in der Vergangenheit liegen")
            return
        if check_out <= check_in:
            print("Das Check-out Datum muss nach dem Check-in Datum liegen")
            return
    except ValueError:
        print("Ungpltiges Datum. Bitte das Format YYYY-MM-DD verwenden.")
        return

    try:
        guests = int(input("Gib die Anzahl der Gäste ein: "))
        stars = int(input("Gib die Mindestanzahl Sterne ein: "))
        if guests < 1:
            print("Bitte gib eine gültige Gästeanzahl ein")
            return
        if not (1 <= stars <= 5):
            print("Bitte gib eine Zahl zwischen 1 und 5 ein")
            return
    except ValueError:
        print("Ungülte Eingabe. Bitte gib eine gültige Zahl ein.")
        return

    results = hotel_manager.find_available_hotels_by_date_guest_stars(city, check_in, check_out, guests, stars)
    if results:
        for hotel, room in results:
            print(f"{hotel.name} in {hotel.address.city}, Zimmer {room.room_number}")
    else:
        print("Keine passenden Hotels/Zimmer in diesem Zeitraum gefunden.")

suche_zimmer_stadt_zeitraum_gaeste_sterne()