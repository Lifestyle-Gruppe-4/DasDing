from data_access.base_data_access import connect

#Alle Hotels
def get_all_hotels():
    with connect() as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(
                "SELECT h.hotel_id, h.name, h.stars, "
                "a.address_id, a.street, a.zip_code, a.city "
                "FROM Hotel h "
                "JOIN Address a ON h.address_id = a.address_id"
            )
            result = cursor.fetchall()
            print("DB-Ergebnis:", result)
            return result
        except Exception as e:
            print("Error in SQL query:", e)
            return None

#Nach Name
def get_all_hotels_by_name(name):
    with connect() as conn:
        params = tuple([""])
        cursor = conn.cursor()
        cursor.execute("SELECT hotel_id, name FROM Hotel WHERE name ?", params)
        return cursor.fetchone()

#Nach Sternen
def get_all_hotels_by_stars(stars):
    with connect() as conn:
        params = tuple([5])
        cursor = conn.cursor()
        cursor.execute("SELECT hotel_id, name, stars FROM Hotel WHERE stars = ?", params)
        return cursor.fetchall()

get_all_hotels()