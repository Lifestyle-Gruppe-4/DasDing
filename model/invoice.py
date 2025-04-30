from datetime import datetime
from model.booking import Booking



class Invoice:
    def __init__(self, invoice_id:int, issue_date:datetime, total_amount:float, booking:Booking, is_paid:bool):
        self.invoice_id = invoice_id
        self.issue_date = issue_date
        self.total_amount = total_amount
        self.booking = booking
        self.is_paid = is_paid

    def mark_as_paid(self):
        pass

