from datetime import datetime
from model.guest import Guest
from model.room import Room

class Booking:
    booking_counter = 1 #Zählt automatisch alle Buchungen (nur intern genutzt)

    def __init__(self, check_in_date: datetime, check_out_date: datetime, guest: Guest, room: Room):
        # Automatisch vergebene Buchungs-ID
        self.__booking_id = Booking.booking_counter
        Booking.booking_counter += 1

        # Wichtige Buchungsdaten
        self.__check_in_date = check_in_date
        self.__check_out_date = check_out_date
        self.__guest = guest # Gast-Objekt
        self.__room = room # Zimmer-Objekt
        self.__is_cancelled = False
        self.__total_amount = self.calculate_total_amount() # Preis berechnen
        self.__invoice = None # Rechnung (falls erstellt)

    # Getter/Setter für Datenfelder, mit Validierung
    @property
    def booking_id(self):
        return self.__booking_id

    @property
    def check_in_date(self):
        return self.__check_in_date

    @check_in_date.setter
    def check_in_date(self, value):
        if not isinstance(value, datetime):
            raise ValueError('check_in_date must be a datetime')
        self.__check_in_date = value
        self.__total_amount = self.calculate_total_amount()

    @property
    def check_out_date(self):
        return self.__check_out_date

    @check_out_date.setter
    def check_out_date(self, value):
        if not isinstance(value, datetime):
            raise ValueError('check_out_date must be a datetime')
        self.__check_out_date = value
        self.__total_amount = self.calculate_total_amount()

    @property
    def guest(self):
        return self.__guest

    @guest.setter
    def guest(self, value):
        if not isinstance(value, Guest):
            raise ValueError('Guest must be an instance of Guest!')
        self.__guest = value

    @property
    def room(self):
        return self.__room

    @room.setter
    def room(self, value):
        if not isinstance(value, Room):
            raise ValueError('Room must be an instance of Room!')
        self.__room = value
        self.__total_amount = self.calculate_total_amount()

    @property
    def is_cancelled(self):
        return self.__is_cancelled

    @is_cancelled.setter
    def is_cancelled(self, value):
        if not isinstance(value, bool):
            raise ValueError('is_cancelled must be a bool')
        self.__is_cancelled = value

    @property
    def total_amount(self):
        return self.__total_amount

    @property
    def invoice(self):
        return self.__invoice

    @invoice.setter
    def invoice(self, value):
        if not isinstance(value, Invoice) and value is not None:
            raise ValueError('invoice must be an instance of Invoice or None!')
        self.__invoice = value

#Methoden Liste

    # Gibt Buchungsinfo als String zurück
    def get_booking_details(self) -> str:
        booking_status = "Cancelled" if self.is_cancelled else "Active"
        return (f"Booking ID: {self.booking_id},  Guest: {self.guest.first_name} {self.guest.last_name} "
                f"Room: {self.room.room_nr}, From: {self.check_in_date}, to: {self.check_out_date} "
                f"Total: {self.total_amount} CHF, Status: {booking_status}")

    # Berechnet Preis: Anzahl Nächte x Zimmerpreis
    def calculate_total_amount(self) -> float:
        nights = (self.check_out_date - self.check_in_date).days
        if nights <= 0:
            raise ValueError("Booking must be at least 1 night.")
        return nights * self.room.price_per_night

    # Methoden für Buchungslogik
    def cancel_booking(self):
        self.is_cancelled = True
        print(f"Booking ID: {self.booking_id} has been cancelled.")

    def update_dates(self, new_check_in: datetime, new_check_out: datetime):
        if new_check_out < new_check_in:
            raise ValueError("Check-out must be the same or after check-in date!")
        self.check_in_date = new_check_in
        self.check_out_date = new_check_out
        self.__total_amount = self.calculate_total_amount()

    def generate_invoice(self):
        if not self.invoice:
            from model.invoice import Invoice # Lokale Import in der Methode
            self.invoice = Invoice(self.total_amount, self)
        return self.invoice

    def is_future_booking(self) -> bool:
        return self.check_in_date > datetime.now()

    def is_active_booking(self) -> bool:
        return self.check_in_date <= datetime.now() <= self.check_out_date and not self.is_cancelled

    def stay_duration(self) -> int:
        return (self.check_out_date - self.check_in_date).days

    def print_confirmation(self):
        print("------Booking Confirmation------")
        print(self.get_booking_details())
        print(f"Duration: {self.stay_duration()} Nights")
        print(f"Total: {self.total_amount} CHF")
        print("--------------------------------")
