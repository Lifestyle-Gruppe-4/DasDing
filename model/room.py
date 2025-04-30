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




