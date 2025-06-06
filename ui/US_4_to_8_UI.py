from datetime import datetime
from business_logic.booking_manager import BookingManager
from business_logic.invoice_manager import InvoiceManager
from business_logic.hotel_manager import HotelManager
from data_access.booking_data_access import BookingDataAccess
from data_access.hotel_data_access import HotelDataAccess
from data_access.invoice_data_access import InvoiceDataAccess

db_path = "../database/hotel_sample.db"
booking_dal = BookingDataAccess(db_path)
invoice_dal = InvoiceDataAccess(db_path)
hotel_dal = HotelDataAccess(db_path)

booking_manager = BookingManager(booking_dal)
invoice_manager = InvoiceManager(invoice_dal)
hotel_manager = HotelManager(hotel_dal)


def user_story_menu():
    while True:
        print("\n-- USER STOrIES --")
        print("4. Zimmer buchen")
        print("5. Rechnung erhalten")
        print("6. Buchung stornieren")
        print("7. Dynamische Preisgestaltung")
        print("8. Alle Buchungen anzeigen")
        print("0. Zurück")

        choice = input("Wähle eine User Story: ")

        if choice == "0":
            break
        elif choice == "4":
            user_story_4()
        elif choice == "5":
            user_story_5()
        elif choice == "6":
            user_story_6()
        elif choice == "7":
            user_story_7()
        elif choice == "8":
            user_story_8()
        else:
            print("Ungültige Auswahl!")


def user_story_4():pass
def user_story_5():pass
def user_story_6():
    """Buchung stornieren"""
    try:
        bid = int(input("Buschung ID: "))
        booking = booking_dal.get_booking_by_id(bid)
        if not booking:
            print("Buchung nicht gefunden!")
            return
        # Markiere die Buchung als storniert
        booking_manager.booking_dal.execute(
            "Update Booking Set is_cancelled = 1 WHERE booking_id = ?", (bid,)
        )
        # Optionale Storno-Rechnungen erzeugen
        invoice_manager.create_invoice(bid, 0.0)
        print("Buchung storniert.")
    except Exception as e:
        print(f"Fehler: {e}")

def user_story_7():
    """Dynamische Preisberechnung anzeigen"""
    try:
        city = input("Stadt: ").strip()
        check_in = datetime.strptime(input("Check-in (YYYY-MM-DD): "), "%Y-%m-%d")
        check_out = datetime.strptime(input("Check-out (YYYY-MM-DD): "), "%Y-%m-%d")

        results = hotel_manager.find_available_hotels_by_date(city, check_in, check_out)
        if not results:
            print("Keine verfügbaren Zimmer gefunden.")
            return

        nights = (check_out - check_in).days
        for hotel, room in results:
            base = room.price_per_night
            if check_in.month in (6, 7, 8):
                factor = 1.2
            elif check_in.month in (11, 12, 1, 2):
                factor = 0.8
            else:
                factor = 1.0
            dyn_price = base * factor * nights
            print(f"{hotel.name}, Zimmer {room.room_number}: {dyn_price:.2f} CHF für {nights} Nächte")
    except Exception as e:
        print(f"Fehler: {e}")

def user_story_8():
    """Alle Buchunge anzeigen (Admin)"""
    try:
        bookings = booking_manager.get_all_bookings()
        for b in bookings:
            print(booking_manager.get_booking_details(b))
    except Exception as e:
        print(f"Fehler: {e}")

if __name__ == "__main__":
    user_story_menu()