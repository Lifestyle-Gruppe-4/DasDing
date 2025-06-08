from data_access.invoice_data_access import InvoiceDataAccess
from model.invoice import Invoice
from datetime import date

class InvoiceManager:
    def __init__(self, invoice_dal: InvoiceDataAccess):
        self.invoice_dal = invoice_dal # Verbindung zur Datenbankschicht

    # Neue Rechnung mit heutigem Datum anlegen
    def create_invoice(self, booking_id: int, total_amount: float) -> int:
        issue_date = date.today().strftime('%Y-%m-%d')
        return self.invoice_dal.create_invoice(booking_id, total_amount, issue_date)

    # Gibt alle Rechnungen zurück
    def get_all_invoices(self) -> list[Invoice]:
        return self.invoice_dal.read_all_invoices()

    # Gibt eine einzelnere Rechnung zurück
    def get_invoice_by_id(self, invoice_id: int) -> Invoice | None:
        return self.invoice_dal.get_invoice_by_id(invoice_id)

    # Markiert eine Rechnung als bezahlt
    def mark_invoice_as_paid(self, invoice_id: int) -> bool:
        invoice = self.get_invoice_by_id(invoice_id)
        if not invoice:
            return False
        invoice.mark_as_paid()
        return self.invoice_dal.update_invoice(invoice_id, invoice.total_amount, invoice.issue_date, is_paid=True)

    # Rechnung löschen
    def delete_invoice(self, invoice_id: int) -> bool:
        return self.invoice_dal.delete_invoice(invoice_id)

    # Rabatt auf Rechnung anwenden
    def apply_discount(self, invoice_id: int, percent: float) -> bool:
        invoice = self.get_invoice_by_id(invoice_id)
        if not invoice:
            return False
        invoice.apply_discount(percent)
        return self.invoice_dal.update_invoice(invoice_id, invoice.total_amount, invoice.issue_date, invoice.is_paid)

    def has_invoice_for_booking(self, booking_id:int) -> bool:
        invoices = self.get_all_invoices()
        return any(inv.booking.booking_id == booking_id for inv in invoices)