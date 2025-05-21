from data_access.base_data_access import BaseDataAccess
from model.address import Address

def get_all_addresses() -> list[Address]:
    base = BaseDataAccess("database/hotel_sample.db")
    sql = "SELECT address_id, street, city, zip_code, country FROM address"
    rows = base.fetchall(sql)

    addresses = []
    for row in rows:
        address = Address(
            address_id=row[0],
            street=row[1],
            city=row[2],
            zip_code=row[3],
            country=row[4]
        )
        addresses.append(address)

    return addresses