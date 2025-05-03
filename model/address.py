class Address:
    def __init__(self, address_id:int,street:str,city:str, zip:str):
        self.address_id = address_id
        self.street = street
        self.city = city
        self.zip = zip

    def __repr__(self):
        return (f"(ID: {self.address_id}, "
               f"Street: {self.street}, City: {self.city}, Zip: {self.zip})")

addr1 = Address(address_id=1,street="Hauptstrasse 5",city="Basel", zip="4051")
addr2 = Address(address_id=2,street="Bahnhofstrasse 27",city="Bern", zip="3001")

