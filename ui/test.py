#!/usr/bin/env python3
from data_access.room_data_access import RoomDataAccess
from data_access.hotel_data_access import HotelDataAccess

def list_hotels(db_path: str):
    room_dal  = RoomDataAccess(db_path)
    hotel_dal = HotelDataAccess(db_path, room_dal)
    hotels = hotel_dal.read_all_hotels()
    if not hotels:
        print("Keine Hotels gefunden.")
        return
    for h in hotels:
        addr = h.address  # Address-Objekt
        print(f"{h.hotel_id}: {h.name} ({h.stars} Sterne) – {addr.street}, {addr.city} {addr.zip_code}")

if __name__ == "__main__":
    DB_PATH = "../database/hotel_sample.db"
    list_hotels(DB_PATH)

#!/usr/bin/env python3
from data_access.address_data_access import AddressDataAccess
from business_logic.address_manager import AddressManager

def list_addresses(db_path: str):
    """
    Test-Skript, das alle Adressen aus der Datenbank liest und ausgibt.
    """
    address_dal     = AddressDataAccess(db_path)
    address_manager = AddressManager(address_dal)
    addresses       = address_manager.get_all_addresses()

    if not addresses:
        print("Keine Adressen gefunden.")
        return

    print("Alle Adressen:")
    for addr in addresses:
        # Model.Address hat property .zip für die Postleitzahl
        print(f"{addr.address_id}: {addr.street}, {addr.city} {addr.zip_code}")

if __name__ == "__main__":
    DB_PATH = "../database/hotel_sample.db"
    list_addresses(DB_PATH)
