from model.address import Address
from datetime import datetime


class Hotel:
    def __init__(self, hotel_id: int | None, name: str, stars: int, address: Address, rooms=None):
        if hotel_id is not None and hotel_id < 0:
            raise ValueError("Hotel ID must be positive if provided")
        if not name:
            raise ValueError("Name is required")
        if not stars:
            raise ValueError("Stars is required")
        if not address:
            raise ValueError("Address is required")

        self.__hotel_id:int = hotel_id
        self.__name = name
        self.__stars = stars
        self.__address = address
        self.__rooms = rooms or []

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



