#Address Class with private variables
class Address:
    def __init__(self, address_id: int| None, street: str, city: str, zip_code: str):
        if address_id is not None and address_id < 0:
            raise ValueError("Address ID must be postive if provided")
        if not street:
            raise ValueError("Street is required")
        if not city:
            raise ValueError("City is required")
        if not zip_code:
            raise ValueError("Zip is required")

        self.__address_id = address_id
        self.__street = street
        self.__city = city
        self.__zip_code = zip_code

    @property
    def address_id(self) -> int | None:
        return self.__address_id
    @property
    def street(self) -> str:
        return self.__street
    @property
    def city(self) -> str:
        return self.__city
    @property
    def zip_code(self) -> str:
        return self.__zip_code

    @address_id.setter
    def address_id(self, address_id: int):
        self.__address_id = address_id


    def __repr__(self):
        return f"Address ID: {self.address_id}, Street: {self.street}, City: {self.city}, ZIP: {self.zip_code}"


# addr1 = Address(address_id=1,street="Hauptstrasse 5",city="Basel", zip_code="4051")
# addr2 = Address(address_id=2,street="Allendweg 69",city="Sissach", zip="4450")
# addr3 = Address(address_id=3,street="Oberer Chriesmattweg 5",city="Böckten",zip="4461")
#
# print(addr1)
# print(addr2)
# print(addr3)


#Address Class defined by Silian in a first step
#class Address:
#    def __init__(self, address_id:int,street:str,city:str, zip:str):
 #       self.address_id = address_id
  #      self.street = street
   #     self.city = city
    #    self.zip = zip

    #def __repr__(self):
     #   return (f"(ID: {self.address_id}, "
      #         f"Street: {self.street}, City: {self.city}, Zip: {self.zip})")