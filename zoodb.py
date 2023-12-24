from dotenv import dotenv_values
from fastapi import FastAPI, HTTPException, status
import sqlalchemy as sql
from sqlalchemy.orm import sessionmaker

import model


class ZooDB:
    engine: sql.Engine
    session: sql.orm.session.Session

    def __init__(self) -> None:
        self.connect_to_DB()
        if not sql.inspect(ZooDB.engine).has_table('zoocomplex'):
            self.create_all_tables()

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
        ZooDB.session = sessionmaker(bind=ZooDB.engine)()
        return True

    def create_all_tables(force=False) -> bool:
        """Creates creates all tables.

        Parameters
        ----------
        force: bool #TODO
            if true given, deletes previous tables and creates them from scratch
        """
        model.BASE.metadata.create_all(ZooDB.engine)


