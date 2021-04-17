import sqlite3


class SqlClass:
    def __init__(self):
        self.database = 'datatables.db'

        customcommands = """CREATE TABLE IF NOT EXISTS customcommands (
                                guild_id integer,
                                command_name text,
                                foreign key (guild_id) references guilds (guild_id)
                                    ON DELETE CASCADE ON UPDATE CASCADE,
                                primary key (guild_id, command_name)
                            );"""
        # create a database connection
        conn = self.create_connection(self.database)
        # create tables
        if conn is not None:
            conn.execute("PRAGMA foreign_keys = ON")
            self.create_table(conn, customcommands)

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
            #conn = pymysql.connect(host=config('SQLIP'), port=int(config('SQLPORT')), user=config('SQLUSER'), password=config('SQLPASS'),
            #                       database=config('SQLDATA'))
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
        :param sql:
        :param parms:
        :return:
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

    def get_command_guild(self, command_name):
        """
        """
        sql = """SELECT guild_id FROM customcommands WHERE command_name=?"""
        return self.execute(sql, (command_name,))

    def add_command(self, guild_id, command_name):
        """
        """
        sql = """INSERT INTO customcommands (`guild_id`, `command_name`) VALUES (?,?)"""
        self.execute(sql, (guild_id, command_name))

    def remove_command(self, guild_id, command_name):
        """
        """
        sql = """DELETE FROM customcommands WHERE guild_id=? AND command_name=?"""
        self.execute(sql, (guild_id, command_name))
