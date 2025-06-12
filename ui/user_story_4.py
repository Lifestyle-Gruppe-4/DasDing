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
        city = input("In welcher Stadt möchten Sie Ihren Aufenthalt buchen? ").strip()
        # Prüft ob in dieser Stadt ein Hotel existiert
        result_city = hotel_manager.find_by_city(city)
        if not result_city:
            print("Keine Hotel in dieser Stadt gefunden")
            return

        check_in = datetime.strptime(input("Check_in (YYYY-MM-DD): "), "%Y-%m-%d").date()
        check_out = datetime.strptime(input("Check_out (YYYY-MM-DD: "), "%Y-%m-%d").date()
        # Prüft das check_in Datum nicht in der Vergangenheit lieget
        if check_in < date.today():
            print("Das Check-in Datum darf nicht in der Vergangenheit liegen!")
            return

        if check_out <= date.today():
            print("Das Check-out Datum muss nach dem Check-in Datum liegen!")
            return

        results = hotel_manager.find_available_hotels_by_date(city, check_in, check_out)
        if not results:
            print("Keine verfügbaren Zimmer gefunden.")
            return

        print("\nVerfügbare Hotels und Zimmer:")
        for idx, (hotel, room) in enumerate(results, start=1):
            print(f"{idx}. {hotel.name} -  Zimmer {room.room_number} (Preis/Nacht: {room.price_per_night} CHF)")

        try:
            selection = int(input("Wähle ein Hotel/Zimmer (0 zum Abbrechen): "))
        except ValueError:
            print("Ungültige Eingabe.")
            return
        if selection == 0 or selection > len(results):
            print("Abgebrochen.")
            return

        hotel, room = results[selection - 1]

        while True:
            print("0 = Exit | 1 = Bestehende Kunde | 2 = Neue Kunde")
            option = input("Wähle eine Option: ").strip()

            if option == "0":
                print("Abgebrochen.")
                return

            elif option == "1":
                first_name = input("Vorname des Kunden: ").strip()
                last_name = input("Nachname des Kunden: ").strip()
                guest = next((g for g in guest_manager.get_all_guests()
                              if g.first_name.lower() == first_name.lower()
                              and g.last_name.lower() == last_name.lower()), None)

                if not guest:
                    print("Kunde nicht gefunden.")
                    continue
                guest_id = guest.guest_id
                break

            elif option == "2":
                print("\n-- Neuer Kunde --")
                first_name = input("Vorname: ").strip()
                last_name = input("Nachname: ").strip()
                email = input("Email: ").strip()
                street = input("Street inkl Nr: ").strip()
                guest_city = input("City: ").strip()
                guest_zip = input("Zip: ").strip()

                address = Address(address_id=None, street=street, city=guest_city, zip_code=guest_zip)
                created_address = address_manager.create_address(address)
                new_guest = Guest(None, first_name, last_name, email, created_address)
                guest_id = guest_manager.add_guest(new_guest)
                break

            else:
                print("Ungültige Auswahl.")

        booking_id = booking_manager.create_booking(check_in, check_out, guest_id, room.room_id, room.price_per_night)
        print(f"Buchung abgeschlossen. Buchung-ID: {booking_id}")

    except Exception as e:
        print(f"Fehler: {e}")

user_story_4()