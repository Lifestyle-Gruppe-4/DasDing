class RoomType:
    def __init__(self, room_type_id: int, description: str, max_guests: int):
        if not room_type_id:
            raise ValueError("RoomType ID is required")
        if not description:
            raise ValueError("Description is required")
        if max_guests <= 0:
            raise ValueError("Max guests must be greater than 0")

        self.__room_type_id = room_type_id
        self.__description = description
        self.__max_guests = max_guests

    @property
    def room_type_id(self) -> int:
        return self.__room_type_id

    @property
    def description(self) -> str:
        return self.__description

    @property
    def max_guests(self) -> int:
        return self.__max_guests

    def __repr__(self):
        return f"RoomType(ID: {self.room_type_id}, Description: {self.description}, Max Guests: {self.max_guests})"
