from base_data_access import BaseDataAccess
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

if __name__ == "__main__":
    db_path = "../database/hotel_sample.db"
    guest_dal = GuestDataAccess(db_path)
    guests = guest_dal.read_all_guests()

    for guest in guests:
        print(guest)

