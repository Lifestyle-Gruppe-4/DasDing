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

    def get_room_by_max_guests(self, max_guests: int) -> list[Room]:
        rooms = self.room_dal.read_all_rooms()
        matching_rooms = [room for room in rooms if room.room_type.max_guests == max_guests]
        return matching_rooms

    def get_all_rooms_with_facilities(self) -> list[Room]:
        return self.room_dal.read_all_rooms_with_facilities()

    def calculate_seasonal_price(self, base_price, check_in_date):
        if check_in_date.month in (6,7,8,):
            factor = 1.2
        elif check_in_date.month in (11,12,1,2):
            factor = 0.8
        else:
            factor = 1.0
        season_price = base_price * factor
        return season_price, factor
