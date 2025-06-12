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


# --- Datenbankpfad und Initialisierung der DALs ---
db_path = "../database/hotel_sample.db"
facility_dal   = FacilityDataAccess(db_path)
room_type_dal  = RoomTypeDataAccess(db_path)

# --- Initialisierung der Manager ---
facility_manager   = FacilityManager(facility_dal)
room_type_manager  = RoomTypeManager(room_type_dal)

from business_logic.room_type_manager import RoomTypeManager
from data_access.room_type_data_access import RoomTypeDataAccess

# Initialisierung DAL & Manager
db_path = "../database/hotel_sample.db"
room_type_dal = RoomTypeDataAccess(db_path)
room_type_manager = RoomTypeManager(room_type_dal)

def user_story_10():
    """User Story 10: Admin verwaltet Zimmertypen (Room Types)"""
    while True:
        print("""
        === STAMMDATEN: ZIMMERTYPEN VERWALTEN ===
        1. Alle Zimmertypen anzeigen
        2. Neuen Zimmertyp anlegen
        3. Bestehenden Zimmertyp bearbeiten
        4. Zimmertyp löschen
        0. Zurück
        """)
        choice = input("Wähle eine Option: ").strip()

        if choice == "0":
            print("Zurück zum Hauptmenü...")
            break

        elif choice == "1":
            room_types = room_type_manager.get_all_room_types()
            if not room_types:
                print("Keine Zimmertypen gefunden.")
            else:
                for rt in room_types:
                    print(f"ID: {rt.room_type_id}, Beschreibung: {rt.description}, Max. Gäste: {rt.max_guests}")

        elif choice == "2":
            try:
                description = input("Beschreibung des neuen Zimmertyps: ").strip()
                max_guests = int(input("Maximale Gästeanzahl: "))
                new_id = room_type_manager.create_room_type(description, max_guests)
                print(f"Zimmertyp wurde erfolgreich angelegt. Neue ID: {new_id}")
            except Exception as e:
                print(f"Fehler beim Anlegen: {e}")

        elif choice == "3":
            try:
                rt_id = int(input("ID des Zimmertyps, der bearbeitet werden soll: "))
                existing = room_type_manager.get_room_type_by_id(rt_id)
                if not existing:
                    print("Zimmertyp mit dieser ID wurde nicht gefunden.")
                    continue
                print(f"Aktuelle Beschreibung: {existing.description}, Max Gäste: {existing.max_guests}")
                new_description = input("Neue Beschreibung (Enter = unverändert): ").strip()
                new_max_guests = input("Neue max. Gästeanzahl (Enter = unverändert): ").strip()

                final_description = new_description if new_description else existing.description
                final_max_guests = int(new_max_guests) if new_max_guests else existing.max_guests

                success = room_type_manager.update_room_type(rt_id, final_description, final_max_guests)
                if success:
                    print("Zimmertyp wurde erfolgreich aktualisiert.")
                else:
                    print("Aktualisierung fehlgeschlagen.")
            except Exception as e:
                print(f"Fehler beim Aktualisieren: {e}")

        elif choice == "4":
            try:
                rt_id = int(input("ID des Zimmertyps, der gelöscht werden soll: "))
                confirmed = input("Bist du sicher? (j/n): ").lower()
                if confirmed != 'j':
                    print("Löschen abgebrochen.")
                    continue
                success = room_type_manager.delete_room_type(rt_id)
                if success:
                    print("Zimmertyp erfolgreich gelöscht.")
                else:
                    print("Löschen fehlgeschlagen.")
            except Exception as e:
                print(f"Fehler beim Löschen: {e}")

        else:
            print("Ungültige Eingabe. Bitte erneut versuchen.")

if __name__ == "__main__":
    user_story_10()
