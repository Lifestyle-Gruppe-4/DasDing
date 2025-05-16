from datetime import datetime
from datetime import timedelta
from model.booking import Booking

class Invoice:
    invoice_counter = 1

    def __init__(self, total_amount: float, booking: Booking):
        self.__invoice_id = Invoice.invoice_counter
        Invoice.invoice_counter += 1

        self.__total_amount =  total_amount
        self.__issue_date = datetime.today()
        self.__is_paid = False
        self.__booking = booking

    @property
    def invoice_id(self):
        return self.__invoice_id

    @property
    def total_amount(self):
        return self.__total_amount

    @total_amount.setter
    def total_amount(self, value):
        if self.__is_paid:
            raise ValueError("Cannot modify invoice after paid")
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Total amount must be a positive number.")
        self.__total_amount = value

    @property
    def issue_date(self):
        return self.__issue_date

    @property
    def is_paid(self):
        return self.__is_paid

    @is_paid.setter
    def is_paid(self, value):
        if not isinstance(value, bool):
            raise ValueError("IsPaid must be a boolean.")
        self.__is_paid = value

    @property
    def booking(self):
        return self.__booking


# Methode to use for testing
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