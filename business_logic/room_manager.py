from data_access.room_data_access import RoomDataAccess
from model.room import Room


class RoomManager:
    def __init__(self, room_dal: RoomDataAccess):
        self.room_dal = room_dal

    def get_all_rooms(self) -> list[Room]:
        return self.room_dal.read_all_rooms()

    def get_room_by_id(self, room_id: int) -> Room:
        rooms = self.room_dal.read_all_rooms()
        for room in rooms:
            if room.room_id == room_id:
                return room
        return None

    def get_rooms_by_hotel_id(self, hotel_id: int) -> list[Room]:
        return self.room_dal.read_rooms_for_hotel(hotel_id)

    def get_room_by_max_guests(self, max_guests: int) -> list[Room]:
        rooms = self.room_dal.read_all_rooms()
        matching_rooms = [room for room in rooms if room.room_type.max_guests == max_guests]
        return matching_rooms

    def get_all_rooms_with_facilities(self) -> list[Room]:
        return self.room_dal.read_all_rooms_with_facilities()

    def calculate_seasonal_price(self, base_price, check_in_date):
        #Hochsaison im Sommer und Winter
        if check_in_date.month in (7,8,12,2):
            factor = 1.2
        #Nebensaison Frühling und Herbst
        elif check_in_date.month in (3,4,5,10,11):
            factor = 0.8
        #Restliche Monate wie Januar, Juni und September
        else:
            factor = 1.0
        season_price = base_price * factor
        return season_price, factor

    def create_room(self, hotel_id: int, type_id: int, price: float) -> Room:

        # Erzeuge ein Room-Objekt mit None als ID
        new_room = Room(
            room_id=None,
            hotel_id=hotel_id,
            type_id=type_id,
            price=price,
            bookings=[],  # noch keine Buchungen
            facilities=[]  # falls du Facilities später anhängen willst
        )
        # In DB speichern – room_dal.create_room() sollte die neue ID zurückliefern
        new_id = self.room_dal.create_room(new_room)
        # Objekt auslesen und zurückgeben
        return self.room_dal.read_room_by_id(new_id)

    def update_room_price(self, room_id: int, new_price: float) -> bool:
        #Validierung
        if new_price <= 0:
            raise ValueError("Der Preis muss größer als 0 sein.")

        #Delegation an den Data-Access
        success = self.room_dal.update_room_price(room_id, new_price)
        return success


