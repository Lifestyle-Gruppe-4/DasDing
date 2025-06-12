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

### User Story 2
def info_pro_zimmer():
    # Stadt abfragen und Hotels auflisten
    city = input("In welcher Stadt möchten Sie ein Zimmer Buchen? ").strip()
    hotels = hotel_manager.find_by_city(city)
    if not hotels:
        print(f"Keine Hotels in {city} gefunden.")
        return

    print("\nGefundene Hotels:")
    for i,h in enumerate(hotels,1):
        print(f"{i}. {h.name} ({h.stars} Sterne) - {h.address.street}")

    # Hotel auswählen
    try:
        idx = int(input("\nWählen Sie ein Hotel (Nummer): "))
        hotel = hotels[idx-1]
    except ValueError:
        print("Ungültige Auswahl.")
        return

    # Nach Datum fragen
    use_dates = input("Möchten Sie einen Zeitraum für Ihren Aufenthalt angeben? (J/N): ").strip().lower()
    # Setzt CheckIn und CheckOut zuerst auf None
    check_in = check_out = None
    if use_dates == "j":
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

    # Zimmer finden
    if check_in and check_out:
        # nur Zimmer in diesm Zeitraum
        results = hotel_manager.find_available_rooms_by_hotel_and_date(hotel,check_in,check_out)
    else:
        # alle Zimmer im Hotel
        results = hotel_manager.find_all_rooms_by_hotel(hotel)

    if not results:
        print("Keine Zimmer gefunden.")
        return

    # Ausgabe
    for room in results:
        desc = room.room_type.description
        max_guests = room.room_type.max_guests
        facilities = ', '.join(f.facility_name for f in room.facilities)
        base_price = room.price_per_night
        print(f"\n{hotel.name}, Zimmer {room.room_number} ({desc}, max. {max_guests} Gäste)")
        print(f"  Ausstattung: {facilities}")

        if check_in and check_out:
            nights = (check_out - check_in).days
            season_price , factor = room_manager.calculate_seasonal_price(base_price,check_in)
            total = season_price * nights
            print(f"  Preis/Nacht: CHF {season_price:.2f} (Basis {base_price:.2f} × Faktor {factor:.2f})")
            print(f"  Gesamtpreis für {nights} Nächte: CHF {total:.2f}")
        else:
            # ohne Datumsangabe: nur Basispreis
            print(f"  Preis/Nacht: CHF {base_price:.2f}")
info_pro_zimmer()