import sqlite3


class SqlClass:
    def __init__(self):
        self.database = 'datatables.db'
        sql_create_guilds_table = """CREATE TABLE IF NOT EXISTS guilds (
                                                    guild_id integer PRIMARY KEY,
                                                    prefix text
                                                );"""
        # create a database connection
        conn = self.create_connection(self.database)
        # create tables
        if conn is not None:
            self.create_table(conn, sql_create_guilds_table)
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

    def get_prefix(self, guild_id: int):
        """gets the prefix of the discord server"""
        sql = """select prefix from guilds where guild_id = ?"""
        return self.execute(sql, (guild_id,))

    def add_guild(self, guild_id: int, prefix: str):
        """adds a new guild to the server"""
        sql = """insert into guilds (`guild_id`, `prefix`) values (?,?)"""
        self.execute(sql, (guild_id, prefix))

    def remove_guild(self, guild_id: int):
        """removes the guild when the bot leaves the server"""
        sql = """delete from guilds where guild_id=?"""
        self.execute(sql, (guild_id,))

    def change_prefix(self, guild_id: int, prefix: str):
        """changes the prefix of the bot"""
        sql = """update guilds set prefix=? where guild_id=?"""
        self.execute(sql, (prefix, guild_id))

    def get_guilds(self) -> list:
        """
        Gets all the guilds recorded on the discord bot
        :return: a tuple of all the discord server ids
        """
        sql = """SELECT guild_id FROM guilds"""
        return self.execute(sql)

    def add_guilds(self, guilds: list, prefix) -> None:
        """
        Adds multiple guilds to the db
        :param guilds: A list of new guilds
        :return:
        """
        sql = """INSERT INTO guilds (`guild_id`, `prefix`) VALUES (?,?)"""
        parms = [(guild, prefix) for guild in guilds]
        self.execute_many(sql, parms)

    def remove_guilds(self, guilds: list) -> None:
        """
        Remove multiple guilds to the db
        :param guilds: A list of old guilds
        :return:
        """
        sql = """DELETE FROM guilds WHERE guild_id = ?"""
        parms = [(guild, ) for guild in guilds]
        self.execute_many(sql, parms)
