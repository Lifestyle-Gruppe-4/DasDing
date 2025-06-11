from datetime import datetime
#from logging import exception

from business_logic.booking_manager import BookingManager
from business_logic.invoice_manager import InvoiceManager
from business_logic.hotel_manager import HotelManager
from business_logic.room_manager import RoomManager
from data_access.booking_data_access import BookingDataAccess
from data_access.hotel_data_access import HotelDataAccess
from data_access.invoice_data_access import InvoiceDataAccess
from data_access.room_data_access import RoomDataAccess
#from ui.UI import room_manager

db_path = "../database/hotel_sample.db"
booking_dal = BookingDataAccess(db_path)
invoice_dal = InvoiceDataAccess(db_path)
room_dal = RoomDataAccess(db_path)
hotel_dal = HotelDataAccess(db_path, room_dal)

booking_manager = BookingManager(booking_dal)
invoice_manager = InvoiceManager(invoice_dal)
hotel_manager = HotelManager(hotel_dal)
room_manager = RoomManager(room_dal)


def user_story_menu():
    while True:
        print("\n-- USER STORIES --")
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


def user_story_4():
    try:
        city = input("Stadt: ").strip()
        check_in = datetime.strptime(input("Check-in (YYYY-MM-DD): "), "%Y-%m-%d").date()
        check_out = datetime.strptime(input("Check-out (YYYY-MM-DD): "), "%Y-%m-%d").date()

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

def user_story_5():

    # Deletion for bookings will be changed later after testing creation of bookings
    try:
        user = int(input("Delete Booking ID: "))
        deletion = booking_dal.delete_booking(user)
        if not deletion:
            print("ID nicht gefunden")
        else:
            print("ID wurde gelöscht")
            return

    except Exception as e:
        print(f"Fehler: {e}")



def user_story_6():
    """Buchung stornieren"""
    try:
        bid = int(input("Buschung ID: "))
        booking = booking_dal.get_booking_by_id(bid)
        if not booking:
            print("Buchung nicht gefunden!")
            return
        #Prüfen, ob die Rechnung bereits storniert wurde
        if booking.is_cancelled:
            print("Buchung wurde bereits storniert.")
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

def user_story_8():
    """Alle Buchunge anzeigen (Admin)"""
    try:
        bookings = booking_manager.get_all_bookings()
        for b in bookings:
            print(booking_manager.get_booking_details(b))
    except Exception as e:
        print(f"Fehler: {e}")

# if __name__ == "__main__":
#     user_story_menu()