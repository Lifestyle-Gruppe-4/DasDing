from data_access.base_data_access import BaseDataAccess
from model.guest import Guest
from model.address import Address

class GuestDataAccess(BaseDataAccess):
    def __init__(self, db_path:str=None):
        super().__init__(db_path)

    def read_all_guests(self) -> list[Guest]:
        sql = """
        SELECT g.guest_id, g.first_name, g.last_name, g.email, a.address_id, a.street, a.city, a.zip_code
        FROM Guest g
        JOIN Address a ON g.address_id = a.address_id
        """
        guests = self.fetchall(sql)

        return [
            Guest(
                guest_id=row[0],
                first_name=row[1],
                last_name=row[2],
                email=row[3],
                address=Address(
                    address_id=row[4],
                    street=row[5],
                    city=row[6],
                    zip_code=row[7]
                )
            )
            for row in guests
        ]

    def create_guest(self, guest: Guest) -> int:
        sql = """
        INSERT INTO Guest (first_name, last_name, email, address_id)
        VALUES (?,?,?,?)
        """

        params = (guest.first_name, guest.last_name, guest.email, guest.address.address_id)
        guest_id, _ = self.execute(sql, params) # "_" anstelle von rows_affected. nicht nötig bei Insert.
        return guest_id

    def update_guest(self, guest: Guest) -> bool:
        sql = """
        UPDATE Guest
        SET first_name = ?, last_name = ?, email = ?, address_id = ?
        WHERE guest_id = ?
        """
        params = (
            guest.first_name,
            guest.last_name,
            guest.email,
            guest.address.address_id,
            guest.guest_id
        )
        _, rows_affected = self.execute(sql, params)
        return rows_affected > 0

    def delete_guest(self, guest_id: int) -> bool:
        sql = """
        DELETE FROM Guest WHERE guest_id = ?
        """
        params = (guest_id,)
        _, rows_affected = self.execute(sql, params)
        return rows_affected > 0


