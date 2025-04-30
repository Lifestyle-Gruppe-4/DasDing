class Address:
    def __init__(self, address_id:int, stree_nr:int, city:str, zip:str):
        self.address_id = address_id
        self.stree_nr = stree_nr
        self.city = city
        self.zip = zip

    def __repr__(self):
        return(f"Address(id={self.address_id}, "
               f"{self.stree_nr}, {self.city}, {self.zip})")
