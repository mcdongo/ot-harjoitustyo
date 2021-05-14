import pickle
import sqlite3
import os

DIRNAME = os.path.dirname(__file__)
sqlite3.register_converter("pickle", pickle.loads)

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
        self.conn = sqlite3.connect(os.path.join(DIRNAME, db_name))

    def pickle_data(self, to_pickle):
        """A function which serializes the inputted data to be updated into a database

        Args:
            to_pickle: data to be serialized
        Returns:
            pickled: serialized data
        """
        pickled = pickle.dumps(to_pickle)
        return pickled

    def unpickle_data(self, to_unpickle):
        """A function which serializes the inputted data to be used in the app

        Args:
            to_unpickle: Data meant to be deserialized
        Returns:
            unpickled: deserialized data
        """
        unpickled = pickle.loads(to_unpickle)
        return unpickled
    
    def reset_player_data(self):
        """Resets player data in the database
        """
        current_health = self.pickle_data(10)
        inventory = {"Sword":1,
                     "Shield":1,
                     "Potion":1
        }
        inventory = self.pickle_data(inventory)
        level_id = self.pickle_data(0)
        self.conn.execute("DELETE FROM player_state WHERE id=1")
        self.conn.execute(
                        """INSERT INTO player_state (current_health, inventory, level_id)
                           VALUES (?, ?, ?)""", [current_health, inventory, level_id]
                        )
        self.conn.commit()

    def store_player_data(self, player, level_id):
        """Stores player data in the database

        Args:
            player: a player object
            level_id: integer, the number of the level
        """
        current_health = self.pickle_data(player.current_health)
        inventory = self.pickle_data(player.inventory)
        level_id = self.pickle_data(level_id)
        self.conn.execute(
                        "UPDATE player_state SET current_health = ?, inventory = ?, level_id = ?",
                        [current_health, inventory, level_id]
                        )
        self.conn.commit()

    def get_player_data(self):
        """Gets player data from the database

        Returns:
            Player's current health, player's inventory and the level_id which the player
            is located in
        """
        data = self.conn.execute(
                                "SELECT current_health, inventory, level_id FROM player_state"
                                ).fetchone()
        return (self.unpickle_data(data[0]),
                self.unpickle_data(data[1]), self.unpickle_data(data[2]))

    def get_map_data(self):
        try:
            to_unpickle = self.conn.execute("SELECT data FROM level_list").fetchone()
            if to_unpickle:
                return self.unpickle_data(to_unpickle[0])
            return None
        except sqlite3.Error:
            return None