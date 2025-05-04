from model.address import Address, addr1
from datetime import datetime


class Hotel:
    def __init__(self, hotel_id: int, name: str, stars: int, address: Address):
        if not hotel_id:
            raise ValueError("Address ID is required")
        if not name:
            raise ValueError("Street is required")
        if not stars:
            raise ValueError("City is required")
        if not address:
            raise ValueError("Zip is required")

        self.__hotel_id = hotel_id
        self.__name = name
        self.__stars = stars
        self.__address = address
        self.__rooms: list = []

    @property
    def hotel_id(self):
        return self.__hotel_id
    @property
    def name(self):
        return self.__name
    @property
    def stars(self):
        return self.__stars
    @property
    def address(self):
        return self.__address
    @property
    def rooms(self):
        return self.__rooms

    def __repr__(self):
        return f"Hotel ID: {self.hotel_id}, Name: {self.name}, Stars: {self.stars}, Address: {self.address} "

#Räume hinzufügen
    def add_room(self, room):
        self.__rooms.append(room)

#Räume löschen
    def delete_room(self, room):
        if room in self.__rooms:
            self.__rooms.remove(room)

#Verfügbare Räume anzeigen lassen
    def get_available_rooms(self, start_date:datetime, end_date:datetime):
        return  [room for room in self.__rooms if room.is_available(start_date, end_date)
                 ]
#Methoden von Thomas:
    def get_rooms_by_stars(self, min_stars: int, max_stars: int) -> list['Room']:
        if min_stars <= self.stars <= max_stars:
            return self.rooms
        else:
            return []

    def get_hotel_list(self):
        return self.name, self.stars, self.address, self.rooms


hotel = Hotel(hotel_id= 1,name= "Hotel Sunshine",stars= 4, address= addr1)
print(hotel)



hotel.add_room("Room 101")
hotel.add_room("Room 102")

print(hotel.rooms)


