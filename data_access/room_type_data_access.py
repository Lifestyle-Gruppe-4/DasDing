

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
                type_id=row[0],
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
        lastrowid, _ = self.execute(sql,(rt.description,rt.max_guests))
        return lastrowid

    def update_room_type(self, type_id:int, description:str,max_guests:int) -> bool:
        sql = """
        UPDATE Room_Type
        SET description = ?, max_guests = ?
        WHERE type_id = ?
        """
        _, rows_affected = self.execute(sql,(description,max_guests,type_id))
        return rows_affected > 0

    def delete_room_type(self, type_id: int) -> bool:
        sql = "DELETE FROM Room_Type WHERE type_id = ?"
        _, rows_affected = self.execute(sql, (type_id,))
        return rows_affected > 0

    def read_room_type_by_id(self, type_id: int) -> RoomType:
        sql = """
              SELECT type_id, description, max_guests
              FROM Room_Type
              WHERE type_id = ?
              """
        row = self.fetchone(sql, (type_id,))
        if not row:
            return None
        return RoomType(
            type_id=row[0],
            description=row[1],
            max_guests=row[2]
        )


