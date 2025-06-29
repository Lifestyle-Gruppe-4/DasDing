from data_access.hotel_data_access import HotelDataAccess
from model.hotel import Hotel
from model.room import Room
from datetime import date

class HotelManager:
    def __init__(self, hotel_dal: HotelDataAccess):
        self.hotel_dal = hotel_dal

    def get_all_hotels(self) -> list[Hotel]:
        return self.hotel_dal.read_all_hotels()

    def create_hotel(self, hotel: Hotel) -> int:
        return self.hotel_dal.create_hotel(hotel)

    def delete_hotel(self, hotel_id:int) -> bool:
        return self.hotel_dal.delete_hotel(hotel_id)

    def update_hotel(self, hotel: Hotel) -> bool:
        return self.hotel_dal.update_hotel(hotel)

    def find_by_id(self, hotel_id: int) -> Hotel:

        for hotel in self.hotel_dal.read_all_hotels():
            if hotel.hotel_id == hotel_id:
                return hotel
        return None

    def find_by_name(self, name:str) -> list[Hotel]:
        name = name.lower()
        return [
            hotel for hotel in self.hotel_dal.read_all_hotels()
            if hotel.name.lower() == name
        ]

    def find_by_city(self, city:str) -> list[Hotel]:
        city = city.lower()
        return [
            hotel for hotel in self.hotel_dal.read_all_hotels()
            if hotel.address.city.lower() == city
        ]

    def find_all_rooms_by_hotel(self,hotel:Hotel) -> list[Room]:
        return hotel.rooms

    def find_hotel_by_city_and_min_stars(self, city: str, stars: int) -> list[Hotel]:
        city = city.lower()
        stars = stars
        return [
            hotel for hotel in self.hotel_dal.read_all_hotels()
            if hotel.address.city.lower() == city and hotel.stars >= stars
        ]

    def find_hotels_with_matching_rooms(self, city: str, guests: int) -> list[tuple[Hotel, Room]]:
        city = city.lower()
        matches = []

        for hotel in self.hotel_dal.read_all_hotels():
            if hotel.address.city.lower() == city:
                for room in hotel.rooms:
                    if room.room_type.max_guests >= guests:
                        matches.append((hotel, room))
                        break

        return matches

    def find_available_hotels_by_date(self, city: str, check_in:date, check_out:date) -> list[tuple[Hotel, Room]]:
        available = []
        for hotel in self.hotel_dal.read_all_hotels():
            if hotel.address.city.lower() ==city.lower():
                for room in hotel.rooms:
                    #Any prüft ob eine Buchung in diesem Zeitraum liegt
                    overlaps = any(
                        b.check_in_date < check_out and b.check_out_date > check_in
                        for b in room.bookings
                        if not b.is_cancelled
                    )
                    if not overlaps:
                        available.append((hotel, room))
                        break
        return available

    def find_available_hotels_by_date_guest_stars(self, city: str, check_in:date, check_out:date, guests:int, stars:int) -> list[tuple[Hotel, Room]]:
        available = []
        for hotel in self.hotel_dal.read_all_hotels():
            if hotel.address.city.lower() == city.lower():
                if hotel.stars >= stars:
                    for room in hotel.rooms:
                        if room.room_type.max_guests >= guests:
                            #Any prüft ob eine Buchung in diesem Zeitraum liegt
                            overlaps = any(
                                b.check_in_date < check_out and b.check_out_date > check_in
                                for b in room.bookings
                                if not b.is_cancelled
                            )
                            if not overlaps:
                                available.append((hotel, room))
                                break
        return available

    def find_available_rooms_by_hotel_and_date(self,hotel:Hotel,check_in:date,check_out:date) -> list[Room]:
        available = []
        for room in hotel.rooms:
            overlaps = any(b.check_in_date < check_out and b.check_out_date > check_in and not b.is_cancelled for b in room.bookings)
            if not overlaps:
                available.append(room)
        return available

    def add_room_to_hotel(self,hotel_id: int,room_number:str, type_id: int, price_per_night: float) -> Room:
        # Zuerst prüfen, ob das Hotel existiert
        hotel = self.find_by_id(hotel_id)
        if not hotel:
            return None

        new_room_id = self.hotel_dal.create_room_for_hotel(
            hotel_id,
            room_number,
            type_id,
            price_per_night
        )
        return self.hotel_dal.read_room_by_id(new_room_id)
