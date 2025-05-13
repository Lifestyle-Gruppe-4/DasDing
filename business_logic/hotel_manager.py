from data_access.hotel_data_access import get_all_hotels, get_all_hotels_by_name, get_all_hotels_by_stars
from model.hotel import Hotel
from model.address import Address

def list_all_hotels():
    rows = get_all_hotels()
    hotels = []
    for row in rows:
        address = Address(row[3], row[4], row[5], row[6])
        hotel = Hotel(row[0], row[1], row[2], address)
        hotels.append(hotel)
    return hotels

list_all_hotels()


