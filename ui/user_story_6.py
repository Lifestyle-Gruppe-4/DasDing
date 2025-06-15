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

def user_story_6():
    """Buchung stornieren"""
    try:
        # Übersicht aller Gäste, um User Story durchführen zu können
        print("\nVerfügbare Gäste:")
        for g in guest_manager.get_all_guests():
            print(f" {g.guest_id}. {g.first_name} {g.last_name}")

        # Eingabe des Namens zur Identifikation
        first_name = input("Vorname des Gastes: ").strip()
        last_name = input("Nachname des Gastes: ").strip()

        # Buchungen des Gastes abrufen
        bookings = booking_manager.get_bookings_by_guest(first_name,last_name)
        if not bookings:
            print("Keine Buchung zu diesem Namen gefunden.")
            return

        # Alle Buchungen anzeigen
        print("\nIhre Buchungen: ")
        for b in bookings:
            print(booking_manager.get_booking_details(b))

        # Benutzer wählt eine Buchungs-ID zur Stornierung
        try:
            bid = int(input("Geben Sie die Buchungs-ID ein, die Sie gerne stornieren möchten: "))
        except ValueError:
            print("Ungültig Eingabe.")
            return

        # Buchung über ID abrufen
        booking = booking_dal.get_booking_by_id(bid)
        if not booking:
            print("Buchung nicht gefunden!")
            return

        #Prüfen, ob die Buchung bereits storniert wurde
        if booking.is_cancelled:
            print("Buchung wurde bereits storniert.")
            return

        # Benutzer muss Stornierung bestätigen
        confirm = input("\nSoll diese Buchung storniert werden? (j/n) ")
        if confirm != 'j':
            print("Abbruch. Auf wiedersehen.")
            return

        # Markiere die Buchung als storniert
        booking_manager.booking_dal.execute(
            "Update Booking Set is_cancelled = 1 WHERE booking_id = ?", (bid,),
        )

        # Optionale Storno-Rechnungen erzeugen
        invoice_manager.create_invoice(bid, 0.0)
        print("Buchung storniert.")
    except Exception as e:
        print(f"Fehler: {e}")

def user_story_6_menu():
    """Menü zur Auswahl der Stornierungsfunktion (User Story 6)"""
    while True:
        print("\nGuten Tag - Sie möchten gerne ihre Buchung stornieren? \nBitte beachten Sie die folgende Überischt:")
        print("\n-- Optionen --")
        print("0 = Exit")
        print("1 = Buchung stornieren")

        choice = input("Wählen Sie eine Option (0/1): ").strip()

        if choice == "0":
            print("Auf Wiedersehen")
            break
        elif choice == "1":
            user_story_6()
        else:
            print("Ungültige Eingabe.")

user_story_6_menu()

