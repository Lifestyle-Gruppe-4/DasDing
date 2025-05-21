from datetime import datetime

from model.hotel import Hotel
from model.room_type import RoomType
from model.facility import Facility


class Room:
    def __init__(self, room_id:int, room_nr:str, price_per_night:float, hotel:Hotel, room_type:RoomType, facility:Facility):
        self.room_id = room_id
        self.room_nr = room_nr
        self.price_per_night = price_per_night
        self.hotel = hotel
        self.room_type = room_type
        self.facility = facility

    def is_available(self, start_date:datetime, end_date:datetime):
        pass
class Room:
    def __init__(self, room_id: int, room_nr: str, price_per_night: float, hotel: Hotel, room_type: RoomType, facility: Facility):
        if not room_id:
            raise ValueError("Room ID is required")
        if not room_nr:
            raise ValueError("Room number is required")
        if price_per_night < 0:
            raise ValueError("Price per night must be non-negative")
        if not hotel:
            raise ValueError("Hotel is required")
        if not room_type:
            raise ValueError("Room type is required")
        if not facility:
            raise ValueError("Facility is required")

        self.__room_id = room_id
        self.__room_nr = room_nr
        self.__price_per_night = price_per_night
        self.__hotel = hotel
        self.__room_type = room_type
        self.__facility = facility
        self.__bookings = []  # List to store bookings for this room

    @property
    def room_id(self) -> int:
        return self.__room_id

    @property
    def room_nr(self) -> str:
        return self.__room_nr

    @property
    def price_per_night(self) -> float:
        return self.__price_per_night

    @property
    def hotel(self) -> Hotel:
        return self.__hotel

    @property
    def room_type(self) -> RoomType:
        return self.__room_type

    @property
    def facility(self) -> Facility:
        return self.__facility

    @property
    def bookings(self) -> list:
        return self.__bookings

    def add_booking(self, booking):
        self.__bookings.append(booking)

    def is_available(self, start_date: datetime, end_date: datetime) -> bool:
        for booking in self.__bookings:
            if not booking.is_cancelled:
                # Prüfen ob Zeiträume sich überschneiden
                if (start_date < booking.check_out_date and end_date > booking.check_in_date):
                    return False
        return True

    def __repr__(self):
        return (f"Room(ID: {self.room_id}, Nr: {self.room_nr}, Price: {self.price_per_night:.2f} CHF, "
                f"Type: {self.room_type.description}, Facility: {self.facility.facility_name}, "
                f"Hotel: {self.hotel.name})")




