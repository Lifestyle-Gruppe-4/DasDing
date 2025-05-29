from business_logic.guest_manager import GuestManager
from business_logic.address_manager import AddressManager
from business_logic.room_manager import RoomManager
from data_access.address_data_access import AddressDataAccess
from data_access.guest_data_access import GuestDataAccess
from data_access.hotel_data_access import HotelDataAccess
from business_logic.hotel_manager import HotelManager
from data_access.room_data_access import RoomDataAccess
from model.address import Address
from model.guest import Guest
from model.hotel import Hotel
from data_access.room_data_access import RoomDataAccess


db_path = "../database/hotel_sample.db"
hotel_dal = HotelDataAccess(db_path)
address_dal = AddressDataAccess(db_path)
room_dal = RoomDataAccess(db_path)

hotel_manager = HotelManager(hotel_dal)
address_manager = AddressManager(address_dal)
room_manager = RoomManager(room_dal)

user_choice = int(input("Enter max guests: "))
result = room_manager.get_room_by_max_guests(user_choice)
for room in result:
    print(room)

# def get_user_choice_plus():
#     print("\nBitte gib hier deine Kriterien ein")
#     city = input("Enter your city: ")
#     stars = int(input("Enter your minimum stars: "))
#     return city, stars
#
# city, stars = get_user_choice_plus()
# result = hotel_manager.find_by_city_and_min_stars(city, stars)
# if result:
#     for hotel in result:
#         print(f"{hotel.name} in {hotel.address.city} mit {hotel.stars} Sterne (Strasse: {hotel.address.street})")
# else:
#     print("Kein passendes Hotel gefunden")

