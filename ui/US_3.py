#!/usr/bin/env python3
from types import SimpleNamespace

from data_access.address_data_access import AddressDataAccess
from data_access.room_data_access import RoomDataAccess
from data_access.hotel_data_access import HotelDataAccess

from model.hotel import Hotel

from business_logic.hotel_manager import HotelManager
from business_logic.address_manager import AddressManager

def user_story_3(db_path: str):
    """3. Hotels verwalten (Admin):
       3.1 Hotel hinzufügen (mit neuer oder bestehender Adresse)
       3.2 Hotel entfernen
       3.3 Hotelinformationen aktualisieren"""
    # Data Access Layer
    room_dal    = RoomDataAccess(db_path)
    address_dal = AddressDataAccess(db_path)
    hotel_dal   = HotelDataAccess(db_path, room_dal)
    # Business Logic
    hotel_manager   = HotelManager(hotel_dal)
    address_manager = AddressManager(address_dal)

    while True:
        print("\n-- Hotelverwaltung (Admin) --")
        print("1. Hotel hinzufügen")
        print("2. Hotel entfernen")
        print("3. Hotel aktualisieren")
        print("0. Zurück")
        choice = input("Wähle eine Option: ").strip()

        if choice == "0":
            break

        elif choice == "1":
            # --- Hotel anlegen ---
            name  = input("Name des Hotels: ").strip()
            stars = int(input("Anzahl Sterne (1–5): ").strip())

            # Adresse auswählen oder neu anlegen
            print("\n1. Neue Adresse erstellen")
            print("2. Vorhandene Adresse auswählen")
            addr_choice = input("Wähle: ").strip()

            if addr_choice == "1":
                # Neue Adresse anlegen: wir bauen ein einfaches Objekt mit street, city, zip_code
                street   = input("Strasse: ").strip()
                city     = input("Stadt: ").strip()
                zip_code = input("ZIP: ").strip()

                temp_addr = SimpleNamespace(
                    street=street,
                    city=city,
                    zip_code=zip_code
                )
                # AddressManager.create_address erwartet genau ein Objekt mit street, city, zip_code
                addr_id = address_manager.create_address(temp_addr)
                # echte Address-Instanz holen
                address = address_dal.read_address_by_id(addr_id)
                print(f"Neue Adresse angelegt (ID: {addr_id}).")

            else:
                # Bestehende Adresse auswählen
                print("\nVerfügbare Adressen:")
                addresses = address_dal.read_all_addresses()
                for addr in addresses:
                    # Address-Model hat property .zip
                    print(f"  {addr.address_id}: {addr.street}, {addr.city} {addr.zip}")
                addr_id = int(input("Adresse-ID auswählen: ").strip())
                address = next((a for a in addresses if a.address_id == addr_id), None)
                if not address:
                    print("Ungültige Adresse-ID. Abbruch.")
                    continue

            # Hotel-Domain-Objekt erzeugen und speichern
            new_hotel = Hotel(
                hotel_id=None,
                name=name,
                stars=stars,
                address=address
            )
            hotel_id = hotel_manager.create_hotel(new_hotel)
            print(f"Hotel erstellt. Hotel-ID: {hotel_id}")

        elif choice == "2":
            # --- Hotel löschen ---
            hid     = int(input("Hotel-ID zum Entfernen: ").strip())
            success = hotel_manager.delete_hotel(hid)
            print("Hotel entfernt." if success else "Hotel nicht gefunden.")

        elif choice == "3":
            # --- Hotel aktualisieren ---
            hid    = int(input("Hotel-ID zum Aktualisieren: ").strip())
            hotels = hotel_dal.read_all_hotels()
            hotel  = next((h for h in hotels if h.hotel_id == hid), None)
            if not hotel:
                print("Hotel nicht gefunden.")
                continue

            name_input  = input(f"Neuer Name ({hotel.name}): ").strip()
            stars_input = input(f"Neue Sterne ({hotel.stars}): ").strip()

            name  = name_input or hotel.name
            stars = int(stars_input) if stars_input else hotel.stars

            updated = Hotel(
                hotel_id=hid,
                name=name,
                stars=stars,
                address=hotel.address
            )
            hotel_manager.hotel_dal.update_hotel(updated)
            print("Hotelinformationen aktualisiert.")

        else:
            print("Ungültige Auswahl.")

# if __name__ == "__main__":
#     DB_PATH = "../database/hotel_sample.db"
#     user_story_3(DB_PATH)
