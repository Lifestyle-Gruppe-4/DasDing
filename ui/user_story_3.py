# Importiere alle Manager,DataAccess-Klassen und Models
from business_logic import AddressManager,BookingManager,FacilityManager,GuestManager,HotelManager,InvoiceManager,RoomManager,RoomTypeManager
from data_access import AddressDataAccess,BookingDataAccess,FacilityDataAccess,GuestDataAccess,HotelDataAccess,InvoiceDataAccess,RoomDataAccess,RoomTypeDataAccess
from model import Address,Hotel

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
    """Hotelverwaltung: Hotels, Zimmer und Einrichtungen verwalten"""
    while True:
        print("\n-- Hotelverwaltung (Admin) --")
        print("1. Hotel hinzufügen")
        print("2. Hotel entfernen")
        print("3. Hotel aktualisieren")
        print("4. Alle Hotels anzeigen")
        print("5. Zimmer zu Hotel hinzufügen")
        print("6. Facilities zu Zimmer hinzufügen")
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

            # Adresse und Hotelobjekt erstellen
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

            # Neue Werte abfragen #TODO: Bestehende Werte müssen ebenfalls eingegeben Werten. Apassen das leere bleiben kann
            name_input = input(f"Neuer Name ({hotel.name}): ").strip()
            stars_input = input(f"Neue Sterne ({hotel.stars}): ").strip()


            # Adresse des bestehenden Hotels
            addr = hotel.address
            new_street = input(f"Neuer Strassenname inkl. Nr ({addr.street}): ").strip()
            new_city = input(f"Neue Stadt ({addr.city}): ").strip()
            new_zip = input(f"Neue PLZ ({addr.zip_code}): ").strip()

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

        # Alle Hotels anzeigen
        elif choice == "4":
            hotels = hotel_manager.get_all_hotels()
            if not hotels:
                print("Keine Hotels vorhanden.")
                continue
            print("\nVerfügbare Hotels:")
            for h in hotels:
                print(f"  {h.hotel_id}: {h.name} ({h.stars} Sterne) in {h.address.street} {h.address.zip_code} {h.address.city}")


        # Zimmer zu Hotel hinzufügen
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

                 #TODO: Keine prüfung ob Zimmernummer bereits besteht.
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

        # Zimmer anlegen #TODO: identische Zimmererstellung verhindern
            new_room = hotel_manager.add_room_to_hotel(hid, room_number, rtid, price)
            if new_room:
                print(f"\nDas Zimmer mit der ID: {new_room.room_id} wurde dem Hotel {hotel.name} hinzugefügt."
                      f"\nZimmernummer: {new_room.room_number}"
                      f"\nRaumtyp: {new_room.room_type.description}"
                      f"\nEinrichtungen: --")
            else:
                print("Fehler beim Anlegen des Zimmers.")


        # Einrichtungen zu Zimmer hinzufügen #TODO: Einrichtungen können zurzeit in Zimmer hinzugefügt werden, die nicht existieren. Anpassen
        elif choice == "6":
            hotels = hotel_manager.get_all_hotels()
            if not hotels:
                print("Keine Hotels vorhanden.")
                continue

            print("\nVerfügbare Hotels:")
            for h in hotels:
                print(f"  {h.hotel_id}: {h.name} ({h.stars} Sterne)")
            try:
                hid = int(input("Hotel-ID wählen: ").strip())
            except ValueError:
                print("Ungültige Eingabe.")
                continue

            rooms = room_manager.get_rooms_by_hotel_id(hid)
            if not rooms:
                print("Keine Zimmer für dieses Hotel vorhanden.")
                continue

            print("\nZimmer im Hotel:")
            for r in rooms:
                print(f"  {r.room_id}: Nr. {r.room_number}, {r.room_type.description} (max {r.room_type.max_guests} Gäste), {r.price_per_night} CHF")

            try:
                rid = int(input("Room-ID wählen: ").strip())
            except ValueError:
                print("Ungültige Eingabe.")
                continue

            all_facilities = facility_manager.get_all_facilities()
            print("\nVerfügbare Ausstattungen:")
            for f in all_facilities:
                print(f"  {f.facility_id}: {f.facility_name}")
            try:
                selected_ids = input("Facility-IDs (kommagetrennt, z.B. 1,3,5): ").strip()
                id_list = [int(fid.strip()) for fid in selected_ids.split(",") if fid.strip()]
            except ValueError:
                print("Ungültige Eingabe.")
                continue

            # Einrichtungen zuweisen #TODO: bestehende Facilities anzeigen
            for fid in id_list:
                success = facility_manager.assign_facility_to_room(rid, fid)
                if success:
                    print(f"Facility {fid} erfolgreich zugewiesen.")
                else:
                    print(f"Zuweisung von Facility {fid} fehlgeschlagen oder schon vorhanden.")
user_story_3()
