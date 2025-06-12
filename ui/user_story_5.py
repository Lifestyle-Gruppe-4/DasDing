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

### User Story 5
def rechnung_erstellen_nach_aufenthalt():
    try:
        # Alle Buchungen holen aus BookingManager
        bookings = booking_manager.get_all_bookings()
        # Filtert Buchungen die bereits vorbei sind
        past_bookings = [b for b in bookings if b.check_out_date < datetime.today().date() and not b.is_cancelled
                         and not invoice_manager.has_invoice_for_booking(b.booking_id)
                         ]
        if not past_bookings:
            print("Alle abgeschlossenen Buchungen wurden bereits abgerechnet.")
            return
        # Alle gültigen Buchungen werden mit fortlaufender Nummer angezeigt
        print("Abgeschlossene Buchungen:")
        for i, b in enumerate(past_bookings):
            print(f"{i + 1}. {BookingManager.get_booking_details(b)}")

        user_choice = int(input("Für welche Buchung soll eine Rechnung erstellt werden? (Nummer eingeben): "))
        if not (1 <= user_choice <= len(past_bookings)):
            print("Ungültige Auswahl.")
            return

        booking = past_bookings[user_choice - 1]

        # Rechnung erstellen
        invoice_id = invoice_manager.create_invoice(
            booking_id=booking.booking_id,
            total_amount=booking.total_amount
        )
        print(f"Rechnung erstellt! (Rechnungs-ID: {invoice_id})")

        invoice = invoice_manager.get_invoice_by_id(invoice_id)
        print(f" Es wurde folgende Rechnung erstellt:\n"
              f"{invoice}")


    except ValueError:
        print("Ungültige Eingabe.")
    except Exception as e:
        print(f"Fehler: {e}")

rechnung_erstellen_nach_aufenthalt()

def alle_rechnungen():
    invoices = invoice_manager.get_all_invoices()
    for invoice in invoices:
        print(invoice)
alle_rechnungen()

def rechnungen_löschen():
    invoices_id = int(input("ID: "))
    invoice_manager.delete_invoice(invoices_id)
#rechnungen_löschen()