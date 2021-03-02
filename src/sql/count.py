import sqlite3


class SqlClass:
    def __init__(self):
        self.database = 'datatables.db'
        sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                            user_id integer,
                                            reddit_name text,
                                            color text,
                                            PRIMARY KEY (user_id)
                                        ); """

        # create a database connection
        conn = self.create_connection(self.database)
        # create tables
        if conn is not None:
            pass
            # self.create_table(conn, sql_create_guilds_table)
            # self.create_table(conn, sql_create_users_table)
            # self.create_table(conn, sql_create_roles_table)
            # self.create_table(conn, sql_create_user_role_table)
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
            conn = sqlite3.connect(db_file)
            return conn
        except Exception as e:
            print(e)

        return conn

    @staticmethod
    def create_table(conn, create_table_sql: str) -> None:
        """ create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except Exception as e:
            print(e)

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

    ############################################################