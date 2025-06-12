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

from data_access.room_data_access import RoomDataAccess

def user_story_9():
    try:
        # Zimmer aus der Datenbank laden
        rooms = room_dal.read_all_rooms()

        if not rooms:
            print("Keine Zimmer gefunden.")
            return

        print("\nZimmerliste mit Ausstattung:")
        for room in rooms:
            hotel_name    = room.hotel.name
            room_number   = room.room_number
            amenity_names = [f.facility_name for f in room.facilities] or []
            amenities_str = ", ".join(amenity_names) if amenity_names else "Keine Ausstattung vorhanden"
            print(f"{hotel_name} – Zimmer {room_number}: {amenities_str}")

    except Exception as e:
        print(f"Fehler: {e}")

if __name__ == "__main__":
    user_story_9()


