import pickle
import sqlite3

class Connection:
    """Class for a database connection

    Attributes:
        conn: sqlite3 connection
    """

    def __init__(self, db_name):
        """Class constructor

        Args:
            db_name: The name of the wanted database
        """
        self.conn = sqlite3.connect(db_name)

    def pickle_data(self, to_pickle):
        pickled = pickle.dumps(to_pickle)

        return pickled

    def unpickle_data(self, to_unpickle):
        unpickled = pickle.load(to_unpickle)

        return unpickled

    def store_data(self, data):
        data = self.pickle_data(data)
        try:
            self.conn.execute("DELETE from cur_level WHERE id=1")
        except sqlite3.Error:
            pass
        self.conn.execute("INSERT INTO cur_level (data) VALUES (?)", [data])

    def get_data(self):
        try:
            to_unpickle = self.conn.execute("SELECT data FROM cur_level").fetchone()
            if to_unpickle:
                return self.unpickle_data(to_unpickle[0])
            return None
        except sqlite3.Error:
            return None