import sqlite3


class SqlData:
    """
    This class is used to connect to the sqlite database
    """
    db_file = "sqlite-latest.sqlite"

    def __init__(self):
        self.conn = sqlite3.connect(self.db_file)
        self.cursor = self.conn.cursor()

    def close(self):
        """
        Closes the connection to the database
        """
        self.conn.close()

    def execute(self, query):
        """
        Executes the given query
        :param query: the query to be executed
        :return: the result of the query
        """
        return self.cursor.execute(query)

    def commit(self):
        """
        Commits the changes to the database
        """
        self.conn.commit()