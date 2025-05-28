from data_access.invoice_data_access import InvoiceDataAccess
from model.invoice import Invoice
from datetime import datetime

class InvoiceManager:
    def __init__(self, invoice_dal: InvoiceDataAccess):
        self.invoice_dal = invoice_dal

    def create_invoice(self, booking_id: int, total_amount: float) -> bool:
        issue_date = datetime.today()
        return self.invoice_dal.create_invoice(booking_id, total_amount, issue_date)

    def get_all_invoices(self) -> list[Invoice]:
        return self.invoice_dal.read_all_invoices()

    def get_invoice_by_id(self, invoice_id: int) -> Invoice | None:
        return self.invoice_dal.get_invoice_by_id(invoice_id)

    def mark_invoice_as_paid(self, invoice_id: int) -> bool:
        invoice = self.get_invoice_by_id(invoice_id)
        if not invoice:
            return False
        invoice.mark_as_paid()
        return self.invoice_dal.update_invoice(invoice_id, invoice.total_amount, invoice.issue_date, is_paid=True)

    def delete_invoice(self, invoice_id: int) -> bool:
        return self.invoice_dal.delete_invoice(invoice_id)

    def apply_discount(self, invoice_id: int, percent: float) -> bool:
        invoice = self.get_invoice_by_id(invoice_id)
        if not invoice:
            return False
        invoice.apply_discount(percent)
        return self.invoice_dal.update_invoice(invoice_id, invoice.total_amount, invoice.issue_date, invoice.is_paid)