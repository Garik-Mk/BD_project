from dotenv import dotenv_values
import sqlalchemy as sql


class ZooDB:
    engine: sql.Engine

    def __init__(self) -> None:
        ...

    def __connect_to_DB() -> sql.Engine:
        config = dotenv_values()
        session_url = sql.engine.URL.create(
            drivername='postgresql+psycopg2',
            username=config.get("POSTGRES_USER"),
            password=config.get("POSTGRES_PASSWORD"),
            host=config.get("POSTGRES_HOST"),
            database=config.get("POSTGRES_DB"),
            port=config.get("POSTGRES_PORT")
        )
        engine = sql.create_engine(session_url)
        return engine

    def connect_to_DB(self) -> bool:
        """Connect to database. Return True if connection established"""
        ZooDB.engine = ZooDB.__connect_to_DB()
        return True

    def create_all_tables(force=False) -> bool:
        """Creates creates all tables.

        Parameters
        ----------
        force: bool
            if true given, deletes previous tables and creates them from scratch
        """
        if not sql.inspect(ZooDB.engine).has_table('test'):
            print(False)

