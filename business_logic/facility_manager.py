from data_access.facility_data_access import FacilityDataAccess
from model.facility import Facility

class FacilityManager:
    def __init__(self, facility_dal: FacilityDataAccess):
        self.facility_dal = facility_dal

    def get_all_facilities(self) -> list[Facility]:
        return self.facility_dal.read_all_facilities()

    def find_by_id(self, facility_id: int) -> Facility:
        facilities = self.facility_dal.read_all_facilities()
        for facility in facilities:
            if facility.facility_id == facility_id:
                return facility
        return None

    def find_by_name(self, name: str) -> Facility:
        facilities = self.facility_dal.read_all_facilities()
        for facility in facilities:
            if facility.facility_name.lower() == name.lower():
                return facility
        return None

    def add_facility(self, facility: Facility) -> Facility:
        return self.facility_dal.create_facility(facility)

    def update_facility(self, facility: Facility) -> Facility:
        return self.facility_dal.update_facility(facility)

    def delete_facility(self, facility: Facility) -> Facility:
        return self.facility_dal.delete_facility(facility)

