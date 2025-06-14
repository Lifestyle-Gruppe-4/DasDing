

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


def alle_zimmer_anzeigen():
    # Liste aller Hotels anzeigen
    hotels = hotel_manager.get_all_hotels()
    if not hotels:
        print("Keine Hotels vorhanden")
        return
    print("\nAlle Hotels")
    for idx, hotel in enumerate(hotels, start=1):
        print(f"{idx}. Name: {hotel.name}, Adresse: {hotel.address.street}, {hotel.address.city}")

    # Hotel Auswahl für Zimmer
    try:
        choice = int(input("\nWählen Sie eine Hotel-Nummer für welches Sie die Zimmer sehen möchten: "))
    except ValueError:
        print("Ungültige Eingabe")
        return

    #Gewähltes Hotel ermitteln
    try:
        selected_hotel = hotels[choice-1]
    except IndexError:
        print("Kein Hotel mit dieser ID gefunden.")
        return

    #Zimmer laden
    rooms = selected_hotel.rooms

    #Ausgabe
    if not rooms:
        print(f"Kein Zimmer für Hotel '{selected_hotel.name}' gefunden.")
    else:
        print(f"\nAlle Zimmer in Hotel '{selected_hotel.name}':")
        for room in rooms:
            # Zieht aus dem Facility-Objekt nur den Namen
            if room.facilities:
                facility_names = ", ".join(f.facility_name for f in room.facilities)
            else:
                facility_names = "Keine Ausstattungen"

            print(f"Zimmernummer: {room.room_number}\n"
                  f"Typ: {room.room_type.description}\n"
                  f"Ausstattung: {facility_names}\n"
                  f"Preis/Nacht: {room.price_per_night:.2f} CHF\n")

alle_zimmer_anzeigen()


