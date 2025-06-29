from datetime import date

# Importiere alle Manager,DataAccess-Klassen und Models
from business_logic import AddressManager,BookingManager,FacilityManager,GuestManager,HotelManager,InvoiceManager,RoomManager,RoomTypeManager,ReviewManager
from data_access import AddressDataAccess,BookingDataAccess,FacilityDataAccess,GuestDataAccess,HotelDataAccess,InvoiceDataAccess,RoomDataAccess,RoomTypeDataAccess,ReviewDataAccess


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
review_dal = ReviewDataAccess(db_path)

# Intialisierung der Manager
address_manager = AddressManager(address_dal)
booking_manager = BookingManager(booking_dal)
facility_manager = FacilityManager(facility_dal)
guest_manager = GuestManager(guest_dal)
invoice_manager = InvoiceManager(invoice_dal)
room_manager = RoomManager(room_dal)
room_type_manager = RoomTypeManager(room_type_dal)
hotel_manager = HotelManager(hotel_dal)
review_manager = ReviewManager(review_dal)

def user_stroy_menu():
    while True:
        print("\n --User Stories--")
        print("1. Bewertungen lesen")
        print("2. Bewertung abgeben")
        print("0. Exit")

        choice = input("Wählen Sie eine Option: ")

        if choice == "0":
            print("Auf Wiedersehen")
            break
        elif choice == "1":
            bewertungen_lesen()
        elif choice == "2":
            bewertung_abgeben()
        else:
            print("Ungültige Eingabe. Bitte geben Sie eine Zahl von 1 bis 2 ein.")


def bewertung_abgeben():
    #Gast identifizieren
    first_name = input("Geben Sie Ihren Vornamen ein: ").lower().strip()
    last_name = input("Geben Sie Ihren Nachnamen ein: ").lower().strip()

    #Buchungen für diesen Gast holen
    all_bookings = booking_manager.get_bookings_by_guest(first_name,last_name)
    if not all_bookings:
        print(f"Keine Buchungen unter diesem Namen gefunden: {first_name} {last_name}")
        return

    # Prüfen ob Aufenthalt abgeschlossen
    past_bookings = [
        b for b in all_bookings if b.check_out_date < date.today()
    ]
    if not past_bookings:
        print(f"Sie haben aktuell keine abgeschlossenen Aufenthalt, die Sie bewerten könnten.")
        return

    # Liste Anzeigen
    print("\nIhre Buchungen:")
    for i,b in enumerate(past_bookings,1):
        hotel_name = b.room.hotel.name
        print(f"{i}, Buchungs ID {b.booking_id} - {hotel_name}: {b.check_in_date} bis {b.check_out_date}")

    # Auswahl treffen
    try:
        sel = int(input("Zu welcher Buchung möchten Sie eine Bewertung abgeben? (Nummer): "))
        booking = past_bookings[sel-1]
    except ValueError:
        print("Ungültige Auswahl")
        return

    # Hotelname erneut aus der Buchung ziehen
    hotel_name = booking.room.hotel.name

    # Rating abfragen
    try:
        rating = int(input("Wie zufrieden waren Sie mit Ihrem Aufenthalt? (1-5)").strip())
        if not 1<=rating<=5:
            raise ValueError
    except ValueError:
        print("Bitte eine ganze Zahl zwischen 1 und 5 eingeben.")
        return

    comment = input("Ihr Kommentar (optional): ")

    # Review speichern
    try:
        review_id = review_manager.add_review(booking.booking_id,rating,comment)
        print(f"\nDanke! Ihre Bewertung für IhrenAufenthalt vom "
              f"{booking.check_in_date} bis {booking.check_out_date} im {hotel_name} wurde gespeichert."
              f"(Review-ID: {review_id})")
    except Exception as e:
        print(f"Fehler beim Speichern der Bewertung: {e}")


def bewertungen_lesen():
    # Liste aller Hotels anzeigen
    hotels = hotel_manager.get_all_hotels()
    if not hotels:
        print("Keine Hotels vorhanden.")
        return

    print("\nVerfügbare Hotels:")
    for h in hotels:
        print(
            f"  {h.hotel_id}: {h.name} ({h.stars} Sterne) in {h.address.street} {h.address.zip_code} {h.address.city}")

    # Hotel Auswahl
    try:
        sel = int(input("Wählen Sie das Hotel, für welches Sie die Bewertungen sehen möchten (Nummer): ").strip())
    except ValueError:
        print("Ungültige Eingabe")
        return

    #ID prüfen
    hotel = next((h for h in hotels if h.hotel_id==sel), None)
    if not hotel:
        print("Keine Hotels gefunden.")
        return

    # Reviews holen
    reviews = review_manager.get_hotel_reviews(sel)
    if not reviews:
        print(f"Für '{hotel.name}' liegen noch keine Bewertungen vor.")
        return

    print(f"\nBewertungen für '{hotel.name}':")
    for r in reviews:
        print(f"Bewertung-Nr {r.review_id} - {r.rating} Sterne")
        if r.comment:
            print(f"Kommentar: {r.comment}")
        print(f"Erfasst am: {r.created_at}")

user_stroy_menu()