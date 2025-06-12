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

def user_story_10():
    """User Story 10: Stammdaten verwalten (Zimmertypen & Preise)"""
    while True:
        print("""
        === STAMMDATEN VERWALTEN (Admin) ===
        1. Zimmertypen anzeigen
        2. Neuen Zimmertyp anlegen
        3. Zimmertyp bearbeiten
        4. Zimmertyp löschen
        -------------------------------------
        5. Zimmerpreise anzeigen
        6. Zimmerpreis bearbeiten
        -------------------------------------
        0. Zurück
        """)
        choice = input("Wähle eine Option: ").strip()

        if choice == "0":
            print("Zurück zum Hauptmenü.")
            break

        elif choice == "1":
            types = room_type_manager.get_all_room_types()
            if not types:
                print("Keine Zimmertypen gefunden.")
            for rt in types:
                print(f"ID: {rt.room_type_id} | Beschreibung: {rt.description} | Max Gäste: {rt.max_guests}")

        elif choice == "2":
            try:
                desc = input("Beschreibung des Zimmertyps: ").strip()
                max_guests = int(input("Max. Gästeanzahl: "))
                new_id = room_type_manager.create_room_type(desc, max_guests)
                print(f"Zimmertyp erstellt mit ID: {new_id}")
            except Exception as e:
                print(f"Fehler: {e}")

        elif choice == "3":
            try:
                rt_id = int(input("ID des zu bearbeitenden Zimmertyps: "))
                existing = room_type_manager.get_room_type_by_id(rt_id)
                if not existing:
                    print("Zimmertyp nicht gefunden.")
                    continue
                new_desc = input(f"Neue Beschreibung [{existing.description}]: ").strip()
                new_guests = input(f"Neue max. Gäste [{existing.max_guests}]: ").strip()

                updated_desc = new_desc if new_desc else existing.description
                updated_guests = int(new_guests) if new_guests else existing.max_guests

                if room_type_manager.update_room_type(rt_id, updated_desc, updated_guests):
                    print("Zimmertyp erfolgreich aktualisiert.")
                else:
                    print("Aktualisierung fehlgeschlagen.")
            except Exception as e:
                print(f"Fehler: {e}")

        elif choice == "4":
            try:
                rt_id = int(input("ID zum Löschen: "))
                confirm = input("Sicher? (j/n): ").lower()
                if confirm != 'j':
                    continue
                if room_type_manager.delete_room_type(rt_id):
                    print("Zimmertyp gelöscht.")
                else:
                    print("Löschen fehlgeschlagen.")
            except Exception as e:
                print(f"Fehler: {e}")

        elif choice == "5":
            rooms = room_manager.get_all_rooms()
            if not rooms:
                print("Keine Zimmer gefunden.")
            for r in rooms:
                print(f"Zimmer-ID: {r.room_id} | Nummer: {r.room_number} | Preis: {r.price_per_night:.2f} CHF | Hotel: {r.hotel.name}")

        elif choice == "6":
            try:
                room_id = int(input("Zimmer-ID für Preisänderung: "))
                room = room_manager.get_room_by_id(room_id)
                if not room:
                    print("Zimmer nicht gefunden.")
                    continue
                print(f"Aktueller Preis: {room.price_per_night:.2f} CHF")
                new_price = float(input("Neuer Preis pro Nacht: "))
                room._Room__price_per_night = new_price  # Direktzugriff wegen fehlendem Setter
                print(f"Neuer Preis gesetzt: {new_price:.2f} CHF (⚠️ Achtung: Änderung ist nur im Objekt, nicht in DB!)")
                # TODO: Speichern in DB → update_room() in RoomDataAccess nötig
            except Exception as e:
                print(f"Fehler: {e}")

        else:
            print("Ungültige Auswahl.")

if __name__ == "__main__":
    user_story_10()
