from sqlalchemy import create_engine, exc, text
from sqlalchemy import engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database


db_user = "postgres"
db_password = "password"
db_host = "localhost"
db_port = "5432"

default_connection_string = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/"
creation_engine = create_engine(default_connection_string, isolation_level="AUTOCOMMIT")
if not database_exists(creation_engine.url):
    create_database(creation_engine.url)

print(database_exists(creation_engine.url))
