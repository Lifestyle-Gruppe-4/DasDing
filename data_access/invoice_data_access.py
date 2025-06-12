from data_access.base_data_access import BaseDataAccess
from model.invoice import Invoice
from data_access.booking_data_access import BookingDataAccess
from datetime import datetime

class InvoiceDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)
        self.booking_dal = BookingDataAccess(db_path) # Zugriff auf zugehörige Buchung

    # Holt alle Rechnungen aus der Datenbank
    def read_all_invoices(self) -> list[Invoice]:
        sql = """
            SELECT invoice_id, booking_id, total_amount, issue_date, is_paid
            FROM invoice
            ORDER BY invoice_id
        """
        rows = self.fetchall(sql)
        invoices = []
        for row in rows:
            inv = Invoice(
                invoice_id=row[0],
                booking=self.booking_dal.get_booking_by_id(row[1]),
                total_amount=row[2],
                issue_date=row[3],
                is_paid=bool(row[4]),
            )
            invoices.append(inv)
        return invoices

    # Neue Rechnung speichern
    def create_invoice(self, booking_id: int, total_amount: float, issue_date: datetime = None, is_paid: bool = False):
        if issue_date is None:
            issue_date = datetime.today().strftime('%Y-%m-%d')
        elif isinstance(issue_date, datetime):
            issue_date = issue_date.strftime('%Y-%m-%d')
        sql = """
            INSERT INTO invoice (booking_id, total_amount, issue_date, is_paid)
            VALUES (?, ?, ?, ?)
        """

        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(sql, (booking_id, total_amount, issue_date, int(is_paid)))
            conn.commit()
            return cursor.lastrowid

    # Bestehende Rechnung aktualisieren
    def update_invoice(self, invoice_id: int, total_amount: float, issue_date: datetime, is_paid: bool = False):
        sql = """
            UPDATE invoice
            SET total_amount = ?, issue_date = ?, is_paid = ?
            WHERE invoice_id = ?
            """
        return self.execute(sql, (total_amount, issue_date, int(is_paid), invoice_id))

    # Rechnung löschen
    def delete_invoice(self, invoice_id: int):
        sql = """
        DELETE FROM invoice WHERE invoice_id = ?
        """
        return self.execute(sql, (invoice_id,))

    # Holt eine Rechnung nach ihrer ID
    def get_invoice_by_id(self, invoice_id: int) -> Invoice | None:
        sql = """
            SELECT invoice_id,booking_id,total_amount, issue_date, is_paid
            FROM invoice
            WHERE invoice_id = ?
        """
        row = self.fetchone(sql, (invoice_id,))
        if not row:
            return None
        return Invoice(
            invoice_id=row[0],
            booking=self.booking_dal.get_booking_by_id(row[1]),
            total_amount = row[2],
            issue_date = row[3],
            is_paid = bool(row[4]),
        )





