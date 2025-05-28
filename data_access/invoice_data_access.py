from base_data_access import BaseDataAccess
from model.invoice import Invoice
from data_access.booking_data_access import BookingDataAccess
from datetime import datetime

class InvoiceDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)
        self.booking_dal = BookingDataAccess(db_path)

    def read_all_invoices(self) -> list[Invoice]:
        sql = """
            SELECT invoice_id, total_amount, issue_date, is_paid, booking_id
            FROM invoice
            ORDER BY invoice_id
        """
        rows = self.fetchall(sql)
        return [
            Invoice(
                total_amount = row[1],
                booking = self.booking_dal.get_booking_by_id(row[4])
            )
            for row in rows
        ]

    def get_invoice_by_id(self, invoice_id: int) -> Invoice | None:
        sql = """
            SELECT invoice_id, total_amount, issue_date, is_paid, booking_id
            FROM invoice
            WHERE invoice_id = ?
        """
        row = self.fetchone(sql, (invoice_id,))
        if not row:
            return None
        return Invoice(
            total_amount = row[1],
            booking = self.booking_dal.get_booking_by_id(row[4])
        )

    def create_invoice(self, booking_id: int, total_amount: float, issue_date: datetime = None, is_paid: bool = False):
        if issue_date is None:
            issue_date = datetime.today().isoformat()
        sql = """
            INSERT INTO invoice (booking_id, total_amount, issue_date, is_paid)
            VALUES (?, ?, ?, ?)
        """

        return self.execute(sql, (booking_id, total_amount, issue_date, int(is_paid)))

    def update_invoice(self, invoice_id: int, total_amount: float, issue_date: datetime, is_paid: bool = False):
        sql = """
            UPDATE invoice
            SET total_amount = ?, issue_date = ?, is_paid = ?
            WHERE invoice_id = ?
            """
        return self.execute(sql, (total_amount, issue_date, int(is_paid), invoice_id))

    def delete_invoice(self, invoice_id: int):
        sql = """
        DELETE FROM invoice WHERE invoice_id = ?
        """
        return self.execute(sql, (invoice_id,))




