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
        addresses = self.fetchall(sql)

        return [
            Address(
                address_id=row[0],
                street=row[1],
                city=row[2],
                zip_code=row[3]
            )
            for row in addresses
        ]

    def read_address_by_id(self, address_id: int) -> Address | None:
        sql = """
        SELECT address_id, street, city, zip_code
        FROM Address
        WHERE address_id = ?
        """
        row = self.fetchone(sql, (address_id,))
        if row:
            return Address(
                address_id=row[0],
                street=row[1],
                city=row[2],
                zip_code=row[3]
            )
        return None


    def create_address(self, address: Address) -> int:
        sql = """
        INSERT INTO Address (street, city, zip_code)
        VALUES (?, ?, ?)
        """
        params = (address.street, address.city,address.zip_code)
        lastrowid, _ = self.execute(sql, params)
        return lastrowid

    def update_address(self, address: Address) -> bool:
        sql = """
        UPDATE Address
        SET street   = ?,
            city     = ?,
            zip_code = ?
        WHERE address_id = ?
        """
        params = (
            address.street,
            address.city,
            address.zip_code,
            address.address_id
        )
        _, rowcount = self.execute(sql, params)
        return rowcount > 0

    def delete_address(self, address_id: int) -> None:
        sql = """
        DELETE FROM Address
        WHERE address_id = ?
        """
        self.execute(sql, (address_id,))

    def find_addresses_by_city(self, city: str) -> list[Address]:
        sql = """
        SELECT address_id, street, city, zip_code
        FROM Address
        WHERE city = ?
        """
        rows = self.fetchall(sql, (city,))
        return [Address(address_id=row[0],
                        street=row[1],
                        city=row[2],
                        zip_code=row[3]
                        )
                for row in rows
                ]

    def find_addresses_by_zip(self, zip_code: str) -> list[Address]:
        sql = """
              SELECT address_id, street, city, zip_code
              FROM Address
              WHERE zip_code = ?
              """
        rows = self.fetchall(sql, (zip_code,))
        return [Address(address_id=row[0],
                        street=row[1],
                        city=row[2],
                        zip_code=row[3]
                        )
                for row in rows]
