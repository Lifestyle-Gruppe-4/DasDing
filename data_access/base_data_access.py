import os
import sqlite3

class BaseDataAccess:
    def __init__(self, db_connection_str: str = None):
        if db_connection_str is None:
            env_path = os.environ.get("DB_FILE")
            if env_path is None:
                # Standardpfad zur DB relativ zu diesem Dateipfad
                base_dir = os.path.dirname(os.path.abspath(__file__))
                env_path = os.path.join(base_dir, '..', 'database', 'hotel_sample.db')

            self.__db_connection_str = os.path.abspath(env_path)
        else:
            self.__db_connection_str = os.path.abspath(db_connection_str)

    def _connect(self):
        return sqlite3.connect(self.__db_connection_str, detect_types=sqlite3.PARSE_DECLTYPES)

    def fetchone(self, sql: str, params: tuple | None = ()):
        with self._connect() as conn:
            try:
                cur = conn.cursor()
                cur.execute(sql, params)
                result = cur.fetchone()
            except sqlite3.Error as e:
                conn.rollback()
                raise e
            finally:
                cur.close()
        return result

    def fetchall(self, sql: str, params: tuple | None = ()) -> list:
        with self._connect() as conn:
            try:
                cur = conn.cursor()
                cur.execute(sql, params)
                result = cur.fetchall()
            except sqlite3.Error as e:
                conn.rollback()
                raise e
            finally:
                cur.close()
        return result

    def execute(self, sql: str, params: tuple | None = ()) -> (int, int):
        with self._connect() as conn:
            try:
                cur = conn.cursor()
                cur.execute(sql, params)
            except sqlite3.Error as e:
                conn.rollback()
                raise e
            else:
                conn.commit()
            finally:
                cur.close()
        return cur.lastrowid, cur.rowcount

    def test_connection(self) -> bool:
        try:
            with self._connect() as conn:
                conn.execute("SELECT 1")
            return True
        except sqlite3.Error as e:
            print(f"Verbindungsfehler: {e}")
            return False
