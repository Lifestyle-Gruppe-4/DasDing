from data_access.room_type_data_access import RoomTypeDataAccess


class RoomTypeManager:
    def __init__(self, room_type_dal: RoomTypeDataAccess):
        self.room_type_dal = room_type_dal
