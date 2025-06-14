class RoomType:
    def __init__(self, type_id: int, description: str, max_guests: int):
        if type_id is not None and type_id <= 0:
            raise ValueError("RoomType ID must be positive or None")
        if not description:
            raise ValueError("Description is required")
        if max_guests <= 0:
            raise ValueError("Max guests must be greater than 0")

        self.__type_id = type_id
        self.__description = description
        self.__max_guests = max_guests

    @property
    def type_id(self) -> int:
        return self.__type_id

    @property
    def description(self) -> str:
        return self.__description

    @property
    def max_guests(self) -> int:
        return self.__max_guests

    def __repr__(self):
        return f"RoomType(ID: {self.type_id}, Description: {self.description}, Max Guests: {self.max_guests})"
