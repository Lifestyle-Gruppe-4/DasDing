from data_access.base_data_access import BaseDataAccess
from model import facility
from model.facility import Facility

class FacilityDataAccess(BaseDataAccess):
    def __init__(self, db_path:str=None):
        super().__init__(db_path)

    def read_all_facilities(self) -> list[Facility]:
        sql = """
        SELECT facility_id, facility_name
        FROM Facilities
        """
        facilities = self.fetchall(sql)

        return [
            Facility(
                facility_id=row[0],
                facility_name=row[1]
            )
            for row in facilities
        ]

    def create_facility(self, facility: Facility) -> str:
        sql = """
        INSERT INTO Facilities (facility_name)
        VALUES (?)
        """

        params = (facility.facility_name,)
        facility_id, _ = self.execute(sql, params)
        return facility_id

    def update_facility(self, facility: Facility) -> bool:
        sql = """
        UPDATE Facilities
        SET facility_name = ?
        WHERE facility_id = ?
        """
        params = (facility.facility_name,)
        _, rows_affected = self.execute(sql, params)
        return rows_affected > 0

    def delete_facility(self, facility_id:int) -> bool:
        sql = """
        DELETE FROM Facilities WHERE facility_id = ?
        """

        params = (facility_id,)
        _, rows_affected = self.execute(sql, params)
        return rows_affected > 0

    def read_facilities_by_room_id(self, room_id: int) -> list[Facility]:
        sql = """
        SELECT f.facility_id,
               f.facility_name
        FROM Facilities AS f
        JOIN Room_Facilities AS rf
        ON f.facility_id = rf.facility_id
        WHERE rf.room_id = ?
        """
        rows = self.fetchall(sql, (room_id,))
        # Aus jeder Zeile ein Facility-Objekt bauen und zurückgeben
        return [
            Facility(
                facility_id   = row[0],
                facility_name = row[1],
            )
            for row in rows
        ]
    def assign_facility_to_room(self, room_id: int, facility_id: int) -> bool:
        sql = """
        INSERT OR IGNORE INTO Room_Facilities (room_id, facility_id)
        VALUES (?, ?)
        """
        _, rows_affected = self.execute(sql, (room_id, facility_id))
        return rows_affected > 0
