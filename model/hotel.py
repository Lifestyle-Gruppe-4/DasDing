from model.address import Address
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

    def __repr__(self):
        return f"Hotel ID: {self.hotel_id}, Name: {self.name}, Stars: {self.stars}, Address: {self.address} "

    @property
    def hotel_id(self):
        return self.__hotel_id

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name darf nicht leer sein")
        self.__name = value

    @property
    def stars(self):
        return self.__stars
    @stars.setter
    def stars(self, value):
        if not isinstance(value, int):
            raise TypeError("Sterne müssen eine ganze Zahl sein")
        if value < 1 or value > 5:
            raise ValueError("Sterne müssen zwischen 1 und 5 liegen")
        self.__stars = value

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, value):
        if not isinstance(value, Address):
            raise TypeError("Die Adresse muss ein Address-Objekt sein")
        self.__address = value

    @property
    def rooms(self):
        return self.__rooms

# #Räume hinzufügen
#     def add_room(self, room):
#         self.__rooms.append(room)
#
# #Räume löschen
#     def delete_room(self, room):
#         if room in self.__rooms:
#             self.__rooms.remove(room)
#
# #Verfügbare Räume anzeigen lassen
#     def get_available_rooms(self, start_date:datetime, end_date:datetime):
#         return  [room for room in self.__rooms if room.is_available(start_date, end_date)
#                  ]
# #Methoden von Thomas:
#     def get_rooms_by_stars(self, min_stars: int, max_stars: int) -> list['Room']:
#         if min_stars <= self.stars <= max_stars:
#             return self.rooms
#         else:
#             return []
#
#     def get_hotel_list(self):
#         return self.name, self.stars, self.address, self.rooms


#hotel = Hotel(hotel_id= 1,name= "Hotel Sunshine",stars= 4, address= addr1)
#print(hotel)



#hotel.add_room("Room 101")
#hotel.add_room("Room 102")

#print(hotel.rooms)


