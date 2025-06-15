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

def print_booking_by_hotels(bookings):
    """Gruppert Buchungen nach Hotels und gibt diese aus"""
    grouped = {}
    for b in bookings:
        hid = b.room.hotel.hotel_id
        # Falls Hotel-ID noch nicht vorhanden ist, neuen Entrag anlegen.
        grouped.setdefault(hid, {"hotel": b.room.hotel, "bookings": []})["bookings"].append(b) #ChatGPT gefragt

    # Buchungen nach Hotel-ID sortiert ausgeben
    for hid in sorted(grouped):
        hotel = grouped[hid]["hotel"]
        print(f"Hotel-ID: {hid} | Name: {hotel.name}")
        for booking in grouped[hid]["bookings"]:
            print("   " + booking_manager.get_booking_details(booking))

def select_hotels():
    """Lässt den Benutzer Hotel-IDs auswählen und gibt die ausgewählte IDs zurück"""
    hotels = hotel_manager.get_all_hotels()
    if not hotels:
        print("Keine Hotels vorhanden.")
        return []

    # Liste verfügbare Hotels anzeigen
    print("\nVerfügbare Hotels: ")
    for h in hotels:
        print(f"{h.hotel_id}. {h.name}")

    # Eingabe von Hotel-IDs durch Benutzer
    ids = input("Von welche Hotels möchten Sie gerne die Buchungen sehen? (Hotel-IDs (kommagetrennt): ").split(",")
    selected = []
    for ident in ids:
        ident = ident.strip()
        if not ident:
            continue
        if not ident.isdigit():
            continue
        hid = int(ident)
        if any(h.hotel_id == hid for h in hotels):
            selected.append(hid)
        else:
            print(f"Hotel-ID: {hid} existiert nicht.")
    return selected

def user_story_8_menu():
    """Menü zur Anzeige von Buchungen nach Hotels (User Story 8)"""
    while True:
        print("\nWillkommen! Falls Sie ihre Buchungen überprüfen möchten, dann bitte die folgede Ausgaben ansehen:")
        print("\n-- Buchungsanzeige --")
        print("0 = Exit")
        print("1 = Alle Buchungen anzeigen")
        print("2 = Alle Buchungen nach Hotels")
        choice = input("Auswahl: ").strip()

        if choice == "0":
            print("Auf Wiedersehen!")
            break
        elif choice == "1":
            # Alle Buchungen abrufen und nach Hotels anzeigen
            print("\nHier ist eine Liste von Hotels mit alle ihre Buchungen:\n")
            bookings = booking_manager.get_all_bookings()
            print_booking_by_hotels(bookings)
        elif choice == "2":
            # Nur Buchungen von ausgewählten Hotels anzeigen
            selected = select_hotels()
            bookings = booking_manager.get_all_bookings()
            filtered = [b for b in bookings if b.room.hotel.hotel_id in selected]
            print_booking_by_hotels(filtered)
        else:
            print("Ungültige Eingabe.")

user_story_8_menu()


