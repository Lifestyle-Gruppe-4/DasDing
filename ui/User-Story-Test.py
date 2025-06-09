from datetime import datetime, date
#Importieren der Models
from model.address import Address
from model.hotel import Hotel

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
    try:
        check_in = datetime.strptime(input("Check-in (YYYY-MM-DD): "), "%Y-%m-%d")
        check_out = datetime.strptime(input("Check-out (YYYY-MM-DD): "), "%Y-%m-%d")
        if check_in < datetime.today():
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
        if not (1 <= stars >= 5):
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

#suche_zimmer_stadt_zeitraum_gaeste_sterne()

# User Story 1.6
def hotel_suche():
    print("""
        === Hotelsuche ===
        1. Nach Stadt
        2. Nach Stadt und Mindeststerne
        3. Verfügbare Zimmer nach Stadt und Gästezahl
        4. Alle Hotels anzeigen
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
        try:
            stars = int(input("Gib die mindest Anzahl Sterne ein: "))
            if not 1 <= stars <= 5:
                print("Bitte gib eine Zahl zwischen 1 und 5 ein.")
                return
        except ValueError:
            print("Ungültige Eingabe. Bitte gib eine Zahl ein.")
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



def info_pro_zimmer():
    city = input("Stadt: ").strip()
    try:
        check_in = datetime.strptime(input("Check-in (YYYY-MM-DD): "), "%Y-%m-%d")
        check_out = datetime.strptime(input("Check-out (YYYY-MM-DD): "), "%Y-%m-%d")

        if check_in < datetime.today():
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
            nights = (check_out - check_in).days
            season_price, factor = room_manager.calculate_seasonal_price(room.price_per_night,check_in)
            total_price = season_price * nights
            facilities = ', '.join(f.facility_name for f in room.facilities)
            print(f"{hotel.name} in {hotel.address.city}, Zimmer {room.room_number} ({room.room_type.description}, max. Gäste: {room.room_type.max_guests}) "
                  f"mit {facilities} für CHF {room.price_per_night:.2f} pro Nacht. "
                  f"Gesamtpreis für {nights} Nächte CHF {total_price:.2f}")

#info_pro_zimmer()

def hotel_suche_nach_zeitraum():
    city = input("Stadt: ").strip()
    try:
        check_in = datetime.strptime(input("Check-in (YYYY-MM-DD): "), "%Y-%m-%d")
        check_out = datetime.strptime(input("Check-out (YYYY-MM-DD): "), "%Y-%m-%d")
        if check_in < datetime.today():
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

def zeige_alle_hotels():
    results = hotel_manager.get_all_hotels()
    if results:
        for hotel in results:
            print(f"{hotel.name} in {hotel.address.city}")

#zeige_alle_hotels()

### User Story 5
def rechnung_erstellen_nach_aufenthalt():
    try:
        # Alle Buchungen holen aus BookingManager
        bookings = booking_manager.get_all_bookings()
        # Filtert Buchungen die bereits vorbei sind
        past_bookings = [b for b in bookings if b.check_out_date < datetime.today().date() and not b.is_cancelled
                         and not invoice_manager.has_invoice_for_booking(b.booking_id)
                         ]
        if not past_bookings:
            print("Alle abgeschlossenen Buchungen wurden bereits abgerechnet.")
            return
        # Alle gültigen Buchungen werden mit fortlaufender Nummer angezeigt
        print("Abgeschlossene Buchungen:")
        for i, b in enumerate(past_bookings):
            print(f"{i + 1}. {BookingManager.get_booking_details(b)}")

        user_choice = int(input("Für welche Buchung soll eine Rechnung erstellt werden? (Nummer eingeben): "))
        if not (1 <= user_choice <= len(past_bookings)):
            print("Ungültige Auswahl.")
            return

        booking = past_bookings[user_choice - 1]

        # Rechnung erstellen
        invoice_id = invoice_manager.create_invoice(
            booking_id=booking.booking_id,
            total_amount=booking.total_amount
        )
        print(f"Rechnung erstellt! (Rechnungs-ID: {invoice_id})")

        invoice = invoice_manager.get_invoice_by_id(invoice_id)
        print(f" Es wurde folgende Rechnung erstellt:\n"
              f"{invoice}")


    except ValueError:
        print("Ungültige Eingabe.")
    except Exception as e:
        print(f"Fehler: {e}")

#rechnung_erstellen_nach_aufenthalt()



def alle_rechnungen():
    invoices = invoice_manager.get_all_invoices()
    for invoice in invoices:
        print(invoice)
#alle_rechnungen()

def rechnungen_löschen():
    invoices_id = int(input("ID: "))
    invoice_manager.delete_invoice(invoices_id)
#rechnungen_löschen()


def create_simple_hotel():
    print("\n--- Neues Hotel mit Adresse erstellen ---")

    name = input("Hotelname: ").strip()
    stars = int(input("Anzahl Sterne (1–5): ").strip())

    street = input("Strasse: ").strip()
    city = input("Stadt: ").strip()
    zip_code = input("PLZ: ").strip()

    # Address-Instanz direkt erstellen (ID = None, wird automatisch durch DB vergeben)
    new_address = Address(address_id=None, street=street, city=city, zip_code=zip_code)
    address = address_manager.create_address(new_address)

    hotel = Hotel(
        hotel_id=None,
        name=name,
        stars=stars,
        address=address
    )

    hotel_id = hotel_manager.create_hotel(hotel)
    print(f"\nHotel '{name}' wurde erfolgreich erstellt (ID: {hotel_id})")

create_simple_hotel()
