from datetime import date

# Importiere alle Manager,DataAccess-Klassen und Models
from business_logic import AddressManager,BookingManager,FacilityManager,GuestManager,HotelManager,InvoiceManager,RoomManager,RoomTypeManager
from data_access import AddressDataAccess,BookingDataAccess,FacilityDataAccess,GuestDataAccess,HotelDataAccess,InvoiceDataAccess,RoomDataAccess,RoomTypeDataAccess


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

        hochsaison_date = date(date.today().year, 7, 1)
        nebensaison_date = date(date.today().year, 3, 1)
        normalsaison_date = date(date.today().year, 6, 1)

        hotels = hotel_manager.get_all_hotels()
        if not hotels:
            print("Keine Hotels gefunden.")
            return

        for hotel in hotels:
            print(f"Hotel: {hotel.name}")
            for room in hotel.rooms:
                base_price = room.price_per_night

                hoch_price, hoch_factor = room_manager.calculate_seasonal_price(base_price, hochsaison_date)
                neben_price, neben_factor = room_manager.calculate_seasonal_price(base_price, nebensaison_date)
                normal_price, normal_factor = room_manager.calculate_seasonal_price(base_price, normalsaison_date)

                print(f" Zimmer {room.room_number}")
                print(f"   Basispreis: {base_price:.2f} CHF")
                print(f"   Hochsaison (Faktor {hoch_factor:.2f}): Preis {hoch_price:.2f} CHF")
                print(f"   Nebensaison (Faktor {neben_factor:.2f}): Preis {neben_price:.2f} CHF")
                print(f"   Normalsaison (Faktor {normal_factor:.2f}): Preis {normal_price:.2f} CHF\n")

    except Exception as e:
        print(f"Fehler: {e}")

user_story_7()