from datetime import datetime, date

# Importiere alle Manager,DataAccess-Klassen und Models
from business_logic import AddressManager,BookingManager,FacilityManager,GuestManager,HotelManager,InvoiceManager,RoomManager,RoomTypeManager,ReviewManager
from data_access import AddressDataAccess,BookingDataAccess,FacilityDataAccess,GuestDataAccess,HotelDataAccess,InvoiceDataAccess,RoomDataAccess,RoomTypeDataAccess,ReviewDataAccess
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

def bewertung_abgeben():
    #Gast identifizieren
    first_name = input("Geben Sie Ihren Vornamen ein: ").lower().strip()
    last_name = input("Geben Sie Ihren Nachnamen ein: ").lower().strip()

    #Buchungen für diesen Gast holen
    bookings = booking_manager.get_bookings_by_guest(first_name,last_name)
    if not bookings:
        print(f"Keine Buchungen unter diesem Namen gefunden: {first_name} {last_name}")
        return
    # Liste Anzeigen
    print("\nIhre Buchungen:")
    for i,b in enumerate(bookings,1):
        hotel_name = b.room.hotel.name
        print(f"{i}, Buchungs ID {b.booking_id} - {hotel_name}: {b.check_in_date} bis {b.check_out_date}")

    # Auswahl treffen
    try:
        sel = int(input("Zu welcher Buchung möchten Sie eine Bewertung abgeben? (Nummer): "))
        booking = bookings[sel-1]
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

#bewertung_abgeben()

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
        sel = int(input("Wählen Sie das Hotel, für welches Sie die Bewrtungen sehen möchten (Nummer): ").strip())
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
        print(f"Review-ID {r.review_id}: Buchung {r.booking_id} - {r.rating} Sterne")
        if r.comment:
            print(f"Kommentar: {r.comment}")
        print(f"Erfasst am: {r.created_at}")

bewertungen_lesen()