from typing import List
from model.address import Address
#from data_access.address_data_access import get_all_addresses
from data_access.address_data_access import AddressDataAccess


class AddressManager:
    def __init__(self, address_dal: AddressDataAccess):
        self.address_dal = address_dal

    def get_all_addresses(self) -> Address:
        return self.address_dal.read_all_addresses()

    def find_address_by_id(self, address_id: int) -> Address:
        return self.address_dal.read_address_by_id(address_id)

    def create_address(self, address: Address) -> Address:
        new_id = self.address_dal.create_address(address)
        return self.address_dal.read_address_by_id(new_id)

    def update_address(self, address: Address) -> Address:
        existing = self.address_dal.read_address_by_id(address.address_id)
        if not existing:
            return None
        self.address_dal.update_address(address)
        return self.address_dal.read_address_by_id(address.address_id)

    def delete_address(self, address_id: int) -> bool:
        existing = self.address_dal.read_address_by_id(address_id)
        if not existing:
            return False
        self.address_dal.delete_address(address_id)
        return True

    def find_addresses_by_city(self, city: str) -> List[Address]:
        return self.address_dal.find_addresses_by_city(city)

    def find_address_by_zip(self, zip_code: str) -> List[Address]:
        return self.address_dal.find_addresses_by_zip(zip_code)

# def create_address(address_id: int, street: str, city: str, zip_code: str, country: str) -> Address:
#     return Address(
#         address_id=address_id,
#         street=street,
#         city=city,
#         zip_code=zip_code,
#         country=country
#     )
#

#
# def print_all_addresses():
#     addresses = list_all_addresses()
#     for address in addresses:
#         print(f"{address.street}, {address.zip} {address.city}, {address.country}")


# Test:
#address = Address(1, "Bahnhofstrasse", "Zürich", "8000", "Schweiz")
#print(f"{address.street}, {address.zip} {address.city}, {address.country}")
