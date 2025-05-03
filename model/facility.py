class Facility:
    def __init__(self, facility_id:int, facility_name:str):
        self.__facility_id = facility_id
        self.__facility_name = facility_name

    def __repr__(self):
        return f"Facility(ID: {self.__facility_id}, Name: {self.__facility_name})"
    @property
    def facility_id(self)->int:
        return self.__facility_id
    @property
    def facility_name(self)->str:
        return self.__facility_name

    @facility_name.setter
    def facility_name(self, facility_name:str):
        if not facility_name:
            raise ValueError("facility_name is required")
        if not isinstance(facility_name, str):
            raise ValueError("facility_name must be a string")
        self.__facility_name = facility_name



tv = Facility(1, "TV")

print(tv)