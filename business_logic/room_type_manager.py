from data_access.room_type_data_access import RoomTypeDataAccess
from model.room_type import RoomType


class RoomTypeManager:
    def __init__(self, room_type_dal: RoomTypeDataAccess):
        self.room_type_dal = room_type_dal

    def get_all_room_types(self) -> list[RoomType]:
        """Holt alle Zimmertypen aus der Datenbank"""
        return self.room_type_dal.read_all_room_types()

    def get_room_type_by_id(self, room_type_id: int) -> RoomType:
        """Sucht einen Zimmertyp anhand seiner ID"""
        room_types = self.room_type_dal.read_all_room_types()
        for room_type in room_types:
            if room_type.room_type_id == room_type_id:
                return room_type
        return None

    def create_room_type(self, description: str, max_guests: int) -> int:
        """Erstellt einen neuen Zimmertyp mit Validierung"""
        if max_guests <= 0:
            raise ValueError("Max guests must be greater than 0")
        if not description:
            raise ValueError("Description is required")

        new_room_type = RoomType(
            room_type_id=None,  # ID wird von der DB generiert
            description=description,
            max_guests=max_guests
        )
        return self.room_type_dal.create_room_type(new_room_type)

    def update_room_type(self, room_type_id: int, new_description: str, new_max_guests: int) -> bool:
        """Aktualisiert einen vorhandenen Zimmertyp"""
        if new_max_guests <= 0:
            raise ValueError("Max guests must be greater than 0")
        if not new_description:
            raise ValueError("Description is required")

        updated_room_type = RoomType(
            room_type_id=room_type_id,
            description=new_description,
            max_guests=new_max_guests
        )
        return self.room_type_dal.update_room_type(updated_room_type)

    def delete_room_type(self, room_type_id: int) -> bool:
        """Löscht einen Zimmertyp mit Existenzprüfung"""
        if not self.get_room_type_by_id(room_type_id):
            raise ValueError("Room type with this ID does not exist")
        return self.room_type_dal.delete_room_type(room_type_id)

    def get_room_types_by_guest_capacity(self, min_guests: int, max_guests: int) -> list[RoomType]:
        """Filtert Zimmertypen nach Gäste-Kapazität"""
        all_types = self.room_type_dal.read_all_room_types()
        return [
            rt for rt in all_types
            if min_guests <= rt.max_guests <= max_guests
        ]