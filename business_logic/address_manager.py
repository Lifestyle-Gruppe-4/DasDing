from email.headerregistry import Address
from typing import List
from model.address import Address
#from data_access.address_data_access import get_all_addresses
from data_access.address_data_access import AddressDataAccess


class AddressManager:
    def __init__(self, address_dal: AddressDataAccess):
        self.address_dal = address_dal

    def get_all_addresses(self) -> list[Address]:
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

address_dal = AddressDataAccess("../database/hotel_sample.db")
manager = AddressManager(address_dal)


addresses = manager.get_all_addresses()
for addr in addresses:
    print(addr)
