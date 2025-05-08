from data_access.test_base_data_access import connect

with connect() as conn:
    params = tuple([5])
    cursor = conn.cursor()
    cursor.execute("SELECT hotel_id, name FROM Hotel WHERE hotel_id = ?", params)
    result = cursor.fetchone()
    print(result)
