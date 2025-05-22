from data_access.base_data_access import BaseDataAccess
from model.address import Address

class AddressDataAccess(BaseDataAccess):
    def __init__(self, db_path:str=None):
        super().__init__(db_path)

    def read_all_addresses(self) -> list[Address]:
        sql = """
        SELECT address_id, street, city, zip_code
        FROM Address
        """
        Addresses = self.fetchall(sql)

        return [
            Address(
                address_id=row[0],
                street=row[1],
                city=row[2],
                zip_code=row[3]
            )
            for row in Addresses
        ]

if __name__ == "__main__":
    db_path = "../database/hotel_sample.db"
    address_dal = AddressDataAccess(db_path)
    addresses = address_dal.read_all_addresses()

    for address in addresses:
        print(address)


# def get_all_addresses() -> list[Address]:
#     base = BaseDataAccess("database/hotel_sample.db")
#     sql = "SELECT address_id, street, city, zip_code, country FROM address"
#     rows = base.fetchall(sql)
#
#     addresses = []
#     for row in rows:
#         address = Address(
#             address_id=row[0],
#             street=row[1],
#             city=row[2],
#             zip_code=row[3],
#             country=row[4]
#         )
#         addresses.append(address)
#
#     return addresses