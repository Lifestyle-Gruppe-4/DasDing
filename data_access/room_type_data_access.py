# data_access/room_type_dal.py

from model.room_type import RoomType
from data_access.base_data_access import BaseDataAccess

class RoomTypeDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def read_all_room_types(self) -> list[RoomType]:
        sql = """
        SELECT
            type_id,
            description,
            max_guests
        FROM Room_Type
        """
        rows = self.fetchall(sql)
        return [
            RoomType(
                room_type_id=row[0],
                description=row[1],
                max_guests=row[2]
            )
            for row in rows
        ]

    def create_room_type(self, rt: RoomType) -> int:
        sql = """
        INSERT INTO Room_Type(description, max_guests)
        VALUES (?, ?)
        """
        params = (rt.description, rt.max_guests)
        new_id, _ = self.execute(sql, params)
        return new_id

    def update_room_type(self, rt: RoomType) -> bool:
        sql = """
        UPDATE Room_Type
        SET description = ?, max_guests = ?
        WHERE type_id = ?
        """
        params = (rt.description, rt.max_guests, rt.room_type_id)
        _, rows_affected = self.execute(sql, params)
        return rows_affected > 0

    def delete_room_type(self, room_type_id: int) -> bool:
        sql = "DELETE FROM Room_Type WHERE type_id = ?"
        _, rows_affected = self.execute(sql, (room_type_id,))
        return rows_affected > 0


if __name__ == "__main__":
    # Beispiel für einen Schnelltest
    db_path = "../database/hotel_sample.db"
    dal = RoomTypeDataAccess(db_path)

    print("=== Alle RoomTypes ===")
    for rt in dal.read_all_room_types():
        print(rt)

    # Neu anlegen
    print("\n=== Erstelle neuen RoomType ===")
    temp = RoomType(room_type_id=0, description="TestTyp", max_guests=3)
    new_id = dal.create_room_type(temp)
    print(f"Neue ID: {new_id}")

    # Update
    print("\n=== Aktualisiere RoomType ===")
    updated = RoomType(room_type_id=new_id, description="TestTyp-Updated", max_guests=4)
    print("Erfolgreich geupdated?", dal.update_room_type(updated))

    # Löschen
    print("\n=== Lösche neuen RoomType ===")
    print("Erfolgreich gelöscht?", dal.delete_room_type(new_id))
