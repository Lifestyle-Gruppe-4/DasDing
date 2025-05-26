from business_logic.guest_manager import GuestManager
from business_logic.address_manager import AddressManager
from data_access.address_data_access import AddressDataAccess
from data_access.guest_data_access import GuestDataAccess
from data_access.hotel_data_access import HotelDataAccess
from business_logic.hotel_manager import HotelManager
from model.address import Address
from model.guest import Guest
from model.hotel import Hotel


db_path = "../database/hotel_sample.db"
hotel_dal = HotelDataAccess(db_path)
address_dal = AddressDataAccess(db_path)

hotel_manager = HotelManager(hotel_dal)
address_manager = AddressManager(address_dal)

# user_choice = input("Enter the city of your choice: ")
# result = hotel_manager.find_by_city(user_choice)
# for hotel in result:
#     print(hotel)

def get_user_choice_plus():
    print("\nBitte gib hier deine Kriterien ein")
    city = input("Enter your city: ")
    stars = int(input("Enter your minimum stars: "))
    return city, stars

city, stars = get_user_choice_plus()
result = hotel_manager.find_by_city_and_min_stars(city, stars)
if result:
    for hotel in result:
        print(f"{hotel.name} in {hotel.address.city} mit {hotel.stars} Sterne (Strasse: {hotel.address.street})")
else:
    print("Kein passendes Hotel gefunden")

