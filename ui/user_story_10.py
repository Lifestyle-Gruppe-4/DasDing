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

def user_story_menu():
    """Hauptmenü zur Verwaltung von Zimmertypen, Preisen und Einrichtungen (Adminbereich)"""
    while True:
        print("\n --Stammdaten Verwalten (Admin)--")
        print("1. Zimmertypen anzeigen")
        print("2. Neuen Zimmertyp anlegen")
        print("3. Zimmertyp bearbeiten")
        print("4. Zimmertyp löschen")
        print("5. Zimmerpreis anzeigen")
        print("6. Zimmerpreis bearbeiten")
        print("7. Einrichtungen anzeigen")
        print("8. Neue Einrichtung hinzufügen")
        print("9. Einrichutng bearbeiten")
        print("10. Einrichtungen löschen")
        print("0. Exit")

        choice = input("Wählen Sie eine Option: ")

        if choice == "0":
            print("Auf Wiedersehen")
            break
        elif choice == "1":
            zimmertypen_anzeigen()
        elif choice == "2":
            zimmertyp_hinzufügen()
        elif choice == "3":
            zimmertyp_bearbeiten()
        elif choice == "4":
            zimmertyp_löschen()
        elif choice == "5":
            zimmerpreis_anzeigen()
        elif choice == "6":
            zimmerpreise_bearbeiten()
        elif choice == "7":
            facilities_anzeigen()
        elif choice == "8":
            facilities_hinzufügen()
        elif choice == "9":
            facilities_bearbeiten()
        elif choice == "10":
            facilities_entfernen()

# === Zimmertypen ===

def zimmertypen_anzeigen():
    """Zeigt alle vorhandenen Zimmtertypen mit Beschreibung und maximaler Gästeanzahl an"""
    types = room_type_manager.get_all_room_types()
    if not types:
        print("Keine Zimmertypen gefunden.")
    else:
        print("\nZimmertypen:")
        #Zeigt alle Zimmertypen an
        for rt in types:
            print(f"ID: {rt.type_id} | Beschreibung: {rt.description} | Max Gäste: {rt.max_guests}")

def zimmertyp_hinzufügen():
    """Erstellt einen neuen Zimmertyp anhand der Benutzereingaben"""
    try:
        desc = input("Beschreibung des Zimmertyps: ").strip()
        max_guests = int(input("Max. Gästeanzahl: "))
        # weist den neuen Zimmertyp einem neuen Objekt zu
        new_id = room_type_manager.create_room_type(desc, max_guests)
        print(f"Zimmertyp erstellt mit ID: {new_id}")
    except Exception as e:
        print(f"Fehler beim Erstellen: {e}")

def zimmertyp_bearbeiten():
    try:
        """Bearbeitet einen vorhandenen Zimmertyp anhand der ID"""
        rt_id = int(input("ID des zu bearbeitenden Zimmertyps: "))
        existing = room_type_manager.get_room_type_by_id(rt_id)
        if not existing:
            print("Zimmertyp nicht gefunden.")
            return
        #definiert die Inputs mit Anzeige von bisherigen Daten
        new_desc = input(f"Neue Beschreibung [{existing.description}]: ").strip() or existing.description
        new_guests = input(f"Neue Max. Gäste [{existing.max_guests}]: ").strip()
        new_guests = int(new_guests) if new_guests else existing.max_guests
        #fügt die neuen Daten dem Zimmertyp hinzu
        success = room_type_manager.update_room_type(rt_id, new_desc, new_guests)
        print("Zimmertyp erfolgreich aktualisiert." if success else "Aktualisierung fehlgeschlagen.")
    except Exception as e:
        print(f"Fehler beim Bearbeiten: {e}")

