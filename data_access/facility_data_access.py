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