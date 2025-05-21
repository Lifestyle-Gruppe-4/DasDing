from typing import List
from model.address import Address
from data_access.address_data_access import get_all_addresses

def create_address(address_id: int, street: str, city: str, zip_code: str, country: str) -> Address:
    return Address(
        address_id=address_id,
        street=street,
        city=city,
        zip_code=zip_code,
        country=country
    )

def list_all_addresses() -> list[Address]:
    return get_all_addresses()

def print_all_addresses():
    addresses = list_all_addresses()
    for address in addresses:
        print(f"{address.street}, {address.zip} {address.city}, {address.country}")


# Test:
#address = Address(1, "Bahnhofstrasse", "Zürich", "8000", "Schweiz")
#print(f"{address.street}, {address.zip} {address.city}, {address.country}")
