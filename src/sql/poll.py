import sqlite3
import datetime


# noinspection SqlNoDataSourceInspection
class SqlClass:
    def __init__(self):
        self.database = 'datatables.db'

        sql_create_polls_table = """CREATE TABLE IF NOT EXISTS polls (
                                            message_id integer,
                                            channel_id integer,
                                            guild_id integer,
                                            name text,
                                            time datetime,
                                            FOREIGN KEY (guild_id) REFERENCES guilds (guild_id) 
                                                ON DELETE CASCADE ON UPDATE CASCADE,
                                            PRIMARY KEY (message_id, channel_id, guild_id)
                                        );"""

        sql_create_options_table = """ CREATE TABLE IF NOT EXISTS options (
                                            message_id integer,
                                            channel_id integer,
                                            guild_id integer,
                                            emote_id integer,
                                            name text,
                                            FOREIGN KEY (message_id, channel_id, guild_id)
                                                REFERENCES polls (message_id, channel_id, guild_id) 
                                                ON DELETE CASCADE ON UPDATE CASCADE,
                                            PRIMARY KEY (emote_id, message_id, channel_id, guild_id)
                                        ); """

        sql_create_votes_table = """ CREATE TABLE IF NOT EXISTS votes (
                                            user_id integer,
                                            emote_id integer,
                                            message_id integer,
                                            channel_id integer,
                                            guild_id integer,
                                            FOREIGN KEY (emote_id, message_id, channel_id, guild_id)
                                                REFERENCES options (emote_id, message_id, channel_id, guild_id)
                                                ON DELETE CASCADE ON UPDATE CASCADE,
                                            PRIMARY KEY (user_id, emote_id, message_id, channel_id, guild_id)
                                        ); """

        # create a database connection
        conn = self.create_connection(self.database)
        # create tables
        if conn is not None:
            conn.execute("PRAGMA foreign_keys = ON")
            self.create_table(conn, sql_create_polls_table)
            self.create_table(conn, sql_create_options_table)
            self.create_table(conn, sql_create_votes_table)
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

    def add_poll(self, message_id: int, channel_id: int, guild_id: int, name: str, time: datetime = None) -> None:
        """Creates a new poll
        :param message_id: the message id of the poll
        :param channel_id: the channel id of the poll
        :param guild_id: the guild that the poll is in
        :param name: the title of the poll
        :param time: optional time at which the poll ends
        :return:
        """
        sql = """INSERT INTO polls (`message_id`, `channel_id`, `guild_id`, `name`, `time`) VALUES (?,?,?,?,?)"""
        self.execute(sql, (message_id, channel_id, guild_id, name, time))

    def add_options(self, message_id: int, channel_id: int, guild_id: int, emote_ids: list, names: list) -> None:
        """Creates all the options in the options table
        :param message_id: the message id of the poll
        :param channel_id: the channel id of the poll
        :param guild_id: the guild that the poll is in
        :param emote_ids: the emote of the poll
        :param names: the name of the option
        :return:
        """
        sql = """INSERT INTO options (`message_id`, `channel_id`, `guild_id`, `emote_id`, `name`) VALUES (?,?,?,?,?)"""
        parms = [(message_id, channel_id, guild_id, emote_ids[n], names[n]) for n in range(len(names))]
        self.execute_many(sql, parms)

    def check_votes(self, user_id: int) -> tuple:
        """Returns the name of every poll that the user has voted on
        :param user_id: the user id of the poll
        :return:
        """
        sql = """
        SELECT polls.name FROM polls, votes 
        WHERE polls.message_id = votes.message_id AND
            polls.channel_id = votes.channel_id AND
            polls.guild_id = votes.guild_id AND
            
            """  # TODO: finish this sql
