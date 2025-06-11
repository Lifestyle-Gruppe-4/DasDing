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

def user_story_10():
    """
    User Story 10 (Admin Stammdaten-Verwaltung):
    Verwaltung von Zimmertypen und Einrichtungen (CRUD).
    """
    while True:
        print("""
        === STAMMDATEN VERWALTEN (Admin) ===
        1. Zimmertypen anzeigen
        2. Zimmertyp anlegen
        3. Zimmertyp aktualisieren
        4. Zimmertyp löschen
        -----------------------------------
        5. Einrichtungen anzeigen
        6. Einrichtung anlegen
        7. Einrichtung aktualisieren
        8. Einrichtung löschen
        -----------------------------------
        0. Zurück
        """)
        choice = input("Wähle eine Option: ").strip()
        if choice == "0":
            break

        # --- Zimmertypen ---
        if choice == "1":
            types = room_type_manager.get_all_room_types()
            for t in types:
                print(f"{t.room_type_id}: {t.description}, max Gäste: {t.max_guests}")

        elif choice == "2":
            name = input("Name des neuen Zimmertyps: ").strip()
            max_guests = int(input("Maximale Gästezahl: "))
            price = float(input("Preis pro Nacht: "))
            rt_id = room_type_manager.create_room_type(name, max_guests, price)
            print(f"Neuer Zimmertyp angelegt mit ID {rt_id}")

        elif choice == "3":
            rt_id = int(input("ID des Zimmertyps, der geändert werden soll: "))
            # Holen des aktuellen Objekts
            rt = room_type_manager.get_room_type_by_id(rt_id)
            if not rt:
                print("Zimmertyp nicht gefunden.")
                continue
            # Neue Werte (Leereingabe = unverändert)
            new_name = input(f"Neuer Name [{rt.name}]: ").strip() or rt.name
            new_max = input(f"Neue max. Gäste [{rt.max_guests}]: ").strip()
            new_price = input(f"Neuer Preis/Nacht [{rt.price_per_night:.2f}]: ").strip()
            room_type_manager.update_room_type(
                rt_id,
                name=new_name,
                max_guests=int(new_max) if new_max else rt.max_guests,
                price_per_night=float(new_price) if new_price else rt.price_per_night
            )
            print("Zimmertyp erfolgreich aktualisiert.")

        elif choice == "4":
            rt_id = int(input("ID des Zimmertyps, der gelöscht werden soll: "))
            room_type_manager.delete_room_type(rt_id)
            print("Zimmertyp gelöscht.")

        # --- Einrichtungen ---
        elif choice == "5":
            facs = facility_manager.get_all_facilities()
            for f in facs:
                print(f"{f.facility_id}: {f.facility_name}")

        elif choice == "6":
            name = input("Name der neuen Einrichtung: ").strip()
            f_id = facility_manager.create_facility(name)
            print(f"Neue Einrichtung angelegt mit ID {f_id}")

        elif choice == "7":
            f_id = int(input("ID der Einrichtung, die geändert werden soll: "))
            fac = facility_manager.get_facility_by_id(f_id)
            if not fac:
                print("Einrichtung nicht gefunden.")
                continue
            new_name = input(f"Neuer Name [{fac.facility_name}]: ").strip() or fac.facility_name
            facility_manager.update_facility(f_id, facility_name=new_name)
            print("Einrichtung erfolgreich aktualisiert.")

        elif choice == "8":
            f_id = int(input("ID der Einrichtung, die gelöscht werden soll: "))
            facility_manager.delete_facility(f_id)
            print("Einrichtung gelöscht.")

        else:
            print("Ungültige Auswahl. Bitte erneut versuchen.")

if __name__ == "__main__":
    user_story_10()
