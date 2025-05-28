from datetime import datetime

from model.hotel import Hotel
from model.room_type import RoomType
from model.facility import Facility

class Room:
    def __init__(self, room_id: int, room_number: str, price_per_night: float, hotel_id: Hotel, room_type: RoomType, facilities: list[Facility]):
        if not room_id:
            raise ValueError("Room ID is required")
        if not room_number:
            raise ValueError("Room number is required")
        if price_per_night < 0:
            raise ValueError("Price per night must be non-negative")
        if not hotel_id:
            raise ValueError("Hotel is required")
        if not room_type:
            raise ValueError("Room type is required")
        if facilities is None:
            raise ValueError("Facility is required")

        self.__room_id = room_id
        self.__room_number = room_number
        self.__price_per_night = price_per_night
        self.__hotel_id = hotel_id
        self.__room_type = room_type
        self.__facilities = facilities
        self.__bookings = []  # List to store bookings for this room

    @property
    def room_id(self) -> int:
        return self.__room_id

    @property
    def room_number(self) -> str:
        return self.__room_number

    @property
    def price_per_night(self) -> float:
        return self.__price_per_night

    @property
    def hotel_id(self) -> Hotel:
        return self.__hotel_id

    @property
    def room_type(self) -> RoomType:
        return self.__room_type

    @property
    def facilities(self) -> list[Facility]:
        return self.__facilities

    @property
    def bookings(self) -> list:
        return self.__bookings

    def __repr__(self):
        facility_names = ','.join(f.facility_name for f in self.__facilities)
        return (f"Room(ID: {self.room_id}, Nr: {self.room_number}, Price: {self.price_per_night:.2f} CHF, "
                f"Type: {self.room_type.description}, Facilities: [{facility_names}], "
                f"Hotel: {self.hotel_id.name})")




