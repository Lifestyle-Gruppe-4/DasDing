from datetime import datetime
from datetime import timedelta
from model.booking import Booking

class Invoice:
    invoice_counter = 1

    def __init__(self, total_amount: float, booking: Booking):
        self.invoice_id = Invoice.invoice_counter
        Invoice.invoice_counter += 1

        self.total_amount =  total_amount
        self.issue_date = datetime.today()
        self.is_paid = False
        self.booking = booking

    def mark_as_paid(self):
        self.is_paid = True
        print(f"Invoice {self.invoice_id} is marked as paid.")

    def get_invoice_details(self) -> str:
        status = "Is Paid" if self.is_paid else "Payment Pending"
        return (f"Invoice ID: {self.invoice_id}, Amount: {self.total_amount:.2f} CHF, "
                f"Issue Date: {self.issue_date.isoformat()}, Status: {status}, Booking ID: {self.booking.booking_id}")

    def send_invoice_by_email(self, email_address: str):
        print(f"Invoice {self.invoice_id} is sent to email: {email_address}")

    def is_overdue(self) -> bool:
        due_date = self.issue_date + timedelta(days=14)
        return not self.is_paid and datetime.today() > due_date

    def apply_discount(self, percent: float):

        if percent < 0 or percent > 100:
            print("Invalid discount percent.")
            return

        if not self.is_paid:
            discount = self.total_amount * (percent / 100)
            self.total_amount -= discount
            print(f"Discount of {percent}% applied. \nNew Total: {self.total_amount:.2f} CHF")
        else:
            print("Cannot apply discount. Invoice already paid.")

    def get_invoice_summary(self) -> str:
        status = "Is Paid" if self.is_paid else "Payment Pending"
        return (f"[Invoice #{self.invoice_id}] Date: {self.issue_date} | Total: {self.total_amount:.2f} CHF | "
                  f"Status: {status} | Booking ID: {self.booking.booking_id}")

    def cancel_invoice(self):
        if self.is_paid:
            print("Invoice already paid. Cannot be cancelled")
        else:
            self.total_amount = 0
            print(f"Invoice {self.invoice_id} has been cancelled.")