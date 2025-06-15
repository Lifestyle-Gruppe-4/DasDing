from datetime import datetime, date

# Importiere alle Manager,DataAccess-Klassen und Models
from business_logic import AddressManager,BookingManager,FacilityManager,GuestManager,HotelManager,InvoiceManager,RoomManager,RoomTypeManager,ReviewManager
from data_access import AddressDataAccess,BookingDataAccess,FacilityDataAccess,GuestDataAccess,HotelDataAccess,InvoiceDataAccess,RoomDataAccess,RoomTypeDataAccess,ReviewDataAccess

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
review_dal = ReviewDataAccess(db_path)

# Intialisierung der Manager
address_manager = AddressManager(address_dal)
booking_manager = BookingManager(booking_dal)
facility_manager = FacilityManager(facility_dal)
guest_manager = GuestManager(guest_dal)
invoice_manager = InvoiceManager(invoice_dal)
room_manager = RoomManager(room_dal)
room_type_manager = RoomTypeManager(room_type_dal)
hotel_manager = HotelManager(hotel_dal)
review_manager = ReviewManager(review_dal)


def user_stroy_menu():
    while True:
        print("\n --User Stories--")
        print("1. Alle Rechnungen Anzeigen")
        print("2. Rechnung als Bezahlt markieren")
        print("0. Exit")

        choice = input("Wählen Sie eine Option: ")

        if choice == "0":
            print("Auf Wiedersehen")
            break
        elif choice == "1":
            alle_rechnungen()
        elif choice == "2":
            rechnung_auf_paid()
        else:
            print("Ungültige Eingabe. Bitte geben Sie eine Zahl von 1 bis 2 ein.")


def alle_rechnungen():
    invoices = invoice_manager.get_all_invoices()
    for invoice in invoices:
        print(invoice)


def rechnung_auf_paid():
    # Alle Rechnungen holen und nur die unbezahlten filtern
    invoices = invoice_manager.get_all_invoices()
    unpaid_invoices = [invoice for invoice in invoices if invoice.is_paid == False]

    # Falls keine offenen Rechnungen, abbrechen
    if not unpaid_invoices:
        print("Keine offenen Rechnungen.")
        return

    # Offene Rechnungen anzeigen
    print("\nOffene Rechnungen:")
    for invoice in unpaid_invoices:
        # je nach Attribut-Namen:
        # print(f"ID: {inv.id} – Kunde: {inv.customer_name} – Betrag: {inv.amount}")
        print(invoice)

    # Eingabe einlesen und auf int prüfen
    try:
        invoice_id = int(input("Geben Sie die Rechnungs-ID ein: "))
    except ValueError:
        print("Ungültige Eingabe. Bitte geben Sie eine ganze Zahl ein.")
        return

    # Prüfen, ob die eingegebene ID in den unbezahlten Rechnungen vorkommt
    valid_ids = [invoice.invoice_id for invoice in unpaid_invoices]
    if invoice_id not in valid_ids:
        print("Ungültige Rechnungs-ID. Bitte wählen Sie eine der aufgelisteten offenen Rechnungen.")
        return

    # Rechnung als bezahlt markieren, mit Fehlerabfang
    try:
        invoice_manager.mark_invoice_as_paid(invoice_id)
    except Exception as e:
        print(f"Fehler beim Markieren als bezahlt: {e}")
        return

    # Bestätigung
    print(f"Rechnung mit ID {invoice_id} wurde erfolgreich als bezahlt markiert.")

user_stroy_menu()
