import os
import sqlite3

def connect():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, '..', 'database', 'hotel_sample.db')
    db_path = os.path.abspath(db_path)
    conn = sqlite3.connect(db_path, detect_types=sqlite3.PARSE_DECLTYPES)
    #conn.row_factory = sqlite3.Row
    return conn
