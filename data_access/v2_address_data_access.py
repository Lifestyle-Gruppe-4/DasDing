from data_access.v2_base_data_access import BaseDataAccess

class AddressDataAccess(BaseDataAccess):
    def get_all_address(self) -> list:
        sql = "SELECT address_id, street, city, zip_code FROM Address"
        return self.fetchall(sql)

address_dao = AddressDataAccess()

address = address_dao.get_all_address()
for address in address:
    print(address)