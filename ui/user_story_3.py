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


def user_story_3():
    while True:
        print("\n-- Hotelverwaltung (Admin) --")
        print("1. Hotel hinzufügen")
        print("2. Hotel entfernen")
        print("3. Hotel aktualisieren")
        print("4. Alle Hotels anzeigen")
        print("5. Zimmer zu Hotel hinzufügen")
        print("0. Zurück")
        choice = input("Wähle eine Option: ").strip()

        if choice == "0":
            break

        # Hotel hinzufügen
        elif choice == "1":
            print("\n--- Neues Hotel mit Adresse erstellen ---")

            name = input("Hotelname: ").strip()
            stars = int(input("Anzahl Sterne (1–5): ").strip())

            street = input("Strassenname inkl. Nr: ").strip()
            city = input("Stadt: ").strip()
            zip_code = input("PLZ: ").strip()

            new_address = Address(address_id=None,
                                  street=street,
                                  city=city,
                                  zip_code=zip_code)

            created_address = address_manager.create_address(new_address)

            hotel = Hotel(
                hotel_id=None,
                name=name,
                stars=stars,
                address=created_address
            )
            hotel_id = hotel_manager.create_hotel(hotel)
            print(f"\nHotel '{name}' wurde erfolgreich erstellt (ID: {hotel_id})")


        #Hotel entfernen
        elif choice == "2":
            # Alle Hotels abrufen und anzeigen
            hotels = hotel_manager.get_all_hotels()
            if not hotels:
                print("Keine Hotels vorhanden.")
                continue

            print("\nVerfügbare Hotels:")
            for h in hotels:
                print(f"  {h.hotel_id}: {h.name} ({h.stars} Sterne)")

            # Jetzt die ID abfragen
            hid = int(input("Hotel-ID zum Entfernen: ").strip())
            success = hotel_manager.delete_hotel(hid)
            print("Hotel entfernt." if success else "Hotel nicht gefunden.")

        # Hotel aktualisieren
        elif choice == "3":
            # Alle Hotels abrufen und anzeigen
            hotels = hotel_manager.get_all_hotels()
            if not hotels:
                print("Keine Hotels vorhanden.")
                continue

            print("\nVerfügbare Hotels:")
            for h in hotels:
                print(f"  {h.hotel_id}: {h.name} ({h.stars} Sterne)")

            # ID des zu aktualisierenden Hotels abfragen
            hid = int(input("Hotel-ID zum Aktualisieren: ").strip())
            hotel = next((h for h in hotels if h.hotel_id == hid), None)
            if not hotel:
                print("Hotel nicht gefunden.")
                continue

            # Neue Werte abfragen (Enter = unverändert)
            name_input = input(f"Neuer Name ({hotel.name}): ").strip()
            stars_input = input(f"Neue Sterne ({hotel.stars}): ").strip()


            # Adresse des bestehenden Hotels
            addr = hotel.address
            new_street = input(f"Neuer Strassenname inkl. Nr ({addr.street}): ").strip()
            new_city = input(f"Neue Stadt ({addr.city}): ").strip()
            new_zip = int(input(f"Neue PLZ ({addr.zip_code}): ").strip())

            # Aktualisieren des Address-Objekts
            updated_address = Address(
                address_id=addr.address_id,
                street=new_street,
                city=new_city,
                zip_code=new_zip
            )
            # Adresse in der DB updaten
            address_manager.update_address(updated_address)

            # Aktualisiertes Hotel-Objekt erstellen
            updated = Hotel(
                hotel_id=hid,
                name=name_input or hotel.name,
                stars=int(stars_input) if stars_input else hotel.stars,
                address=updated_address
            )

            # Update ausführen
            hotel_manager.update_hotel(updated)
            print("Hotelinformationen aktualisiert.")

        elif choice == "4":
            hotels = hotel_manager.get_all_hotels()
            if not hotels:
                print("Keine Hotels vorhanden.")
                continue
            print("\nVerfügbare Hotels:")
            for h in hotels:
                print(f"  {h.hotel_id}: {h.name} ({h.stars} Sterne) in {h.address.street} {h.address.zip_code} {h.address.city}")


        elif choice == "5":
            hotels = hotel_manager.get_all_hotels()
            if not hotels:
                print("Keine Hotels vorhanden.")
                continue

            print("\nVerfügbare Hotels:")
            for h in hotels:
                print(f"  {h.hotel_id}: {h.name} ({h.stars} Sterne)")

            try:
                hid = int(input("Hotel-ID zum Hinzufügen von Zimmern: ").strip())
            except ValueError:
                print("Ungültige Eingabe!")
                continue

            hotel = hotel_manager.find_by_id(hid)
            if not hotel:
                print("Hotel nicht gefunden.")
                continue

            room_number = input("Raumnummer eingeben: ").strip()
            if not room_number:
                print("Raumnummer darf nicht leer sein.")
                continue

        # Zimmertypen abfragen
            room_types = room_type_manager.get_all_room_types()
            print("\nVerfügbare Zimmertypen:")
            for t in room_types:
                print(f"  {t.type_id}: {t.description} (max {t.max_guests} Gäste)")

            try:
                rtid = int(input("Zimmertyp-ID auswählen: ").strip())
                price = float(input("Preis pro Nacht eingeben: ").strip())
            except ValueError:
                print("Ungültige Eingabe!")
                continue

        # Zimmer anlegen
            new_room = hotel_manager.add_room_to_hotel(hid, room_number, rtid, price)
            if new_room:
                print(f"Zimmer {new_room.room_id} ({new_room.room_number}) zum Hotel '{hotel.name}' hinzugefügt.")
            else:
                print("Fehler beim Anlegen des Zimmers.")
user_story_3()
