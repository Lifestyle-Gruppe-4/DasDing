from datetime import datetime
from datetime import timedelta
from model.booking import Booking

class Invoice:
    def __init__(self,invoice_id:int,booking:Booking, total_amount: float, issue_date:datetime,is_paid: bool):
        # Automatisch vergebene Rechnungs-ID
        self.__invoice_id = invoice_id
        self.__booking = booking  # Zugehörige Buchung
        self.__total_amount =  total_amount # Rechnungsbetrag
        self.__issue_date = issue_date# Datum der Rechnungserstellung
        self.__is_paid = is_paid # Bezahlstatus

    # Getter/Setter für Eigenschaften (mit Validierungen)
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

    def __repr__(self):
        status = "Paid" if self.is_paid else "Unpaid"
        return (f"<Invoice #{self.invoice_id} | "
                f"Booking ID: {self.booking.booking_id} | "
                f"Amount: {self.total_amount:.2f} CHF | "
                f"Date: {self.issue_date} | "
                f"Status: {status}>")



    # Methode to use for testing

    # Setzt Rechnung als bezahlt
    def mark_as_paid(self):
        self.is_paid = True
        print(f"Invoice {self.invoice_id} is marked as paid.")

    # Gint alle Details zurück
    def get_invoice_details(self) -> str:
        status = "Is Paid" if self.is_paid else "Payment Pending"
        return (f"Invoice ID: {self.invoice_id}, Amount: {self.total_amount:.2f} CHF, "
                f"Issue Date: {self.issue_date.isoformat()}, Status: {status}, Booking ID: {self.booking.booking_id}")

    # "Versendet" die rechnung (Simulation über Print)
    def send_invoice_by_email(self, email_address: str):
        print(f"Invoice {self.invoice_id} is sent to email: {email_address}")

    # Prüft, ob die Rechnung überfällig ist
    def is_overdue(self) -> bool:
        due_date = self.issue_date + timedelta(days=14)
        return not self.is_paid and datetime.today() > due_date

    # Wendet Rabatt an (falls noch nicht bezahlt)
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

    # Gibt kurze Zusammenfassung der Rechnung
    def get_invoice_summary(self) -> str:
        status = "Is Paid" if self.is_paid else "Payment Pending"
        return (f"[Invoice #{self.invoice_id}] Date: {self.issue_date} | Total: {self.total_amount:.2f} CHF | "
                  f"Status: {status} | Booking ID: {self.booking.booking_id}")

    # Storniert unbezahlte Rechnung
    def cancel_invoice(self):
        if self.is_paid:
            print("Invoice already paid. Cannot be cancelled")
        else:
            self.total_amount = 0
            print(f"Invoice {self.invoice_id} has been cancelled.")