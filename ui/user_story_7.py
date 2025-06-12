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
        #city = input("Stadt: ").strip()
        #check_in = datetime.strptime(input("Check-in (YYYY-MM-DD): "), "%Y-%m-%d").date()
        #check_out = datetime.strptime(input("Check-out (YYYY-MM-DD): "), "%Y-%m-%d").date()
        hochsaison_date = date(date.today().year, 7, 1)
        nebensaison_date = date(date.today().year, 3, 1)
        normalsaison_date = date(date.today().year, 6, 1)

        #results = hotel_manager.find_available_hotels_by_date(city, check_in, check_out)
        #if not results:
         #   print("Keine verfügbaren Zimmer gefunden.")
          #  return
        hotels = hotel_manager.get_all_hotels()
        if not hotels:
            print("Keine Hotels gefunden.")
            return

        #nights = (check_out - check_in).days
        #for hotel, room in results:
          #  season_price, factor = room_manager.calculate_seasonal_price(room.price_per_night, check_in)
          #  total = season_price * nights
        for hotel in hotels:
            print(f"Hotel: {hotel.name}")
            for room in hotel.rooms:
                base_price = room.price_per_night

          #  print(f"{hotel.name} - Zimmer {room.room_number}")
          #  print(f" Zeitraum: {check_in} bis {check_out} ({nights} Nächte)")
          #  print(f" Standardpreis pro Nacht: {room.price_per_night:.2f} CHF")
          #  print(f" Saisonpreis pro Nacht: (Faktor {factor:.2f}): {season_price:.2f} CHF")
          #  print(f" Gesamtpreis: {total:.2f} CHF\n")
                hoch_price, hoch_factor = room_manager.calculate_seasonal_price(base_price, hochsaison_date)
                neben_price, neben_factor = room_manager.calculate_seasonal_price(base_price, nebensaison_date)
                normal_price, normal_factor = room_manager.calculate_seasonal_price(base_price, normalsaison_date)

                print(f" Zimmer {room.room_number}")
                print(f"   Basispreis: {base_price:.2f} CHF")
                print(f"   Hochsaison ({hochsaison_date} | Faktor {hoch_factor:.2f}): {hoch_price:.2f} CHF")
                print(f"   Nebensaison ({nebensaison_date} | Faktor {neben_factor:.2f}): {neben_price:.2f} CHF")
                print(f"   Normalsaison ({normalsaison_date} | Faktor {normal_factor:.2f}): {normal_price:.2f} CHF\n")

    except Exception as e:
        print(f"Fehler: {e}")

user_story_7()