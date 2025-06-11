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

### User-Story 1.1,1.2,1.3 und 1.6
def hotel_suche():
    print("""
        === Hotelsuche ===
        1. Nach Stadt
        2. Nach Stadt und Mindeststerne
        3. Verfügbare Zimmer nach Stadt und Gästezahl
        4. Alle Hotels anzeigen
                """)
    user_input = input("Wählen Sie eine Suchoption: ")

    if user_input == "1":
        search_input = input("Geben sie die gewünschte Stadt ein: ")
        results = hotel_manager.find_by_city(search_input)
        if results:
            for hotel in results:
                print(f"{hotel.name} in {hotel.address.city} mit {hotel.stars} Sternen (Strasse: {hotel.address.street})")
        else:
            print("Kein Hotel in dieser Stadt gefunden")

    elif user_input == "2":
        city = input("Geben Sie die Stadt des Hotels ein: ")
        try:
            stars = int(input("Geben Sie die mindest Anzahl Sterne ein: "))
            if not 1 <= stars <= 5:
                print("Bitte geben Sie eine Zahl zwischen 1 und 5 ein.")
                return
        except ValueError:
            print("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")
            return

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

    elif user_input == "4":
        results = hotel_manager.get_all_hotels()
        if results:
            for hotel in results:
                print(f"{hotel.name} ({hotel.stars} Sterne) in {hotel.address.city}")

    else:
        print("Ungültige Eingabe. Bitte geben Sie eine Zahl von 1 bis 4 ein.")
#hotel_suche()

### User Story 1.4
def hotel_suche_nach_zeitraum():
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
        print("Ungültiges Datum. Bitte das Format YYYY-MM-DD verwenden.")
        return

    results = hotel_manager.find_available_hotels_by_date(city, check_in, check_out)
    if results:
        for hotel, room in results:
            print(f"{hotel.name} in {hotel.address.city}, Zimmer {room.room_number}")
    else:
        print("Keine passenden Hotels/Zimmer in diesem Zeitraum gefunden.")
#hotel_suche_nach_zeitraum()

### User Story 1.5
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
        guests = int(input("Geben Sie die Anzahl Ihrer Gäste ein: "))
        stars = int(input("Geben Sie die Mindestanzahl der gewünschten Sterne ein: "))
        if guests < 1:
            print("Bitte geben Sie eine gültige Gästeanzahl ein")
            return
        if not (1 <= stars <= 5):
            print("Bitte geben Sie eine Zahl zwischen 1 und 5 ein")
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
#suche_zimmer_stadt_zeitraum_gaeste_sterne()