from datetime import date
from model.guest import Guest
from model.room import Room

class Booking:
    booking_counter = 1 #Zählt automatisch alle Buchungen (nur intern genutzt)

    def __init__(self, check_in_date: date, check_out_date: date, guest: Guest = None, room: Room = None, is_cancelled:bool = False, total_amount: float = 0, booking_id: int | None = None,):
        if booking_id is None:
            # Automatische vergebene Buchungs-ID
            self.__booking_id = Booking.booking_counter
            Booking.booking_counter += 1
        else:
            self.__booking_id = booking_id
            if booking_id >= Booking.booking_counter:
                Booking.booking_counter = booking_id + 1

        # Wichtige Buchungsdaten
        self.__check_in_date = check_in_date
        self.__check_out_date = check_out_date
        self.__guest = guest # Gast-Objekt
        self.__room = room # Zimmer-Objekt
        self.__is_cancelled = is_cancelled
        self.__total_amount = total_amount
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
        if not isinstance(value, date):
            raise ValueError('check_in_date must be a datetime')
        self.__check_in_date = value

    @property
    def check_out_date(self):
        return self.__check_out_date

    @check_out_date.setter
    def check_out_date(self, value):
        if not isinstance(value, date):
            raise ValueError('check_out_date must be a datetime')
        self.__check_out_date = value

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

    @total_amount.setter
    def total_amount(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("total_amount must be a positive number!")
        self.__total_amount = float(value)

    @property
    def invoice(self):
        return self.__invoice

    @invoice.setter
    def invoice(self, value):
        from model.invoice import Invoice
        if not isinstance(value, Invoice) and value is not None:
            raise ValueError('invoice must be an instance of Invoice or None!')
        self.__invoice = value


