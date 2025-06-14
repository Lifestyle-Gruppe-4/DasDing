from datetime import datetime

# Importiere alle Manager,DataAccess-Klassen und Models
from business_logic import AddressManager,BookingManager,FacilityManager,GuestManager,HotelManager,InvoiceManager,RoomManager,RoomTypeManager
from data_access import AddressDataAccess,BookingDataAccess,FacilityDataAccess,GuestDataAccess,HotelDataAccess,InvoiceDataAccess,RoomDataAccess,RoomTypeDataAccess
from model import booking

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

def user_stroy_menu():
    while True:
        print("\n --User Stories--")
        print("1. Alle Rechnungen Anzeigen")
        print("2. Rechnung Auslösen")
        print("3. Rechnung löschen")
        print("0. Exit")

        choice = input("Wählen Sie eine Option: ")

        if choice == "0":
            print("Auf Wiedersehen")
            break
        elif choice == "1":
            alle_rechnungen()
        elif choice == "2":
            rechnung_erstellen_nach_aufenthalt()
        elif choice == "3":
            rechnungen_entfernen()
        else:
            print("Ungültige Eingabe. Bitte geben Sie eine Zahl von 1 bis 4 ein.")

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

        try:
            user_choice = int(input("Für welche Buchung soll eine Rechnung erstellt werden? (Nummer eingeben) - Abbrechen -> 0: "))
        except ValueError:
            print("Ungültige Eingabe")
            return
        if user_choice == 0:
            print("Abbruch...")
            return
        # Prüfung ob es im Gültigen Bereich liegt
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


def rechnungen_entfernen():
    while True:
        user_input = input("Rechnungs-ID zum Löschen eingeben (oder '0' zum Abbrechen): ").strip()
        if user_input.lower() in ('q', 'quit', 'abbrechen', 'exit'):
            print("Vorgang abgebrochen.")
            return

        # Eingabe validieren
        try:
            invoices_id = int(user_input)
        except ValueError:
            print("Ungültige Eingabe: Bitte eine Zahl eingeben.")
            continue

        # Existenz prüfen
        invoice = invoice_manager.get_invoice_by_id(invoices_id)
        if invoice is None:
            print(f"Keine Rechnung mit der ID {invoices_id} gefunden.")
            continue

        # Vor dem Löschen anzeigen und bestätigen
        print("\nGefundene Rechnung:")
        print(invoice)  # nutzt __repr__
        confirm = input(f"Wirklich löschen? (j=Ja / n=Nein): ").strip().lower()
        if confirm not in ('j', 'ja'):
            print("Löschung abgebrochen.")
            return

        # Löschen und Ergebnis melden
        try:
            deleted = invoice_manager.delete_invoice(invoices_id)
            if deleted is False or (isinstance(deleted, int) and deleted == 0):
                print(f"Rechnung mit ID {invoices_id} konnte nicht gelöscht werden (nicht gefunden).")
            else:
                print(f"Rechnung mit ID {invoices_id} wurde erfolgreich gelöscht.")
        except Exception as e:
            print(f"Fehler beim Löschen der Rechnung: {e}")
        return

def alle_rechnungen():
    invoices = invoice_manager.get_all_invoices()
    for invoice in invoices:
        print(invoice)

user_stroy_menu()