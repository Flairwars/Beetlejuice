import sqlite3


class SqlBaseCommands:
    def __init__(self, tables: list):
        self.database = 'datatables.db'
        # create a database connection
        conn = self.create_connection(self.database)
        # create tables
        if conn is not None:
            conn.execute("PRAGMA foreign_keys = ON")
            for table in tables:
                conn.execute(table)
        else:
            print("Error! cannot create the database connection.")

    @staticmethod
    def create_connection(db_file):
        """ create a database connection to the SQLite database
            specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """
        conn = None
        try:
            # If you are testing and debugging, change which lines are commented out. you will have to do this for each sql file
            conn = sqlite3.connect(db_file)
            # conn = pymysql.connect(host=config('SQLIP'), port=int(config('SQLPORT')), user=config('SQLUSER'), password=config('SQLPASS'),
            #                       database=config('SQLDATA'))
            return conn
        except Exception as e:
            print(e)

        return conn

    def execute(self, sql: str, parms: tuple = ()) -> list:
        """Executes a single command
        :param sql:
        :param parms:
        :return:
        """
        conn = self.create_connection(self.database)

        if conn is not None:
            try:
                c = conn.cursor()
                c.execute(sql, parms)
                data = c.fetchall()
                conn.commit()
                return data
            except Exception as e:
                print(e)

    def execute_many(self, sql: str, parms: list) -> list:
        """Executes a multi line command
        :param sql: the sql command being run
        :param parms: a list of tuples of information
        :return: any output from the sql code
        """
        conn = self.create_connection(self.database)

        if conn is not None:
            try:
                c = conn.cursor()
                c.executemany(sql, parms)
                data = c.fetchall()
                conn.commit()
                return data
            except Exception as e:
                print(e)
