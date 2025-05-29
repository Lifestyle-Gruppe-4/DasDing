from datetime import datetime

# Importiere alle Manager und DataAccess-Klassen
from business_logic.address_manager import AddressManager
from business_logic.booking_manager import BookingManager
from business_logic.facility_manager import FacilityManager
from business_logic.guest_manager import GuestManager
from business_logic.hotel_manager import HotelManager
from business_logic.invoice_manager import InvoiceManager
#from business_logic.room_manager import RoomManager
#from business_logic.room_type_manager import RoomTypeManager

from data_access.address_data_access import AddressDataAccess
from data_access.booking_data_access import BookingDataAccess
from data_access.facility_data_access import FacilityDataAccess
from data_access.guest_data_access import GuestDataAccess
from data_access.hotel_data_access import HotelDataAccess
from data_access.invoice_data_access import InvoiceDataAccess
from data_access.room_data_access import RoomDataAccess
from data_access.room_type_data_access import RoomTypeDataAccess

# Datenbankpfad und Initialisierung der DALs
db_path = "../database/hotel_sample.db"
address_dal = AddressDataAccess(db_path)
booking_dal = BookingDataAccess(db_path)
facility_dal = FacilityDataAccess(db_path)
guest_dal = GuestDataAccess(db_path)
hotel_dal = HotelDataAccess(db_path)
invoice_dal = InvoiceDataAccess(db_path)
room_dal = RoomDataAccess(db_path)
room_type_dal = RoomTypeDataAccess(db_path)

# Intialisierung der Manager
address_manager = AddressManager(address_dal)
booking_manager = BookingManager(booking_dal)
facility_manager = FacilityManager(facility_dal)
guest_manager = GuestManager(guest_dal)
invoice_manager = InvoiceManager(invoice_dal)
#room_manager = RoomManager(room_dal)
#room_type_manager = RoomTypeManager(room_type_dal)

# Platzhalter für weitere Funktionen gemäss Menue
def hotel_suchen(): pass
def zimmer_suchen(): pass
def buchung_erstellen(): pass
def buchung_verwalten(): pass
def rechnungen_verwalten(): pass
def hotel_verwalten(): pass
def zeige_dynamische_preise(): pass
def buchungen_anzeigen(): pass
def zimmerausstattung_anzeigen(): pass
def stammdaten_verwalten(): pass

def main_menu():
    while True:
        print("""
        ==== HOTELVERWALTUNGSSYSTEM ====
        1. Hotels nach Stadt/Sternen/Gästezahl anzeigen
        2. Verfügbare Zimmer suchen (nach Zeitraum und Gästezahl)
        3. Zimmer buchen
        4. Buchungen verwalten (anzeigen, ändern, stornieren)
        5. Rechnungen verwalten
        6. Hotelverwaltung (Admin)
        7. Dynamische Preisanzeige
        8. Buchungsübersicht (Admin)
        9. Zimmerausstattung anzeigen
        10. Stammdaten verwalten (Admin)
        11. Beenden
        """)

        choice = input("Wähle eine Option: ")
        if choice == "1":
            hotel_suchen()
        elif choice == "2":
            zimmer_suchen()
        elif choice == "3":
            buchung_erstellen()
        elif choice == "4":
            buchung_verwalten()
        elif choice == "5":
            rechnungen_verwalten()
        elif choice == "6":
            hotel_verwalten()
        elif choice == "7":
            zeige_dynamische_preise()
        elif choice == "8":
            buchungen_anzeigen()
        elif choice == "9":
            zimmerausstattung_anzeigen()
        elif choice == "10":
            stammdaten_verwalten()
        elif choice == "11":
            print("Programm beendet!")
            break
        else:
            print("Ungültige Eingabe!")
        pass

if __name__ == "__main__":
    main_menu()


