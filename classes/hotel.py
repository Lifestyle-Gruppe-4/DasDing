from classes.address import Address
from classes.room import Room
from datetime import datetime

class Hotel:
    def __init__(self, hotel_id:int, name:str, stars:int, address:Address):
        self.hotel_id = hotel_id
        self.name = name
        self.stars = stars
        self.address = address
        self.rooms: list[Room] = []

    def add_room(self, room):
        self.rooms.append(room)

    def delete_room(self, room):
        pass
    # deletion process needs to be added

    def get_available_rooms(self, start_date: datetime, end_date: datetime) -> list['Room']:
        return [room for room in self.rooms if room.is_available(start_date, end_date)]

    def get_rooms_by_stars(self, min_stars: int, max_stars: int) -> list['Room']:
        if min_stars <= self.stars <= max_stars:
            return self.rooms
        else:
            return []

    def get_hotel_list(self):
        return self.name, self.stars, self.address, self.rooms
