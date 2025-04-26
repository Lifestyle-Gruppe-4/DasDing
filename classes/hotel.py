from classes.address import Address

class Hotel:
    def __init__(self, hotel_id:int, name:str, stars:int, address:Address):
        self.hotel_id = hotel_id
        self.name = name
        self.stars = stars
        self.address = address

    def get_available_rooms(self):
        pass

    def get_rooms_by_stars(self):
        pass