def zimmertyp_löschen():
    """Löscht einen Zimmertyp nach Eingabe der ID und Bestätigung"""
    try:
        rt_id = int(input("ID des zu löschenden Zimmertyps: "))
        if input("Sicher löschen? (j/n): ").lower() != 'j':
            print("Löschung abgebrochen.")
            return
        # löscht den gewählten Zimmertyp
        success = room_type_manager.delete_room_type(rt_id)
        print("Zimmertyp gelöscht." if success else "Löschen fehlgeschlagen.")
    except Exception as e:
        print(f"Fehler beim Löschen: {e}")

# === Zimmerpreise ===

def zimmerpreis_anzeigen():
    """Zeigt alle Zimmer mit akutellen Preis und zugehörigem Hotel"""
    # Zieht alle Zimmers
    rooms = room_manager.get_all_rooms()
    if not rooms:
        print("Keine Zimmer gefunden.")
    else:
        #Zeigt alle Zimmer der in der Liste an
        print("\nZimmerpreise:")
        for r in rooms:
            print(f"Zimmer-ID: {r.room_id} | Nummer: {r.room_number} | Preis: {r.price_per_night:.2f} CHF | Hotel: {r.hotel.name}")

def zimmerpreise_bearbeiten():
    """Ermöglicht die Bearbeitung des Zimmerpreises anhand der Zimmer-ID"""
    try:
        # Zieht gewünschtes Zimmer
        room_id = int(input("Zimmer-ID für Preisänderung: "))
        room = room_manager.get_room_by_id(room_id)
        if not room:
            print("Zimmer nicht gefunden.")
            return
        print(f"Aktueller Preis: {room.price_per_night:.2f} CHF")
        new_price = float(input("Neuer Preis pro Nacht: "))
        # übergibt dem Manager den neuen Preis für das Zimmer
        success = room_manager.update_room_price(room_id, new_price)
        print(f"Neuer Preis gespeichert: {new_price:.2f} CHF" if success else "Preisänderung fehlgeschlagen.")
    except Exception as e:
        print(f"Fehler beim Bearbeiten: {e}")

# === Einrichtungen ===

def facilities_anzeigen():
    #zieht alle Facilities aus der Liste
    facs = facility_manager.get_all_facilities()
    if not facs:
        print("Keine Einrichtungen gefunden.")
    else:
        print("\nEinrichtungen:")
        for fac in facs:
            print(f"ID: {fac.facility_id} | Name: {fac.facility_name}")

def facilities_hinzufügen():
    """Fügt eine neue Einrichtung hinzu"""
    try:
        name = input("Name der neuen Einrichtung: ").strip()
        # Übergibt neue Facility an den Manager und fügt diese hinzu
        new_id = facility_manager.create_facility(name)
        print(f"Einrichtung erstellt mit ID: {new_id}")
    except Exception as e:
        print(f"Fehler beim Erstellen: {e}")

def facilities_bearbeiten():
    """Bearbeitet den Namen einer vorhandenen Einrichtungen"""
    try:
        fac_id = int(input("ID der zu bearbeitenden Einrichtung: "))
        existing = facility_manager.find_by_id(fac_id)
        if not existing:
            print("Einrichtung nicht gefunden.")
            return
        new_name = input(f"Neuer Name [{existing.facility_name}]: ").strip() or existing.facility_name
        # neuer Name wird an Manager übergeben und updated
        success = facility_manager.update_facility(fac_id, new_name)
        print("Einrichtung erfolgreich aktualisiert." if success else "Aktualisierung fehlgeschlagen.")
    except Exception as e:
        print(f"Fehler beim Bearbeiten: {e}")

def facilities_entfernen():
    """Löscht eine Einrichtung nach Eingabe der ID und Bestätigung"""
    try:
        fac_id = int(input("ID der zu löschenden Einrichtung: "))
        if input("Sicher löschen? (j/n): ").lower() != 'j':
            print("Löschung abgebrochen.")
            return
        # Id der gewünschten Facility wird dem Manager zur löschung übergeben
        success = facility_manager.delete_facility(fac_id)
        print("Einrichtung gelöscht." if success else "Löschen fehlgeschlagen.")
    except Exception as e:
        print(f"Fehler beim Löschen: {e}")

user_story_menu()