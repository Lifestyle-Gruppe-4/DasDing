#!/usr/bin/env python3
from data_access.address_data_access import AddressDataAccess
from data_access.room_data_access import RoomDataAccess
from data_access.hotel_data_access import HotelDataAccess

from model.address import Address
from model.hotel import Hotel

from business_logic.address_manager import AddressManager
from business_logic.hotel_manager import HotelManager

def user_story_3(db_path: str):
    """
    3. Hotels verwalten (Admin):
       3.1 Hotel hinzufügen (mit neuer oder bestehender Adresse)
       3.2 Hotel entfernen
       3.3 Hotelinformationen aktualisieren
    """
    # Data Access Layer
    room_dal    = RoomDataAccess(db_path)
    address_dal = AddressDataAccess(db_path)
    hotel_dal   = HotelDataAccess(db_path, room_dal)

    # Business Logic Layer
    address_manager = AddressManager(address_dal)
    hotel_manager   = HotelManager(hotel_dal)

    while True:
        print("\n-- Hotelverwaltung (Admin) --")
        print("1. Hotel hinzufügen")
        print("2. Hotel entfernen")
        print("3. Hotel aktualisieren")
        print("0. Zurück")
        choice = input("Wähle eine Option: ").strip()

        if choice == "0":
            break

        # 3.1 Hotel hinzufügen
        elif choice == "1":
            name  = input("Name des Hotels: ").strip()
            stars = int(input("Anzahl Sterne (1–5): ").strip())

            print("\n1. Neue Adresse erstellen")
            print("2. Bestehende Adresse auswählen")
            addr_choice = input("Wähle: ").strip()

            if addr_choice == "1":
                # neue Adresse anlegen
                street   = input("Strasse: ").strip()
                city     = input("Stadt: ").strip()
                zip_code = input("ZIP: ").strip()

                new_address = Address(
                    address_id=None,
                    street=street,
                    city=city,
                    zip_code=zip_code
                )
                address = address_manager.create_address(new_address)
                print(f"Neue Adresse angelegt (ID: {address.address_id})")

            else:
                # bestehende Adresse auswählen
                addresses = address_manager.get_all_addresses()
                if not addresses:
                    print("Keine Adressen vorhanden. Bitte zuerst eine neue Adresse anlegen.")
                    continue
                print("\nVerfügbare Adressen:")
                for a in addresses:
                    print(f"  {a.address_id}: {a.street}, {a.city} {a.zip_code}")
                sel_id = int(input("Adresse-ID auswählen: ").strip())
                address = address_manager.find_address_by_id(sel_id)
                if not address:
                    print("Ungültige Adresse-ID.")
                    continue

            # Hotel anlegen
            new_hotel = Hotel(
                hotel_id=None,
                name=name,
                stars=stars,
                address=address
            )
            hid = hotel_manager.create_hotel(new_hotel)
            print(f"Hotel erstellt. ID: {hid}")

        # 3.2 Hotel entfernen
        elif choice == "2":
            hid     = int(input("Hotel-ID zum Entfernen: ").strip())
            success = hotel_manager.delete_hotel(hid)
            print("Hotel entfernt." if success else "Hotel nicht gefunden.")

        # 3.3 Hotel aktualisieren
        elif choice == "3":
            hid    = int(input("Hotel-ID zum Aktualisieren: ").strip())
            hotels = hotel_manager.get_all_hotels()
            hotel  = next((h for h in hotels if h.hotel_id == hid), None)
            if not hotel:
                print("Hotel nicht gefunden.")
                continue

            name_input  = input(f"Neuer Name ({hotel.name}): ").strip()
            stars_input = input(f"Neue Sterne ({hotel.stars}): ").strip()

            updated = Hotel(
                hotel_id=hid,
                name   = name_input or hotel.name,
                stars  = int(stars_input) if stars_input else hotel.stars,
                address=hotel.address
            )
            hotel_manager.update_hotel(updated)
            print("Hotelinformationen aktualisiert.")

        else:
            print("Ungültige Auswahl.")

# if __name__ == "__main__":
#     DB_PATH = "../database/hotel_sample.db"
#     user_story_3(DB_PATH)
